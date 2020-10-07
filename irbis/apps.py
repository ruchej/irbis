class App:
    def __init__(self, urlpatterns: dict, front_controllers: list):

        self.urlpatterns = urlpatterns
        self.front_controllers = front_controllers

    def __call__(self, env: list, func_response) -> str:
        path = env["PATH_INFO"].rstrip("/")
        if path in self.urlpatterns:
            view = self.urlpatterns[path]
            request = {}
            for controller in self.front_controllers:
                controller(request)
            code, text = view(request)
            func_response(code, [("Content-Type", "text/html")])
            return [text.encode("utf-8")]
        else:
            func_response("404 NOT FOUND", [("Content-Type", "text/html")])
            return [b"Not Found"]
