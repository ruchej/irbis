class App:

    http_method_names = ["GET", "POST", "PUT", "DELETE"]

    def __init__(self, urlpatterns: dict, middlewares: list):

        self.urlpatterns = urlpatterns
        self.middlewares = middlewares

    def __call__(self, env: list, func_response) -> str:
        request_method = env['REQUEST_METHOD']
        path = env["PATH_INFO"].rstrip("/")
        if path in self.urlpatterns:
            view = self.urlpatterns[path]
            request = {}
            for middleware in self.middlewares:
                middleware(request)
            code, text = view(request)
            func_response(code, [("Content-Type", "text/html")])
            return [text.encode("utf-8")]
        else:
            func_response("404 NOT FOUND", [("Content-Type", "text/html")])
            return [b"Not Found"]
