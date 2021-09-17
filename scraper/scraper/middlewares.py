import random

from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
from stem.util.log import get_logger


def _set_new_ip():
    logger = get_logger()
    logger.propagate = False

    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='tor_password')  # tor password
        controller.signal(Signal.NEWNYM)


def _get_user_agent():
    ua = UserAgent()

    return random.choice([ua.chrome, ua.firefox, ua.safari, ua.google])


class ProxyMiddleware:
    def process_request(self, request, spider):
        _set_new_ip()
        request.headers['User-Agent'] = _get_user_agent()
        request.meta['proxy'] = 'http://127.0.0.1:8118'  # standart privoxy address and port
