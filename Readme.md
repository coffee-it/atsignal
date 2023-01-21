The `atsignal` module defines functions to register cleanup functions. Functions thus registered are automatically executed upon interpreter termination with the registered signal.

### `atexit.SignalHandler.register(signal, func, *args, **kwargs)`

Register `func` as a function to be executed at termination by specified `signal`. Any optional arguments that are to be passed to `func` must be passed as arguments to `register()`. It is possible to register the same function and arguments more than once.

### `atexit.sigint(func)`

Register `func` as a function to executed at termination by SIGINT (2). Does not pass any arguments to the `func`. Convenient to use as a decorator.

### `atexit.sigterm(func)`

Register `func` as a function to executed at termination by SIGTERM (15). Does not pass any arguments to the `func`. Convenient to use as a decorator.

```
import time
from atsignal import sigterm, sigint

@sigint
def interrupt():
  print("SIGINT")

@sigterm
def terminate():
  print("SIGTERM")

while 1:
  time.sleep(1)

```

```
import atsignal, time

def interrupt(*args, **kwargs):
  print("SIGINT", args, kwargs)

# register SIGINT
atsignal.SignalHandler.register(2, interrupt, "one", 2, [3, 4, 5], foo="bar")

# register SIGTERM
atsignal.SignalHandler.register(15, interrupt)

while 1:
  time.sleep(1)

```