from django.views.generic.simple import direct_to_template
from django.views.decorators.cache import cache_page
from django.shortcuts import *
from django.template import TemplateDoesNotExist
import logging
logging.getLogger().setLevel(logging.NOTSET)

from models import *
import engsoc_events

import re
useful=re.compile(r'^/(?!base_)([^\.]*?)(?:\.html)?$')

@cache_page(10)
def index(request):
        match=useful.match(request.path)
        if match:
                try:
                        return render_to_response((match.group(1)or"index")+".html",{
				'panels':dumps([[x.action,x.argument,x.duration]for x in engsoc_events.models.Panel.objects.all()]),
			})
                except TemplateDoesNotExist as e:
                        logging.error(e)
        return redirect("/static"+request.path,{
		'panels':dumps([[x.action,x.argument,x.duration]for x in engsoc_events.models.Panel.objects.all()]),
	})

from django.contrib.admin.views.decorators import staff_member_required
from django.middleware.csrf import get_token
from json import dumps

@staff_member_required
def modify(request):
	form=None
	if request.method=='POST':
		form=ModifyForm(request.POST)
		form.full_clean()
		ent=engsoc_events.models.Event.objects.get(eid=str(form.data['eid']))
		if ent:
			ent.extra_html=form.data['extra_html']
			ent.save()
			engsoc_events.update()
			form=ModifyForm(request.POST,ent)
		elif form.is_valid():
			form.save()
			engsoc_events.update()
	return render_to_response('base_modify.html',{
		'form':form,
		'events':engsoc_events.events,
		'panels':dumps([[x.action,x.argument,x.duration]for x in engsoc_events.models.Panel.objects.all()]),
		'csrf_token':get_token(request),
	})
