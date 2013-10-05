from threading import Timer,Lock
from json import load
from urllib2 import urlopen
_calendar_url = 'http://www.google.com/calendar/feeds/um08n4cml235750sucn1vmgqd0@group.calendar.google.com/public/full?alt=jsonc&orderby=starttime&max-results=25&sortorder=ascending&futureevents=true&ctz=America/Toronto&singleevents=true'
def every(seconds,args=()):
	def wrapper(f):
		def callback():
			f(*args)
			t=Timer(seconds,callback)
			t.setDaemon(True)
			t.start()
		callback()
		return f
	return wrapper
def all_events():
	url=_calendar_url
	while url is not None:
		data=load(urlopen(url))['data']
		url=data.get('nextLink',None)
		for item in data['items']:
			yield item

from dateutil.rrule import rrulestr
from pytz import timezone
from dateutil.parser import parse
from datetime import timedelta,datetime
from django.utils.timezone import now
import re
tz_re=re.compile(r';TZID=(.*):(\w*)\r?$',re.MULTILINE)
tz_bogus=re.compile(r'^(?:DTSTART:1970|DTEND|BEGIN|TZ.*|X-.*|END).*\r?\n',re.MULTILINE)
def parse_recurrence(recur):
	def fix_tz(m):
		#print m.group(1),m.group(2)
		return":"+m.group(2)
		return m.group(0)
	return rrulestr(tz_re.sub(fix_tz,tz_bogus.sub('',recur)))
def parse_day(day):
	return datetime.strptime(day,"%Y-%m-%d")
import engsoc_events.models
def upcoming_events(delta=timedelta(weeks=2)):
	cutoff=now()+delta
	cutoff_naive=datetime.now()+delta
	lives=10#XXX use proper logic
	html={e.eid:e.extra_html for e in engsoc_events.models.Event.objects.all()}
	for event in all_events():
		if'when'not in event:
			continue#XXX parse ical recurrences
			print event['recurrence']
		filtered=[]
		class Done(Exception):pass
		for time in event['when']:
			try:
				for _parse in parse,parse_day:
					for _cutoff in cutoff,cutoff_naive:
						try:
							if _parse(time['start'])<_cutoff:
								filtered.append({k:_parse(time[k])for k in time})
							raise Done()
						except TypeError:
							pass
			except Done:
				pass
		event['when']=filtered
		if not filtered:
			lives-=1
			if lives<=0:#XXX wtf
				break
			continue
		event['extra_html']=html.get(event['id'],'')
		yield event
events=None
@every(60)
def update():
	global events
	events=list(upcoming_events())
if __name__=="__main__":
	#print list(parse_recurrence(u'DTSTART;TZID=America/Toronto:20130916T183000\r\nDTEND;TZID=America/Toronto:20130916T191500\r\nRRULE:FREQ=WEEKLY;UNTIL=20131128T233000Z;BYDAY=MO,TH\r\nBEGIN:VTIMEZONE\r\nTZID:America/Toronto\r\nX-LIC-LOCATION:America/Toronto\r\nBEGIN:DAYLIGHT\r\nTZOFFSETFROM:-0500\r\nTZOFFSETTO:-0400\r\nTZNAME:EDT\r\nDTSTART:19700308T020000\r\nRRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU\r\nEND:DAYLIGHT\r\nBEGIN:STANDARD\r\nTZOFFSETFROM:-0400\r\nTZOFFSETTO:-0500\r\nTZNAME:EST\r\nDTSTART:19701101T020000\r\nRRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU\r\nEND:STANDARD\r\nEND:VTIMEZONE\r\n'))
	pass
