import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django

django.setup()

## FAKE POP SCRIPT
from first_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fake = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games"]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populateTopics(N=5):
    for entry in range(N):
        # get topic for the entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = fake.url()
        fake_name = fake.company()
        fake_date = fake.date()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


def populateUsers(N=5):
    for entry in range(N):
        try:
            fake_name, fake_surname = fake.name().split(sep=" ")
            fake_email = fake.email()
            user = User.objects.get_or_create(first_name=fake_name, last_name=fake_surname, email=fake_email)[0]
        except:
            print(fake_surname + " " + fake_name)


if __name__ == '__main__':
    print("populating script!")
    # populateTopics(20)
    populateUsers(15)
    print("done")
