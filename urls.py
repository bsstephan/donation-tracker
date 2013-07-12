from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tracker.views',
	url(r'^challenges/(?P<event>\w+|)$', 'challengeindex'),
	url(r'^challenge/(?P<id>-?\d+)$', 'challenge'),
	url(r'^choices/(?P<event>\w+|)$', 'choiceindex'),
	url(r'^choice/(?P<id>-?\d+)$', 'choice'),
	url(r'^choiceoption/(?P<id>-?\d+)$', 'choiceoption'),
	url(r'^donors/(?P<event>\w+|)$', 'donorindex'),
	url(r'^donor/(?P<id>-?\d+)/(?P<event>\w+|)$', 'donor'),
	url(r'^donations/(?P<event>\w+|)$', 'donationindex'),
	url(r'^donation/(?P<id>-?\d+)$', 'donation'),
	url(r'^runs/(?P<event>\w+|)$', 'runindex'),
	url(r'^run/(?P<id>-?\d+)$', 'run'),
	url(r'^prizes/(?P<event>\w+|)$', 'prizeindex'),
	url(r'^prize/(?P<id>-?\d+)$', 'prize'),
	url(r'^prize_donors/(?P<id>-?\d+)$', 'prize_donors'),
	url(r'^draw_prize/(?P<id>-?\d+)$', 'draw_prize'),
	url(r'^merge_schedule/(?P<id>-?\d+)$', 'merge_schedule'),
	url(r'^events/$', 'eventlist'),
	url(r'^setusername/$', 'setusername'),
	url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^search/$', 'search'),
	url(r'^add/$', 'add'),
	url(r'^edit/$', 'edit'),
	url(r'^delete/$', 'delete'),
	url(r'^index/(?P<event>\w+|)$', 'index'),
	url(r'^donate/(?P<event>\w+)$', 'donate', name='donate'),
	# unfortunately, using the 'word' variant here clashes with the admin site (not to mention any unparameterized urls), so I guess its going to have to be this way for now.  I guess that ideally, one would only use the 'index' url, and redirect to it as neccessary).
	url(r'^(?P<event>\d+|)$', 'index'),
	url(r'^paypal_return/$', 'paypal_return', name='paypal_return'),
	url(r'^paypal_cancel/$', 'paypal_cancel', name='paypal_cancel'),
	url(r'^ipn/$', 'ipn', name='ipn'),
)

