# from .models import AcademicSession, AcademicTerm


# class SiteWideConfigs:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         current_session = AcademicSession.objects.get(current=True)
#         current_term = AcademicTerm.objects.get(current=True)

#         request.current_session = current_session
#         request.current_term = current_term

#         response = self.get_response(request)

#         return response


### new

from django.core.exceptions import ObjectDoesNotExist
from .models import AcademicSession, AcademicTerm

class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            current_session = AcademicSession.objects.get(current=True)
            request.current_session = current_session
        except ObjectDoesNotExist:
            request.current_session = None

        try:
            current_term = AcademicTerm.objects.get(current=True)
            request.current_term = current_term
        except ObjectDoesNotExist:
            request.current_term = None

        response = self.get_response(request)
        return response
