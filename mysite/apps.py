from django.apps import AppConfig

#在settings.py裡INSTALLED_APPS=[最後一行'mysite.apps.MysiteConfig']的由來
class MysiteConfig(AppConfig):
    name = 'mysite'
