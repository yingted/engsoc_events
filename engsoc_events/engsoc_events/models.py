from django.contrib import admin
from django.db.models import *
class Panel(Model):
	action = CharField(max_length=32,choices=(('src','src'),('src-t','src-t'),('xss','xss'),('html','html'),('img','img')),default='src-t')
	argument = TextField()
	order = IntegerField(default=0)
	duration = IntegerField(default=300000)
admin.site.register(Panel)
	
class Event(Model):
	eid = CharField(max_length=256,primary_key=True)
	extra_html = TextField()
admin.site.register(Event)

from django.forms import *
class ModifyForm(ModelForm):
	class Meta:
		model=Event
		fields=["eid","extra_html"]
