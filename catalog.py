from modules.book import Book
from modules.cd import cd
from modules.dvd import dvd
from modules.magazine import magazine

class Catalog():
    def __init__(self, catalog):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog_item in self.catalog:
            for item in catalog_item:
                if input_search.lower() in item.title.lower():
                    if isinstance(item, magazine):
                        list_result.append(f'Title: {item.title}, volume: {item.volume}, Type Catalog: Magazine')
                    elif isinstance(item, Book):
                        list_result.append(f'Title: {item.title}, DDS Number: {item.dds_number}, Type Catalog: Book')
                    elif isinstance(item, dvd):
                        list_result.append(f'Title: {item.title}, genre: {item.genre}, Type Catalog: DVD')
                    elif isinstance(item, cd):
                        list_result.append(f'Title: {item.title}, artist: {item.artist}, Type Catalog: CD')
        return list_result
