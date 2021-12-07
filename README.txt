FAZER SEMPRE QUE CRIAR UM NOVO PROJETO

    mudar TIME_ZONE = 'UTC' para TIME_ZONE = 'America/Sao_Paulo' em
        settings.py, para fazer com que o horario do projeto esteja no fuso do brasil

    mudar LANGUAGE_CODE = 'en-us' para LANGUAGE_CODE = 'pt-br' em settings.py
        para os decimais do banco de dados serem escritos com ',' ao invés de '.'

    adicionar os.path.join(BASE_DIR, 'templates') em DIR de TEMPLATES em settings.py
        para fazer com que a pasta templates na raiz do diretorio seja lida
    
    adicionar a variavel STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
        em settings.py, para fazer com que a pasta de imagens e arquivos seja lida 
        
    cmd -> py manage.py createsuperuser, para criar um usuario admin