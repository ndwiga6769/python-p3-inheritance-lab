#!/usr/bin/env python3

from user import User

import random

class Teacher(User):
    
    def __init__(self,first_name,last_name):
        self.knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]
        super().__init__(first_name,last_name)
        
    def teach(self):  
        return random.choice(self.knowledge)
mwangi = Teacher("David","Mwangi")
# print(mwangi.knowledge)
print (mwangi.teach())