# coding=utf-8
import os
import json

from .models import Person

DATA_FILE = os.path.join(
    os.path.dirname(
        os.path.dirname(
        os.path.dirname(__file__))),
        'MOCK_DATA.json'
)


def run(verbose=True):
    with open(DATA_FILE) as data_file:
        data = json.load(data_file)
        for record in data:
            Person.objects.create(
                first_name=record['first_name'],
                last_name=record['last_name'],
                gender=record['gender'],
                email=record['email'],
                ip_address=record['ip_address'])
            print(record)
