from django.shortcuts import render


def page_view(request):
    return render(request, 'meny_app/page.html')


def secondary_menu_view(request):
    return render(request, 'meny_app/secondary_meny.html')


def third_menu_view(request):
    return render(request, 'meny_app/third_menu.html')
