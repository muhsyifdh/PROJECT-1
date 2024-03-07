from modules.libraryitem import LibraryItem

class magazine(LibraryItem):
    def __init__(self, title, upc, subject, volume, issue):
        super().__init__(title, upc, subject)
        self.volume = volume
        self.issue = issue