import prog28
from importlib import reload # helps to reload the other file module ex: prog28
print('Hello from program29 module')
reload(prog28) # reload the module prog28
print('Hello from program29 module after reloading prog28')
reload(prog28) # reload the module prog28
print('Hello from program29 module after reloading prog28 again')