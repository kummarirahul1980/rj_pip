class UrlGenerator:
    @staticmethod
    def __init__ (**kwargs):
        host  = kwargs.get("hostname")
        port = kwargs.get("port")
        path = kwargs.get("path","")
        return f"http://{host}:{port}/{path}"
    

class jsonify:
    @staticmethod
    def __init__(**kwargs):
        return kwargs

    def returnjson (dictionary = {} , message="", error= "", status="failed", info="", **args):
        dictionary.setdefault("message", message)
        dictionary.setdefault("status",status)
        dictionary.setdefault("info", info)
        dictionary.update(args)

        return dictionary