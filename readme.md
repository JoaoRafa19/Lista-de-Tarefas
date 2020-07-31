<html>

<h1>Lista de Tarefas</h1>

<div>
<h2>Resumo</h2>
<p>Um pequeno modelo de uma lista de tarefas, onde você pode criar, modificar e remover tarefas marcadas como urgente ou não.</p>


</p>
<h3>Objetivos</h3>

---
<ul>
    <li>Iniciar um projeto WEB em Django</li>
    <li>Criar um CRUD de tarefas
    <li>Criar um modelo de Tabela no Django</li>
    <li>Configurar o Banco de dados</li>
    <li>Criar as URL's do Projeto</li>
    <li>Criar as views</li>
    <li>Criar o formulário para adicionar tarefas
    <li>Criar os Templates jinja</li>
    <li>Trabalhar com os dados do banco</li>
</ul>

---
<h2>Settings</h2>

<p>Adiciona o app 'tasks' ao projeto</p>

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',

]
```

<p>Configura o banco de dados Sqlite3 no projeto</p>

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

<p> Adiciona a pasta de arquivos estáticos ao projeto</p>

```
STATIC_URL = '/static/'
```
---

<h2>Models</h2>
<p>Há apenas uma unica classe no Banco de dados para salvar as tarefas</p>

```
class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    SIM = 'SIM'
    NAO = 'NAO'
    urgencia_escolhas = [
        (SIM, 'SIM'),
        (NAO, 'NAO'),
    ]
    urgencia = models.CharField(
        max_length=3,
        choices=urgencia_escolhas,
        default=NAO,
    )


    class Meta:
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.nome

```
---

<h2>Forms</h2>

cria um modelo de formulário para a renderização no template
como modelo para a tabela de Tarefas
````
from django.forms import ModelForm
from .models import Tarefa

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome','urgencia']
    
````
---

<h2>Admin</h2>

<p>Registra o modelo de banco de dados

```
from .models import Tarefa
admin.site.register(Tarefa)

```

---
<h2>URLs</h2>

<p>Conecta as url's nas respectivas funções nas views
<ul>
    <li><h5>Index</h5>
    <p>liga a view que retorna a pagina principal da aplicação e que retorna os elementos da lista
    <li><h5>Add</h5>
    <p>retorna a template de adicionar tarefa
    <li><h5>Update</h5>
    <p>retorna a template de adicionar mas com um objeto (Tarefa) como parâmetro instanciado no formulário do template 
    <li><h5>Delete</h5>
    <p>passa como parametro um objeto e a chave primária dele e remove o registro do banco de dados

</ul>

```

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add/', adicionar_tarefa, name='add'),
    path('update/<int:id>/', update_tarefa, name='update'),
    path('delete/<int:id>/', delete_tarefa, name='delete'),
]


```
---

<h2>Views</h2>

funçoes que são chamadas a parir de urls

imports
```
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarefa
from .forms import TarefaForm


```

<h6>index</h6>
retorna a pagina principal com os objetos da tabela Tarefas

```
def index(request):
    data = {}
    data['tarefas'] = Tarefa.objects.all()
    return render(request, 'tasks/index.html', data)


```


<h6>adicionar tarefa</h6>

```
def adicionar_tarefa(request):
    data = { }
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    data['form'] = form
    return render(request, 'tasks/form.html', data)

```

update tarefa

```
def update_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'tasks/form.html', {'form':form, 'tarefa':tarefa})
```
deleta tarefa
```
def delete_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('index')

</div>
</html>
```
