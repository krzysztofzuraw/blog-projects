from haystack import indexes

from .models import Person


class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    gender = indexes.CharField(model_attr='gender')
    email = indexes.CharField(model_attr='email')
    ip_address = indexes.CharField(model_attr='ip_address')

    def get_model(self):
        return Person
