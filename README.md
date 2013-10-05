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
- jquery scrolling jumps to the top of the page (perhaps use CSS animations if EngSoc LCDs support it?)
- the SASS/CSS sucks (although it correctly handles mobile screens)

## default `events.db`
user: `root`

email: `root@example.com`

password: `root@example.com`
