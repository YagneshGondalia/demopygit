
def person(name, **data):

    print(name)

    for i,j in data.items():
        print(i,j)

person('navin', age=30, city='Mumbai', mob=98765)