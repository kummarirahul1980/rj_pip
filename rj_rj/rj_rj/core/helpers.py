# def jsonify(update={}, *args: dict, **kwargs) -> dict:
#     # update = {}
#     for i in args:
#         if isinstance(i, dict):
#             update.setdefault("kwargs", {})
#             update["kwargs"].update(i)

#         else:
#             update.setdefault("args", [])
#             update["args"].append(i)

#     for i in kwargs:
#         update.setdefault(i, kwargs.get(i))

#     return update


# def jsonify(*args, ___ignore_empty__=False, **kwargs) -> dict:
#     result = {}

#     # Process all positional arguments (dicts or single values)
#     for item in args:
#         if isinstance(item, dict):
#             if ___ignore_empty__:
#                 continue
#             # Merge dictionary and filter out empty strings/None values if needed
#             for key, val in item.items():
#                 if val:  # Filters out empty values like "", None, []
#                     result[key] = val
#         else:
#             # Handle non-dict positional items
#             result.setdefault("args", []).append(item)

#     # Process keyword arguments (kwargs override positional args)
#     for key, val in kwargs.items():
#         if val:
#             result[key] = val

#     return result


import json


def jsonify(*args, ___ignore_empty__=False, **kwargs) -> dict:
    result = {}

    def is_valid(val):
        if ___ignore_empty__:
            return True
        # Filter out None, empty strings, and empty collections (lists/dicts/tuples)
        if val is None or val == "":
            return False
        if isinstance(val, (list, dict, set, tuple)) and len(val) == 0:
            return False
        return True

    # 1. Process positional arguments
    for item in args:
        if isinstance(item, dict):
            for key, val in item.items():
                if is_valid(val):
                    result[key] = val
        else:
            if is_valid(item):
                result.setdefault("args", []).append(item)

    # 2. Process keyword arguments
    for key, val in kwargs.items():
        if is_valid(val):
            result[key] = val

    return result


class STATUS:
    # --- 2xx Success ---
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204

    # --- 3xx Redirection ---
    MOVED_PERMANENTLY = 301
    FOUND = 302
    NOT_MODIFIED = 304

    # --- 4xx Client Errors ---
    BAD_REQUEST = 400
    UNAUTHENTICATED = 401
    UNAUTHORIZED = 403  # Forbidden
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    TOO_MANY_REQUESTS = 429

    # --- 5xx Server Errors ---
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504

    # Mapping codes to human-readable status phrases
    _MESSAGES = {
        200: "OK",
        201: "Created",
        202: "Accepted",
        204: "No Content",
        301: "Moved Permanently",
        302: "Found",
        304: "Not Modified",
        400: "Bad Request",
        401: "Unauthenticated",
        403: "Unauthorized",
        404: "Not Found",
        405: "Method Not Allowed",
        409: "Conflict",
        422: "Unprocessable Entity",
        429: "Too Many Requests",
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
    }

    def __init__(self, code):
        if code not in self._MESSAGES:
            raise ValueError(f"Invalid or unsupported status code: {code}")

        self.status = code
        self.message = self._MESSAGES[code]

    def __repr__(self):
        return f"<STATUS code={self.status} message='{self.message}'>"


class returnjson:
    @staticmethod
    def _N_GET_STATUS_CODES():
        return STATUS

    def __init__(
        self,
        dictionary={},
        message="",
        error="",
        status="failed",
        info="",
        status_code=200,
        **args,
    ):
        args.setdefault("data", None)
        dictx = jsonify(
            dictionary,
            args,
            message=message,
            status_code=status_code,
            error=error,
            status=status,
            info=info,
            ___ignore_empty__=True,
        )

        self.__dict__.update(dictx)

    @property
    def json(self):
        return self.__dict__

    def __str__(self):
        import json

        return json.dumps(self.__dict__, indent=2)

    def __repr__(self):
        return json.dumps(self.__dict__, indent=2)

    @staticmethod
    def _N_SERVER_ERROR():
        return returnjson(
            message="Server Caught Exception",
            status_code=500,
            error="InternalServerError",
        )

    @staticmethod
    def _N_STATUS_OK():
        return returnjson(
            message=STATUS._MESSAGES.get(STATUS.OK), status_code=STATUS.OK, status="ok"
        )

    @staticmethod
    def _N_JSON_DECODE_ERROR():
        return returnjson(
            message="Please provide a valid json format.",
            status_code=STATUS.BAD_REQUEST,
            error="JSONDecodeError",
        )


# class comjson:
#     def __init__(
#         self,
#         message="",
#         error="",
#         status="failed",
#         info="",
#         object=None,
#         data={},
#         **args
#     ):
#         self.__dict__.update(
#             jsonify(
#                 error=error,
#                 message=message,
#                 info=info,
#                 data=data,
#                 object=object,
#                 **args,
#                 status=status,
#             )
#         )

import json


class comjson:
    def __init__(
        self,
        dictionary=None,
        message="",
        error="",
        status="failed",
        info="",
        object=None,
        data=None,
        **args,
    ):
        if dictionary is None:
            dictionary = {}

        # Merge extra keyword arguments into dictionary if provided
        combined_dict = {**dictionary, **args}

        # Filter empty strings, Nones, and empty collections
        dictx = jsonify(
            combined_dict,
            message=message,
            error=error,
            status=status,
            info=info,
            object=object,
            data=data,
            ___ignore_empty__=True,
        )

        self.__dict__.update(dictx)

    @property
    def json(self):
        return self.__dict__

    def __str__(self):
        return json.dumps(self.__dict__, indent=2)

    def __repr__(self):
        return json.dumps(self.__dict__, indent=2)


if __name__ == "__main__":

    def printf(*args, **kwargs):
        import json

        for i in args:
            if isinstance(i, tuple):
                kwargs.setdefault("args", {})
                kwargs["args"].update(args)
        finaldict = (
            kwargs.update(args)
            if isinstance(args, dict)
            else kwargs.setdefault("args", args)
        )
        print(type(args))
        print(json.dumps(kwargs, indent=2))

    def printf(*args, **kwargs):
        print(*args, **kwargs)

    print(jsonify(returnjson().json, message="test", **returnjson().json))
    print(returnjson(obj="Hello world string").json)
    print(comjson(neekenduuku="Chaduvuko first").json)
