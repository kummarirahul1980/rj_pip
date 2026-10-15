from sys import stderr, path
from importlib import import_module
class RJModuleNotFoundException (Exception):
   def __init__(self, message, *args):
      self.message = message
      super().__init__(message,*args)
try :
   from rj.AVAILABLE_MODULES import APPS

   for i in APPS:
      i = i.lower()

      try :
         module = import_module ("rj_"+i)
         
      except ModuleNotFoundError as e :
         pass
         

except ModuleNotFoundError as e :
   if e.name == "rj" :
      print("Error ", file=stderr)
      raise RJModuleNotFoundException("RJ module, 'rj_home' was not installed. Installed it with \\pip install rj_home\\.")

   elif e.name == "rj.AVAILABLE_MODULES":
      raise RJModuleNotFoundException("'AVAILABLE_MODULES' was not declared in the package. Please wait for updates or you can ask for support at http://github.com/kummarirahul1980/")

except ImportError as e :
   print("Name space was not defined or missing. Plesae contact support or wait for updates.")
   raise e from None

# Core focues on fundamentals of python helpers like validators of the basic form filling and while mail focuses on mailing Helper functions for developers. In this version, there is no readme documented. 
