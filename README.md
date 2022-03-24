# Django N+1
Demonstração do problema N+1 em um projeto Django

## Passos
* Clonar repositório:
```
git clone git@github.com:victoraugustosoares/django-n-1.git
```

* Entrar em diretório:
```
cd django-n-1
```

* Abrir projeto na IDE

* Copiar variáveis de ambiente:
```
cp contrib/env-sample .env
```

* Criar ambiente virtual e ativá-lo:
```
python -m venv .venv
source .venv/bin/activate
```

* Instalar dependências:
```
pip install -r requirements-dev.txt
```

* Verificar se projeto está executando:
```
python manage.py runserver
```

* Para aplicar migrações:
```
python manage.py migrate
```