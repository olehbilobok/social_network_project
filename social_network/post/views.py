from django.db.models import Count
from rest_framework import response, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from post.models import Post, Like
from post.serializers import PostSerializer, LikeSerializer


class POSTList(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return response.Response(serializer.data)

    @staticmethod
    def post(request):
        request.data['user'] = request.user.id
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeDetail(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        body = {
            "user": request.user.id,
            "post": pk
        }
        like = Like.objects.filter(post=pk).filter(user=request.user.id)
        if not like:
            serializer = LikeSerializer(data=body)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            like.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)


class AnalyticsView(APIView):
    pagination_class = LimitOffsetPagination

    def get(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')

        likes_per_day = Like.objects.filter(
            created_at__gte=date_from if date_from else '1900-01-01T08:30:01.428744Z',
            created_at__lte=date_to if date_to else '3000-01-01T08:30:01.428744Z').\
            extra(select={'created_at': 'date(created_at)'}).values('post', 'created_at').\
            annotate(count=Count('created_at'))

        data = {}
        for post_like in likes_per_day:
            post_id = post_like['post']
            created_at = post_like['created_at']
            count = post_like['count']
            if post_id not in data:
                post = Post.objects.get(pk=post_id)
                serializer = PostSerializer(post)
                data[post_id] = {
                    'post': serializer.data,
                    'likes_per_day': {created_at: count}
                }
            else:
                data[post_id]['likes_per_day'][created_at] = count
        return response.Response(data)

