from book.models import Country

import csv
with open('temp/countries.csv', mode='r', encoding='utf-8') as f:
    dict = csv.DictReader(f)
    for item in dict:
        country = Country.objects.create(name=item['Name'], code=item['Code'])

        print(country)
