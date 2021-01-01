# Levels
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50


class CheckMessage:
    def __init__(self, level, msg, hint=None, obj=None, id=None):
        self.level = level
        self.msg = msg
        self.hint = hint
        self.obj = obj
        self.id = id


class Critical(CheckMessage):
    pass


class Debug(CheckMessage):
    pass


class Error(CheckMessage):
    pass


class Info(CheckMessage):
    pass


class Warning(CheckMessage):
    pass
