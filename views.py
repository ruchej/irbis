from irbis.template import render

def about_view(request):
    return '200 OK', render('templates/about.html', info='Дополнительно')
