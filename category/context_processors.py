from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

#ab is context processor ko setting.py file mein b add krna hai