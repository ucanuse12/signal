# Import necessary modules
from django.test import TestCase
from app.models import User, Subscriber


## =================
## Unit Models Test
## =================
class ModelsTestCase(TestCase):
    
    def setUp(self):
        # Create a User instance
        self.user = User.objects.create(name="John Doe", email="john@example.com")
        # Create a Subscriber instance associated with the User
        self.subscriber = Subscriber.objects.create(subscribe=True, user=self.user)
    
    def test_user_model(self):
        # Retrieve the User instance
        user = User.objects.get(name="John Doe")
        # Check if the user exists
        self.assertIsNotNone(user)
        
        # Print user information
        print("User Name:", user.name)
        print("User Email:", user.email)
        
    def test_subscriber_model(self):
        # Retrieve the Subscriber instance
        subscriber = Subscriber.objects.get(user__name="John Doe")
        
        # Check if the subscriber exists
        self.assertIsNotNone(subscriber)
        
        # Print subscriber information
        print("User:", subscriber.user.name)
        print("Subscribed:", subscriber.subscribe)


## =======================
## Integrated Models Test
## =======================
class IntegratedModelsTestCase(TestCase):
    
    def test_user_subscriber_interaction(self):
        # Create a User instance
        user = User.objects.create(name="Alice", email="alice@example.com")
        
        # Create a Subscriber instance associated with the User
        subscriber = Subscriber.objects.create(subscribe=True, user=user)
        
        # Retrieve the Subscriber instance and check if it's associated with the correct User
        retrieved_subscriber = Subscriber.objects.get(user=user)
        self.assertEqual(retrieved_subscriber.user, user)
        
        # Check if the subscriber's subscribe field is True
        self.assertTrue(retrieved_subscriber.subscribe)
        
        # Check if changing the subscribe field of Subscriber affects the User model
        retrieved_subscriber.subscribe = False
        retrieved_subscriber.save()
        updated_user = User.objects.get(pk=user.pk)
        self.assertFalse(updated_user.subscriber.subscribe)


# Run the tests
if __name__ == "__main__":
    unittest.main()