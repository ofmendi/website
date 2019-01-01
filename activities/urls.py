from django.conf.urls import url

from .views import ActivitiesView


app_name = 'activities'


urlpatterns = [
    url('', ActivitiesView.as_view(), name='index'),
]
