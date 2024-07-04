from django import template
from users.models import Category
register = template.Library()
@register.inclusion_tag('catg.html')
def catg():
    categories = Category.objects.all()
    return{'categories':categories}
