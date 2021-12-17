from django.core.exceptions import ObjectDoesNotExist

from user.models import CustomUser


def get_user(request) -> object:
    try:
        user = CustomUser.objects.get(pk=request.user.pk)
        return user
    except ObjectDoesNotExist:
        return None
