from django.core.management import BaseCommand

from mainapp.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        category_list = [
            {'category_name': 'Бакалея', 'description': 'Макароны, крупы, консервация, сахар, соль, специи, соусы, масло'},
            {'category_name': 'Молочные продукты', 'description': 'Молоко, Сыр, Йогурты, Творог, Сметана, Кефир, Прочие молочные продукты'},
            {'category_name': 'Кондитерские изделия', 'description': 'Шоколад, Печенье, Зефир и мармелад, Варенье и мед, Пряники и вафли, Восточные сладости'},
            {'category_name': 'Вода, Соки, Напитки', 'description': 'Вода, Газировка, Соки, Энергетики, Морсы, Чай'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        # print(category_for_create)

        Category.objects.bulk_create(category_for_create)




