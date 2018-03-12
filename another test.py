# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:23:36 2018

@author: e
"""
MAXDAYS = 73000
LOG = []
PEOPLE = []
DAY = 0
deaths = []
import random
malnames = ["Joshua", "Carl", "Peter", "Alexander", "Scott", "Henry", "Aaron",#7
            "Isaac", "Liam", "Mark", "Michael", "Elijah", "Achilles", #13
            "Orion","Magnus", "Constantine", "Ares", "Theodore", "Jason",#19
            "Romulus"]
femnames = ["Gloria", "Samantha", "Alexandra", "Helena", "Mary", "Katherine",#6
            "Sophia", "Elizabeth", "Marian", "Ariel", "Willow", "Theodora", #12
            "Sarah", "Suzanne", "Olivia", "Freya", "Fiona", "Emma", "Gertrude",
            "Cameron"] 

lasnames = ["Burke", "Winnet", "Orange", "Auriga"]

class person:
    def __init__(self, gender = random.choice(["male", "female"]),
                 r = None):
        self.gender = gender
        if self.gender == "male":    
            self.firstname = random.choice(malnames)
        else:
            self.firstname = random.choice(femnames)
        if r != None:
            r.addchild(self)
            self.lastname = r.lastname
        else:
            self.lastname = random.choice(lasnames)
        self.maidenname = ""
        self.marriage = None
        LOG.append(self.firstname + " "+self.lastname + " was born in the "+ 
                   "year of " + str(DAY//365))
        PEOPLE.append(self)
        self.age = 0
        self.deathchance = 0
    def death(self):
        if not self.marriage == None:
            marriage.partners.remove(self) #No longer married
        PEOPLE.remove(self) #No longer living
        LOG.append(self.firstname + " "+self.lastname + " died in the year of "
                   + str(DAY//365)+ ", at the age of "+str(self.age//365))
        
    

class marriage:
    def __init__(self, p1, p2):
        """
        The last name of all children and all partners is the last name of 
        p1
        """
        p1.marriage = self
        p2.marriage = self
        self.lastname = p1.lastname
        p2.maidenname = p2.lastname
        p2.lastname = self.lastname
        self.children = []
        self.nchildren = 0
        self.partners = (p1,p2)
    def addchild(self, child):
        self.children.append(child)
        self.nchildren += 1
        
tick =1 
   
PEOPLE.append(person())    
for DAY in range(MAXDAYS):
    if len(PEOPLE) < 4:
        for i in range(random.randint(4,10)):
            PEOPLE.append(person())
    for per in PEOPLE:
        per.age += 1
        if DAY%365 == 0:
            if random.randint(1,100) < (8/400000000)*(((per.age//365)-20)**8):
                per.death()

    

for elem in LOG:
    print(elem)