from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def filter_all(arg_list, k):
    ret = ""
    if k == "article_type_id":
        n1 = arg_list['article_type_id']
        n2 = arg_list['category_id']
        if n1 == 0:
            ret = '<a class="active" href="/article-0-%s.html">全部</a>' % n2
        else:
            ret = '<a class="active" href="/article-0-%s.html">全部</a>' % n2
    else:
        n1 = arg_list['category_id']
        n2 = arg_list['article_type_id']
        if n1 == 0:
            ret = '<a class="active" href="/article-%s-0.html">全部</a>' % n2
        else:
            ret = '<a class="active" href="/article-%s-0.html">全部</a>' % n2
    return mark_safe(ret)

@register.simple_tag
def filter_article_type(article_type,arg_list):
    """
         {% for row in article_type %}
                {% if row.id == arg_list.article_type_id %}
                <a class="active" href="/article-{{ row.id }}-{{ arg_list.category_id }}.html">{{ row.caption }}</a>
                {% else %}
                <a href="/article-{{ row.id }}-{{ arg_list.category_id }}.html">{{ row.caption }}</a>
                {% endif %}
        {% endfor %}
    """
    ret = []
    for row in article_type:
        print(row[0],row[1],arg_list)
        if row[0] == arg_list['article_type_id']:
            temp = '<a class="active" href="/article-%s-%s.html">%s</a>'%(row[0],arg_list['category_id'],row[1])
        else:
            temp = '<a href="/article-%s-%s.html">%s</a>'%(row[0],arg_list['category_id'],row[1])
        ret.append(temp)
    return mark_safe("".join(ret))

@register.simple_tag
def filter_category(category,arg_list):
    ret = []
    for row in category:
        if row.id == arg_list['category_id']:
            temp =  '<a class="active" href="/article-%s-%s.html">%s</a>'%(arg_list['article_type_id'],row.id,row.caption,)
        else:
            temp = '<a href="/article-%s-%s.html">%s</a>'%(arg_list['article_type_id'],row.id,row.caption,)
        ret.append(temp)
    return mark_safe("".join(ret))