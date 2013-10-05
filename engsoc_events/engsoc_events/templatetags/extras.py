from django import template
register=template.Library()
import engsoc_events

@register.inclusion_tag("base_event_list.html")
def event_list(count):
	return{
		"events":engsoc_events.events,
	}
