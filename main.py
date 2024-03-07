import json
from modules.book import Book
from modules.cd import cd
from modules.dvd import dvd
from modules.magazine import magazine
from modules.catalog import Catalog

f = open('file/catalog.json')
data_json = json.load(f)

books = []
magazines = []
dvds = []
cds = []

for item in data_json:
    if item['source'] == 'book':
        books.append(
            Book(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                issbn=item['issbn'],
                authors=item['authors'],
                dds_number=item['dds_number']
            )
        )
    elif item['source'] == 'magazine':
        magazines.append(
            magazine(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                volume=item['volume'],
                issue=item['issue']
            )
        )
    elif item['source'] == 'dvd':
        dvds.append(
            dvd(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                actors=item['actors'],
                director=item['director'],
                genre=item['genre']
            )
        )
    elif item['source'] == 'cd':
        cds.append(
            cd(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                artist=item['artist']
            )
        )

catalog_all = [books, magazines, dvds, cds]
input_search = 'test'
results = Catalog(catalog_all).search(input_search)

for index, result in enumerate(results):
    print(f'result ke-{index+1} | {result}')