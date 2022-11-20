import time
import logging

from django.utils.deprecation import MiddlewareMixin


class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        logging.basicConfig(filename='logs.log')
        logging.warning(duration)
        return response

