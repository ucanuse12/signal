from django.test import TestCase, Client
from django.urls import reverse
from app.models import User, Subscriber

class HomeViewTest(TestCase):
    def test_home_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the Home.")

class SubscriberTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(name="Hashim", email="Hashim@example.com")
        self.user2 = User.objects.create(name="Raza", email="Raza@example.com")
        Subscriber.objects.create(user=self.user1, subscribe=True)
        Subscriber.objects.create(user=self.user2, subscribe=False)

    def test_subscriber_function(self):
        client = Client()
        response = client.get(reverse('subscriber'))
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"data": [
                {"user": {"name": "Hashim", "email": "Hashim@example.com"}, "subscribe": True},
                {"user": {"name": "Raza", "email": "Raza@example.com"}, "subscribe": False}
            ]}
        )
