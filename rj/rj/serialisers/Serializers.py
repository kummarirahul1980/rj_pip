



def dynamic_model_serialiser(cls,fields="__all__",**kwargs):
  try:
    from rest_framework import serializers
    
    
  except:
    raise ImportError("rest_framework is not installed.")
  MetaClass = type(
    "Meta",(),{ "fields" : fields, "model" : cls } 
    )
    
  DynamicSerialiserClass = type (
    "DynamicSerialiser",
    (serializers.ModelSerializer,)
    , { "Meta" : MetaClass }
    )
  return DynamicSerialiserClass(cls) 