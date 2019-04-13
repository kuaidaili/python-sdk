# -*- coding: utf-8 -*-

import sys


class KdlException(Exception):
    """异常类"""

    def __init__(self, code=None, message=None):
        self.code = code
        self.message = message
        self._hint_message = "[KdlException] code: {} message: {}".format(self.code, self.message)

    @property
    def hint_message(self):
        return self._hint_message

    @hint_message.setter
    def hint_message(self, value):
        self._hint_message = value

    def __str__(self):
        if sys.version_info[0] < 3 and isinstance(self.hint_message, unicode):
            return self.hint_message.encode("utf8")
        else:
            return self.hint_message


class KdlStatusError(KdlException):
    """状态码异常类"""
    def __init__(self, code, message):
        super(KdlStatusError, self).__init__(code, message)
        self.hint_message = "[KdlStatusError] status_code: {}, message: {}".format(self.code, self.message)


class KdlNameError(KdlException):
    """ 参数异常类 """
    def __init__(self, message, code=-2):
        super(KdlNameError, self).__init__(code, message)
        self.hint_message = "[KdlNameError] message: {}".format(self.message)


class KdlTypeError(KdlException):
    """ 类型异常类 """
    def __init__(self, message, code=-1):
        super(KdlTypeError, self).__init__(code, message)
        self.hint_message = "[KdlTypeError] message: {}".format(self.message)