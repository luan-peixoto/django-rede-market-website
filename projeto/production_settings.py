import environ

from projeto.settings import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)
# cria uma variável de ambiente para debug, como padrão 'False' caso nada seja definido

SECRET_KEY = env('SECRET_KEY')
# cria uma variável de ambiente para esconder a secret key do projeto, em produção ela não
# pode ficar nos do projeto

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
# cria uma variável de ambiente para os hosts permitidos, no caso é preciso colocar 
# o url do site nela

DATABASES = {
    'default': env.db(),
}
# esse env.db() pega todos os dados do bd postgre criado no heroku, é bem prático
