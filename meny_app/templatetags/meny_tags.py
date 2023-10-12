from django import template
from django.urls import reverse
from meny_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('meny_app/meny_template.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path_info

    # Загрузим все пункты этого меню в память
    all_items = list(MenuItem.objects.filter(menu_name=menu_name).order_by('parent_id'))

    # Найдем активный пункт
    active_item = None
    for item in all_items:
        if item.named_url:
            item.url = reverse(item.named_url)
        if item.url == current_url:
            active_item = item
            break

    return {'all_items': all_items, 'active_item': active_item}
