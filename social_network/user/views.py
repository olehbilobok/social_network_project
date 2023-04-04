from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from user.serializers import UserSerializer
from rest_framework import response, status
from user.models import UserActivity


class UserRegistration(generics.GenericAPIView):

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserActivityViewList(APIView):

    @staticmethod
    def get(request):
        activities = UserActivity.objects.all()
        data = []
        for activity in activities:
            user_id = activity.user.id
            if user_id not in [value.get('user_id') for value in data]:
                user_activity = UserActivity.objects.filter(user=user_id).last()
                data.append(
                    {
                        'user_id': user_id,
                        'last_request': user_activity.timestamp,
                        'last_login': user_activity.user.last_login
                    }
                )
        return response.Response(data)


class UserActivityViewDetail(APIView):

    @staticmethod
    def get(request, pk):
        try:
            activity = UserActivity.objects.filter(user=pk).last()
            data = {
                'last_request': activity.timestamp,
                'last_login': activity.user.last_login
            }
            return response.Response(data)
        except ObjectDoesNotExist:
            raise Http404


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return response.Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
