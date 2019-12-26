from django.urls import include,path
from .views import managerApp
from .views import proposal

#app_name = 'propuestas'

urlpatterns = [

    path('', managerApp.home, name='home'),

    path('proposals/', include(([
        path('', proposal.index, name='proposals_list')
    ], 'managerApp'), namespace='proposals')),

    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:propuesta_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:propuesta_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:propuesta_id>/modify/', views.modify, name='modify'),
]
