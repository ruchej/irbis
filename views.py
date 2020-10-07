from irbis.template import render


def about_view(request):
    return "200 OK", render("about.j2", info="Дополнительно")
