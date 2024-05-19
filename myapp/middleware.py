from django.http import HttpResponseForbidden
class BlockedIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        # Check if the IP address is blocked
        if ip_address in blocked_ip_list:
            return HttpResponseForbidden("Access Forbidden")
        response = self.get_response(request)
        return response