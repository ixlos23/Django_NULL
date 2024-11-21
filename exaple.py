import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

django.setup()

from apps.models import Product, User

# for i in Category.objects.filter(name__istartswith="lin"):
#     print(i)

# for i in Category.objects.exclude(name__endswith='ux'):
#     print(i)

# q = Product.objects.annotate(Count("name"))
# print(q)


# blogs = Category.objects.alias(entries=Count("name")).filter(name__istartswith="lin")
# print(blogs)

# p = Category.objects.order_by('name').filter(name__istartswith='l')
# print(p)

# for i in Example.objects.order_by('-age'):
#     print(i.age)

# print(Example.objects.distinct('name'))
#
# product = Product.objects.filter(name__icontains='tex').annotate(model_name=Value('Product', CharField(
# ))).values_list("name", "model_name") category = Category.objects.filter(name__icontains='tex').annotate(
# model_name=Value('Category', CharField())).values_list("name", "model_name")

# find = product.union(category)
#
# for name, model_name in find:
#     print(f"{name} ({model_name})")
# a = Example.objects.extra(select={"date_of_birth": "date_of_birth > '2024-11-13'"})
# print(a)
# print(Example.objects.all())


#
# example_id = int(input('Enter an example id: '))
#
# example = Example.objects.raw("select * from apps_example where id = %s", (example_id,))
# for i in example:
#     if i.name == 'xurshid':
#         print(i.name + ' developer')
#     else:
#         print(i.name)


# get = Example.objects.get(pk=2)
# print(get.name)

# create = Example.objects.create(name='example', age='19')

# obj, created = Example.objects.get_or_create(
#     name="John",
#     age="65",
#     defaults={"date_of_birth": date(1940, 10, 9)},
# )
#
#
# print(obj)
# obj, created = Example.objects.update_or_create(
#     name="John",
#     age="88",
#     defaults={"first_name": "Bob"},
#     create_defaults={"name": "age", "birthday": date(1940, 10, 9)},
# )


# Product.objects.filter(Q(category__name='meva') | Q(name='banan')).update(price='25_000')


# Product.objects.filter(Q(category__name='meva')).update(price=F('price') * 2)


# print(Example.objects.in_bulk(([1, 2])))

# print(Example.objects.in_bulk(id_list=None, field_name='pk'))

# for i in Product.objects.all().iterator():
#     print(i.name)

# eng kichik summali product narxini barcha productlarga qo'shing
# from django.db.models import F, Min
#
# min_price = Product.objects.aggregate(min_price=Min('price'))['min_price']
#
# if min_price is not None:
#     Product.objects.update(price=F('price') + min_price)
#
# for i in Product.objects.iterator():
#     print(i.id, i.name, i.price)

# from django.db.models import F
#
# results = Product.objects.values(c_name=F('category__name'))
# for i in results:
#     print(i)

# from django.db.models import Sum, Count
#
# results = Product.objects.values('category__id', 'name').annotate(total_price=Sum('price'),
#                                                                   product_soni=Count('name'))
#
# for result in results:
#     print(result)

# from django.db import transaction
#
# latest_user = User.objects.latest('created_at')
#
# with transaction.atomic():
#     products = Product.objects.filter(user=latest_user)
#     for product in products:
#         if product.name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
#             product.price += 1000
#             product.save()


# users_in_2020 = User.objects.filter(date_joined__year=2020)
#
# for user in users_in_2020:
#     print(user.username, user.date_joined)

#
# from django.db.models import Q
#
# products = Product.objects.filter(
#     Q(price__gte=2000, price__lte=3500) &
#     Q(description__isnull=False) &
#     Q(name__icontains='a')
# )
#
# for product in products:
#     print(f"name: {product.name},      description: {product.description}")
#
