from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from threading import Thread

## Signals
## 1. pre_save
## 2. post_save
## 3. pre_delete
## 4. post_delete
## 5. m2m_changed
## 6. pre_init
## 7. post_init
## 8. pre_migrate
## 9. post_migrate
## 10. class_prepared
## 11. request_started
## 12. request_finished
## 13. got_request_exception
## 14. setting_changed
## 15. setting_changed
## 16. template_rendered
## 17. database_connection_created
## 18. connection_created
## 19. connection_terminated
## 20. sql_flush_started
## 21. sql_flush_finished
## 22. sql_sequence_reset
## 23. pre_commit
## 24. post_commit
## 25. pre_rollback
## 26. post_rollback

## User
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"


## Subscriber
class Subscriber(models.Model):
    subscribe = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} | {self.subscribe}"
    
## Mail Function
def notify_user_by_mail(instance):
    send_mail(
                "Subject here",
                f'{instance.user} has subscribed the channel',
                "ucanuse54@gmail.com",
                ["emhaxim@gmail.com"],
            )


## User Subscribe and Email Signal
@receiver(post_save, sender=Subscriber)
def subscriber_notify_signal(sender, instance, created, *args, **kwargs):
    pass
    # if instance.subscribe:
    #     print(f'{instance.user} has subscribed the channel')
    #     x = Thread(target=notify_user_by_mail, args=(instance,))
    #     x.start()
        



class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name + " - " + self.phone 


def pre_save_contact(sender, instance, **kwargs):
    print("pre save signal Worked")


def post_save_contact(sender, instance, **kwargs):
    print("post save signal Worked")



pre_save.connect(pre_save_contact, sender=Contact)
post_save.connect(post_save_contact, sender=Contact)

## Similar task with decorator
@receiver(post_save, sender=Contact)
def user_created_handler(sender, instance, created , *args, **kwargs):
    if created:
        print('Send mail to user!')




        

    