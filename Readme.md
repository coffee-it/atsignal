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
import atsignal

def interrupt():
  print("SIGINT")

@sigterm
def terminate():
  print("SIGTERM")

# register SIGINT
atsignal.SignalHandler.register(2, interrupt)

# register SIGTERM
atsignal.SignalHandler.register(15, interrupt)

while 1:
  time.sleep(1)

```