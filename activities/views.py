import os
import meetup.api
from django.views.generic.base import TemplateView
class ActivitiesView(TemplateView):
    template_name = "activities/activities_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_events'] = self.get_all_activities()
        return context

    def get_all_activities(self):
        client = meetup.api.Client(os.environ.get('MEETUP_API_KEY'))
        all_events = client.GetEvents(
            {'group_urlname': 'python-istanbul', 'status': ['upcoming', 'past']})
        return all_events.__dict__
