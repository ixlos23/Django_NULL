import uuid

from django.contrib.auth.models import AbstractUser
from django.core import exceptions
from django.core.exceptions import ValidationError
from django.db.models import CharField, Model, UUIDField, SlugField, BigAutoField, ForeignKey, CASCADE, \
    PositiveSmallIntegerField, DateField, PositiveIntegerField, DateTimeField
from django.utils import timezone
from django.utils.text import slugify


class User(AbstractUser):
    created_at =DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if 'botir' in self.username.lower():
            raise ValidationError('Username atmen!')

        super().save(*args, **kwargs)


class Category(Model):
    name = CharField(max_length=255)
    id = BigAutoField(primary_key=True)
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)  # unique=True qo'shildi
    slug = SlugField(unique=True, blank=True, editable=False)

    def save(self, *args, init_id=None, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


def error_handler(value):
    minute = timezone.now().minute
    if minute % 2 != 0:
        raise exceptions.ValidationError('xabar', code='ixlos', params={'value': value})
    return value


class Product(Model):
    name = CharField(max_length=255, validators=[error_handler], error_messages={"ixlos": '%(value)s vatq juft emas6'})
    category = ForeignKey('apps.Category', CASCADE, to_field='uuid')
    price = PositiveIntegerField(default=0)
    description = CharField(max_length=255, default='ab', null=True, blank=True)
    user = ForeignKey('apps.User', on_delete=CASCADE)


class Example(Model):
    name = CharField(max_length=255)
    age = PositiveSmallIntegerField(null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
# from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# from django.db.models import Model, CharField, ImageField, ForeignKey, CASCADE, PositiveIntegerField
#
#
# class Product(Model):
#     name = CharField(max_length=255)
#
#
# class A(Model):
#     name = CharField(max_length=255)
#     images = GenericRelation('apps.Image')
#
#
# class B(Model):
#     name = CharField(max_length=255)
#     images = GenericRelation('apps.Image')
#
#
# class C(Model):
#     name = CharField(max_length=255)
#     images = GenericRelation('apps.Image')
#
#
# class D(Model):
#     name = CharField(max_length=255)
#     images = GenericRelation('apps.Image')
#
#     class Meta:
#         abstract = True
#
#
# class Image(Model):
#     image = ImageField()
#     content_type = ForeignKey('contenttypes.ContentType', CASCADE, limit_choices_to={'model__in': ['a', 'b', 'c', 'd']})
#     object_id = PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')


#
# class AImage(Model):
#     a_image = ImageField(null=True, blank=True)
#     b_image = ImageField(null=True, blank=True)
#     c_image = ImageField(null=True, blank=True)
#     d_image = ImageField(null=True, blank=True)


# class AImage(Model):
#     image = ImageField()
#
#
# class BImage(Model):
#     image = ImageField()
#
#
# class CImage(Model):
#     image = ImageField()
#
#
# class DImage(Model):
#     image = ImageField()


# GenericForeignKey

# class User(AbstractUser):
#     pass

#
# class A(Model):
#     name = CharField(max_length=100)
#
#
# class B(Model):
#     age = CharField(max_length=100)
#     a = ManyToManyField('apps.A', through='apps.AB', blank=True)
#
#
# class AB(Model):
#     # YEAR_IN_SCHOOL_CHOICES = [
#     #     ("junior", "Junior"),
#     #     ("middle", "Middle"),
#     #     ("senior", "Senior")
#     # ]
#     # status = CharField(max_length=100, choices=YEAR_IN_SCHOOL_CHOICES, default=YEAR_IN_SCHOOL_CHOICES[0][0])
#
#     class YearInSchoolChoices(TextChoices):
#         JUNIOR = 'junior', 'Junior'
#         MIDDLE = 'middle', 'Middle'
#         SENIOR = 'senior', 'Senior'
#         __empty__ = 'Aniqlanmagan'
#
#     status2 = CharField(max_length=100, choices=YearInSchoolChoices.choices, default=YearInSchoolChoices.JUNIOR)
#
#     MEDIA_CHOICES = {
#         "Audio": {
#             "vinyl": "Vinyl",
#             "cd": "CD",
#         },
#         "Video": {
#             "vhs": "VHS Tape",
#             "dvd": "DVD",
#         },
#         "unknown": "Unknown",
#     }
#     status = CharField(max_length=100, choices=MEDIA_CHOICES, null=True, blank=True)
#
#     a = ForeignKey('apps.A', CASCADE)
#     b = ForeignKey('apps.B', CASCADE)
# def save(self, *args, **kwargs):
#     self.times = timezone.localtime(timezone.now())
#     super().save(*args, **kwargs)

# class Meta:
#     abstract = True

# def save(self, *args, init_id=None, **kwargs):
#     self.slug = slugify(self.name)
#     if not init_id:
#         self.save(*args, init_id=True, **kwargs)
#         self.slug += f"-{self.uuid}"
#     super().save(*args, **kwargs)
#
# def __str__(self):
#     return self.name
#
# SCHEMA = {
#     'type': 'dict',
#     'keys': {
#         'size': {
#             'type': 'number',
#             'default': 50,  # default value for age
#         },
#         'color': {
#             'type': 'string',
#         }
#     },
# }
# data = JSONField(schema=SCHEMA)
#
# url = URLField(null=True, blank=True)
#
# def clean(self):
#     super().clean()
#     if self.url:
#         try:
#             response = requests.head(self.url, timeout=5)
#             if response.status_code >= 400:
#                 raise ValidationError(f"The URL '{self.url}' is not reachable.")
#         except requests.RequestException:
#             raise ValidationError(f"The URL '{self.url}' is not reachable.")

# date = DateTimeField(default=timezone.now)
# duration = DurationField(default=0)

# event_date = DateField(default="2022-01-01")
# number = BigAutoField(primary_key=True)  # SERIAL
# image = BinaryField(null=True, blank=True)
# quantity = AutoField() # SERIAL

#
# class Product(Model):
#     name = CharField(max_length=255, db_column='name123')
#     slug = SlugField(unique=False, blank=True, editable=False)
#     times = DateTimeField(default=timezone.now)
#     uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     category = ForeignKey("apps.Category", related_name='products', on_delete=CASCADE)
