from user.models import UserActivity


class UserActivityMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            activity = UserActivity.objects.create(user=request.user, action=request.path)
            activity.save()

        return response
