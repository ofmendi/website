import os
import json
import pprint
import meetup.api
from django.views.generic.base import TemplateView
class ActivitiesView(TemplateView):
    template_name = "activities/activities_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = self.get_all_activities()
        return context

    def get_past_activities(self):
        client = meetup.api.Client(os.environ.get('MEETUP_API_KEY'))
        past_events = client.GetEvents({'group_urlname': 'python-istanbul', 'status': 'past'})
        return past_events.__dict__