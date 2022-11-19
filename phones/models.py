from django.db import models as m


class Phone(m.Model):
    name = m.CharField(max_length=100)
    price = m.CharField(max_length = 10)
    image = m.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    release_date = m.DateField(auto_now=False, auto_now_add=False)
    lte_exists = m.CharField(max_length=10)
    slug = m.SlugField(max_length=200)

    def __str__(self):
        return self.name


