import os
import sys
class Person():
    def __init__(self,firstname,lastname,street,city,state,postcode):
        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.city = city
        self.state = state
        self.postcode = postcode

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def getStreet(self):
        return self.street

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getPostcode(self):
        return self.postcode

    def __str__(self):
        return 'Firstname: {}\nLastname: {}\nStreet: {}\nCity: {}\nState: {}\nPostcode: {}'.format(self.firstname,self.lastname,self.street,self.city, self.state,self.postcode)

firstname = input('Enter your firstname: ')
lastname = input('Enter your lastname: ')
street = input('Enter your street: ')
city = input('Enter your city: ')
state = input('Enter your state: ')
postcode = input('Enter your postcode: ')

person = Person(firstname,lastname,street,city,state,postcode)
print(person)

fileObject = open('person.txt', 'w+')
personData = str(person)
f = open('./person.txt'.format(fileObject), 'w+')
f.write('{}'.format(personData))
f.close()
        

    
    
