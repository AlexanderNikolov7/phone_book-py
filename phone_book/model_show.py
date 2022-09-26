

         # отобразит все строки в файле

def show_all():
    data = open('file.txt', 'r')
    for line in data:
        print(line)
    data.close()

# show_all()    