'''
Created on 7 de jun. de 2022

@author: daline
'''
from faker import Faker

fake = Faker('pt_BR')

print (fake.email()) 
print(fake.country()) 
print(fake.name()) 
print(fake.text()) 
print(fake.latitude(), fake.longitude()) 
print(fake.url()) 
print(fake.sentence()) 