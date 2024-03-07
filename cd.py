from modules.libraryitem import LibraryItem

class cd(LibraryItem):
    def __init__(self, title, upc, subject, artist):
        super().__init__(title, upc, subject)
        self.artist = artist