
from django.test import TestCase
from .models import Route
  # Импортируйте вашу модель

class YourModelTest(TestCase):
    def test_create_your_model(self):
        obj = Route.objects.create(field1='value1', field2='value2')
        self.assertEqual(obj.field1, 'value1')
        self.assertEqual(obj.field2, 'value2')

# routes/tests.py
from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))  # Замените 'home' на ваш URL-имя
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Привет, мир!")

# routes/tests.py
from django.test import TestCase
from django.template import Template, Context

class TemplateTest(TestCase):
    def test_template_renders_correctly(self):
        template = Template("Привет, мир! Это мой первый шаблон Django.")
        context = Context()
        rendered = template.render(context)
        self.assertIn("Привет, мир!", rendered)
