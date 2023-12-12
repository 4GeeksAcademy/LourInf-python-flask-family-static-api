
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:  #1. we define our class which will represent a family structure object
    def __init__(self, last_name): #2. we initialize it with the constructor method "__init__", like saying "to start creating a FamilyStructure we first need the FamilyStructure itself (self) and whatever else we want to add as a parameter (last_name)
        self.last_name = last_name #3.we define the attributes that my FamilyStructure will have, so I'm saying: this FamilyStructure has a last name of X (the last_name that I will pass). So this attribute will store the family's last name.
        self._members = [] # this list stores family members
   
    #4. here we define the methods we want to create and use in our object
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
