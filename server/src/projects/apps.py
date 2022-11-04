from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.projects'

    def ready(self):
        import server.src.projects.signals
