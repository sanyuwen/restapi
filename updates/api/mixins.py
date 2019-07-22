from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# do not use CSRF in production, this is just for test
class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

