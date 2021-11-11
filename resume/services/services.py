from django.core.exceptions import ObjectDoesNotExist

from ..models import Resume


def get_resume(request):
    try:
        return Resume.objects.filter(user=request.user.pk)
    except ObjectDoesNotExist:
        return None


def get_resume_on_pk(pk):
    try:
        return Resume.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return None
