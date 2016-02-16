from settings import PROJECT_ROOT

DEBUG = True

# TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'message_board',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'Python99',
        'PORT': ''
    }
}