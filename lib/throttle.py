from rest_framework.throttling import UserRateThrottle


class LoginThrottle1(UserRateThrottle):
    scope = 'login1'


class LoginThrottle2(UserRateThrottle):
    scope = 'login1'
