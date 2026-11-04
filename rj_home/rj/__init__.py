from sys import stderr, modules,exit



from importlib import import_module
class RJModuleNotFoundException (Exception):
   def __init__(self, message, *args):
      self.message = message
      super().__init__(message,*args)

if "-h" in sys.argv or "--help":
   print("The rj home acts as as a translation layer between rj_core like apps starting with rj_*, translating it to under single namespace, rj.* , allowing to just import single namespace and could able to access the complete rj system using single namespace. Yet the project is intended under developement, and now wworking. This would be resolved in future updates. Please contact github.com/kummarirahul1980 or wait fo rupdates.")
   print("With regards,  RJ DEVELOPERS TEAM Cheif")
   print("Rahul")
raise RJModuleNotFoundException("The module rj_home is not ready yet. Will be ready soon .please wait for future updates.")
try :
   from rj.AVAILABLE_MODULES import APPS

   for i in APPS:
      i = i.lower()

      try :
         pkg_name = "rj_"+i
         module = import_module (pkg_name)
         modules[f"rj.{i}"] = module
         globals()[f"rj.{i}"] = module
         
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


print("Import namespace rj.")