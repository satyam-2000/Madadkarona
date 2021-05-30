from django.conf.urls import url
from corona import views

# SET THE NAMESPACE!
app_name = 'corona'

urlpatterns=[
   
    url('delhi/',views.delhi,name='delhi'),
    url('kanpur/',views.kanpur,name='kanpur'),
    url('donate',views.donate,name='donate'),
    url('lbeds/',views.lbeds,name="lbeds"),
    url('dbeds/',views.dbeds,name="dbeds"),
    url('kbeds/',views.kbeds,name="kbeds"),
   
]