# `engsoc_events`
for EngSoc Hack Day 2013
## setup
1. install django and run `./manage.py syncdb` if you delete `events.db`
2. add a panel pointing to /events
3. generate a new django secret key

## urls
- all panels: `/`
- events (scrolling): `/events`
- add HTML to events: `/modify`
- other admin: `/admin`
- RSS: [`engsoc_events._calendar_url.replace('alt=jsonc&','')`](http://www.google.com/calendar/feeds/um08n4cml235750sucn1vmgqd0%40group.calendar.google.com/public/full?orderby=starttime&max-results=25&sortorder=ascending&futureevents=true&ctz=America/Toronto&singleevents=true)

## issues
(in alphabetical order, to make up for not using the issue tracker)

- admin interface has crappy friendly names (i.e. "updated" message is "Event with this Eid already exists.")
- admin does not use syntax highlighting or show previews
- delays
- does not create a default panel
- does not display multiple panels (not an inherent limitation)
- does not publish to LED screens (not an inherent limitation, can be done in the polling loop)
- event overwrite behaviour hard-coded
- import ignores timezones
- import ignores recurrence rules
- import uses hard-coded 25-item paging
- jquery scrolling jumps to the top of the page (perhaps use CSS animations if EngSoc LCDs support them?)
- the SASS/CSS sucks (although it correctly handles mobile screens)

## default `events.db`
user: `root`

email: `root@example.com`

password: `root@example.com`

## original objective: (copied from [Facebook](https://www.facebook.com/events/535585283180062/537747149630542))
Platform for displaying media on LCD {

This is a front end where you enter a description for an event or service. You create an event. Generates RSS feed of upcoming events and puts it in the EngSoc calendar automatically. Starting two weeks before the event, it will push ads for the event (which you can upload in this service as well) onto the EngSoc LCDs as well as the LED display automagically. You can subscribe to this RSS feed so you get events updates

}
(LEDs were unavailable and the EngSoc calendar is managed separately)
