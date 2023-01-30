from django.test import TestCase

from .models import *

class ProjectTestCase(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name="Test Project",
            description="This is a test project",
            status="Active",
            start_date="2019-01-01",
            end_date="2019-12-31",
            budget=1000,
            client="Test Client",
            manager="Test Manager",
            team="Test Team",
        )

    def test_project_creation(self):
        self.assertTrue(isinstance(self.project, Project))
        self.assertEqual(self.project.__str__(), self.project.name)
