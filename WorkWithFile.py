import re

def Open_file(a):
    f1 = open(a, 'r')
    x = f1.read()
    print(x)
    f1.close()
def Open_file_and_search_date(a):
    f1 = open(a, 'r')
    x = f1.read()
    f1.close()
    date = re.findall('\d{2}.\d{2}.\d{4}', x)
    print(date)
