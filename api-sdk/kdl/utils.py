# -*- coding: utf-8 -*-
from functools import wraps

from kdl.exceptions import KdlNameError


def signature_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.auth.apiKey:
            raise KdlNameError("apiKey is required for signature")
        return func(self, *args, **kwargs)
    return wrapper


class OpsOrderLevel(object):
    """开放代理订单级别"""
    NORMAL = "dev"  # 普通
    VIP = "dev"  # vip
    SVIP = "svip"  # svip
    PRO = "ent"  # 专业版