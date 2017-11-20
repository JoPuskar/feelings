import datetime
import json
from django import template
from django.utils import timezone

from ..forms import ThoughtForm

register = template.Library()


@register.inclusion_tag('thoughts/_form.html')
def thought_form():
    form = ThoughtForm()
    return {'form': form}


@register.simple_tag(takes_context=True)
def chart_data(context):
    user = context['user']
    days_ago = timezone.now() - datetime.timedelta(days=10)
    thoughts = user.thoughts.filter(recorded_at__gte=days_ago)
    return json.dumps({
        'labels': [thought.recorded_at.strftime('%y-%m-%d') for thought in thoughts],
        'series': [[thought.condition for thought in thoughts]]
    })