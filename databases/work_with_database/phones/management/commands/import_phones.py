import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        full = [phone for phone in phones]
        return full

    def add_db(self):
        for i in Command().handle():
            Phone.objects.create(
                name = i['name'],
                price = i['price'],
                image = i['image'],
                release_date = i['release_date'],
                lte_exists = i['lte_exists'],
                slug = '',
            )

print(Command().handle())