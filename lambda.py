# creating lambda functions
def myfunc(n):
    return lambda a:a*n
mydoubler = myfunc(3)
print(mydoubler(11))
# another example of lambda functions
people = [{'name':'taddele','departement':'computer'},
          {'name':'temesgen','departement':'health'},
          {'name':'zekarias','departement':'finance'}]
"""
def f(person):
    return person['departement']
"""
people.sort(key=lambda person:person['departement'])
print(people)
