# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:23:36 2018

@author: e
"""
MAXDAYS = 73000
LOG = []
PEOPLE = []
MARRIAGES = []
DAY = 0 
DATINGPOOL = []
RULER  = None
HEIR = None
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
        if self not in PEOPLE:
            PEOPLE.append(self)
        self.age = 0
        self.deathchance = 0
        self.dating = False
        self.name = (self.firstname+ " " + self.lastname)
    def death(self):
        if not self.marriage == None:
            marriage.partners.remove(self) #No longer married
        PEOPLE.remove(self) #No longer living
        LOG.append(self.firstname + " "+self.lastname + " died in the year of "
                   + str(DAY//365)+ ", at the age of "+str(self.age//365))
        global RULER
        global HEIR
        if self == RULER:
            RULER = HEIR
            HEIR = None
        
    

class marriage:
    RULER
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
        LOG.append("in the year of "+ str(DAY//365) + " "+ p1.name +
                   " married " + p2.name)
    def addchild(self):
        global HEIR
        child = person()
        self.children.append(child)
        self.nchildren += 1
        if RULER in self.partners and HEIR != None:
            HEIR = child
    
    
def matchmaking(): #code for handling and marrying people in the dating pool
    if len(DATINGPOOL) > 2:
        mpool = []
        fpool = []
        for per in DATINGPOOL: #splitting the pool into males and females
            if per.gender == "male":
                mpool.append(per)
            else:
                fpool.append(per)
        if len(fpool) != 0 and len(mpool) != 0:
            if RULER in DATINGPOOL:
                if RULER.gender == "male":
                    MARRIAGES.append(marriage(RULER, random.choice(fpool)))
                else:
                    MARRIAGES.append(marriage(RULER, random.choice(mpool)))
   

RULER = person()  
for DAY in range(MAXDAYS):
    if len(PEOPLE) < 4: #creating more people should the supply ever fail
        for i in range(random.randint(4,10)):
            PEOPLE.append(person())
    for per in PEOPLE:
        per.age += 1 #everyone gets older
        if DAY%365 == 0: #once per year checks
            if random.randint(1,100) < (8/400000000)*(((per.age//365)-30)**6):
                per.death()
            if (per.marriage == None and per.age//365 > 18 and per.dating == 
                False):
                per.dating = True
                DATINGPOOL.append(per)
            matchmaking()

            

for elem in LOG:
    print(elem)