import re

class File:
    """Class working with file"""
    def __init__(self, name, mode):
        self.name = str(name) + '.txt'
        self.mode = str(mode)

    def Open_file(self, name, mode):
        self.name = str(name) + '.txt'
        self.mode = str(mode)
        f1 = open(self.name, self.mode)
        x = f1.read()
        print(x)
        f1.close()


    def Open_file_and_search_date(self, name, mode):
        self.name = str(name) + '.txt'
        self.mode = str(mode)
        f1 = open(self.name, self.mode)
        x = f1.read()
        f1.close()
        date = re.findall('\d{2}.\d{2}.\d{4}', x)
        print(date)
