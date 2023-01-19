import signal
from sys import exit as sys_exit
from micropython import const
import logging, time

atsignal_log = logging.getLogger("atsignal")

# SIG_DFL = const(0)
# SIG_IGN = const(1)
SIGINT  = const(2)
SIGPIPE = const(13)
SIGTERM = const(15)

class SignalHandler(object):
    _instance = None
    HANDLERS = {}
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SignalHandler, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def register(cls, signum:int, callback:function):
        if signum in cls.HANDLERS:
            cls.HANDLERS[signum].append(callback)
        else:
            cls.HANDLERS.update({signum: [callback]})
            atsignal_log.debug("Bind signal to %s %s" % (signum, cls.signal_wrapper))
            signal.signal(signum, cls.signal_wrapper)

    @classmethod
    def signal_wrapper(cls, signum):
        atsignal_log.debug("Received signal %s" % signum)
        if signum in cls.HANDLERS:
            for _h_cb in cls.HANDLERS[signum]:
                _h_cb()
        atsignal_log.debug("Exit with code %s" % signum)
        sys_exit(signum)

def sigint(func) -> None:
    SignalHandler.register(signum=SIGINT, callback=func)
def sigterm(func) -> None:
    SignalHandler.register(signum=SIGTERM, callback=func)