import uuid

import requests
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import Model, URLField, SlugField, CharField, TimeField, UUIDField
from django.utils.text import slugify
from django_jsonform.models.fields import JSONField


class User(AbstractUser):

    def save(self, *args, **kwargs):
        if 'botir' in self.username.lower():
            raise ValidationError('Username atmen!')

        super().save(*args, **kwargs)


class Product(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, blank=True, editable=False)
    times = TimeField(default=0)
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # class Meta:
    #     abstract = True

    def save(self, *args, init_id=None, **kwargs):
        self.slug = slugify(self.name)
        if not init_id:
            self.save(*args, init_id=True, **kwargs)
            self.slug += f"-{self.uuid}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    SCHEMA = {
        'type': 'dict',
        'keys': {
            'size': {
                'type': 'number',
                'default': 50,  # default value for age
            },
            'color': {
                'type': 'string',
            }
        },
    }
    data = JSONField(schema=SCHEMA)

    url = URLField(null=True, blank=True)

    def clean(self):
        super().clean()
        if self.url:
            try:
                response = requests.head(self.url, timeout=5)
                if response.status_code >= 400:
                    raise ValidationError(f"The URL '{self.url}' is not reachable.")
            except requests.RequestException:
                raise ValidationError(f"The URL '{self.url}' is not reachable.")

    # date = DateTimeField(default=timezone.now)
    # duration = DurationField(default=0)

    # event_date = DateField(default="2022-01-01")
    # number = BigAutoField(primary_key=True)  # SERIAL
    # image = BinaryField(null=True, blank=True)
    # quantity = AutoField() # SERIAL
