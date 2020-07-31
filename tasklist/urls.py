from django.contrib import admin
from django.urls import path
from tasks.views import index, adicionar_tarefa, update_tarefa, delete_tarefa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add/', adicionar_tarefa, name='add'),
    path('update/<int:id>/', update_tarefa, name='update'),
    path('delete/<int:id>/', delete_tarefa, name='delete'),
]
