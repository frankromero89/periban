from django.shortcuts import render

from menus.models import Menu, Platillo

# Create your views here.
def menus(request):    
    menus = Menu.objects.all()
    return render(request, 'menus/menus.html', {'menus': menus} )

def platillos(request, name):
    menus = Menu.objects.all()
    platillo = Platillo.objects.get(url_name=name)
    return render(
        request=request,
        template_name='menus/platillo.html',
        context={
            'menus': menus,
            'platillo': platillo
        }
    )

def menu(request, menu_name):
    menus = Menu.objects.all()
    platillos = Platillo.objects.filter(menu__name=menu_name)
    return render(
        request=request,
        template_name='menus/menu.html',
        context={
            'menus': menus,
            'platillos': platillos
        }
    )