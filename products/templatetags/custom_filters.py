from django import template

register = template.Library()


@register.filter
def subtract(value, arg):
    return value - arg


@register.simple_tag
def get_page_range(current_page, total_pages):
    if total_pages <= 3:
        return range(1, total_pages + 1)
    else:
        if current_page == 1:
            return [1, None, round(total_pages / 2), None, total_pages]
        elif current_page == 2:
            return [1, current_page, None, total_pages]
        elif current_page == total_pages - 1:
            return [1, None, current_page, total_pages]
        elif current_page == total_pages:
            return [1, None, round(total_pages / 2), None, total_pages]
        else:
            return [1, None, current_page, None, total_pages]
