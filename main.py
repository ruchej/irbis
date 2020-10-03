from irbis import App

import views


urlpatterns = {'/about': views.about_view}


def secret_control(request):
    request['secret_key'] = 'SECRET'


front_controllers = [secret_control]

app = App(urlpatterns, front_controllers)

