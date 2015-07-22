DATABASES = {
   'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'fixmystreet',
        'USER': 'postgis',
        'PASSWORD': 'postgis',
        'HOST': 'postgis',
        'PORT': 5432,
        # 'OPTIONS': {
        #     'autocommit': True
        # }
   }
}

EMAIL_HOST = "relay.irisnet.be"
EMAIL_ADMIN = "bsu@imio.be"
ADMIN_EMAIL = "bsu@imio.be"

