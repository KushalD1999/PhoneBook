from linkedlist import SingleLinkedList
from node import Node
"""

Name: Kushal Dalal
Date: 23rd June 2018
"""


class MissingPhoneNumberException(Exception):
    pass


class MissingNameException(Exception):
    pass


class SameContactException(Exception):
    pass


class InvalidPhoneNumberException(Exception):
    pass


class Contact():
    def __init__(self, cp=None, name=None, surname=None, hp=None, wp=None,
                 email=None, ha=None, fav=False):
        '''(Contact, str, str, str, str, str, str, str, bool) -> NoneType
        Initializes the instances of the all the contacts if given'''
        # Instances of the contacts
        self._cellphone = cp
        self._name = name
        self._surname = surname
        self._homephone = hp
        self._workphone = wp
        self._email = email
        self._homeaddress = ha
        self._fav = fav
        # instance to keep track of the primary phone number
        self._primaryphone = None

        # check if the name or surname is given or not
        if (self._name is None) and (self._surname is None):
            # else raise an exception
            raise MissingNameException("First Name and Surname are missing")

        # Check which primary cell phone number is given
        # Check if the cellphone is given
        if(self._cellphone is not None):
            # set primary phone to the given cellphone
            self._primaryphone = self._cellphone
        # Check if the homephone is given and cellphone is none
        elif (self._cellphone is None) and (self._homephone is not None):
            # set primary phone to the given homephone
            self._primaryphone = self._homephone
        else:
            # set primary phone to the given workphone
            self._primaryphone = self._workphone

        # if no phone number is given then raises an exception
        if (self._primaryphone is None):
            raise MissingPhoneNumberException("Phone Number is Missing")

    def set_cellphone(self, cell):
        '''(Contact, str) -> NoneType
        set the cellphone of the contact'''
        self._cellphone = cell

    def get_cellphone(self):
        '''(Contact) -> str
        returns the cellphone of the contact'''
        return self._cellphone

    def set_name(self, person_name):
        '''(Contact, str) -> NoneType
        set the name of the contact'''
        self._name = person_name

    def get_name(self):
        '''(Contact) -> str
        returns the name of the contact'''
        return self._name

    def set_surname(self, person_surname):
        '''(Contact, str) -> NoneType
        set the surname of the contact'''
        self._surname = person_surname

    def get_surname(self):
        '''(Contact) -> str
        returns the surname of the contact'''
        return self._surname

    def set_homephone(self, homephone):
        '''(Contact, str) -> NoneType
        set the homephone of the contact'''
        self._homephone = homephone

    def get_homephone(self):
        '''(Contact) -> str
        returns the homephone of the contact'''
        return str(self._homephone)

    def set_workphone(self, workphone):
        '''(Contact, str) -> NoneType
        set the workphone of the contact'''
        self._workphone = workphone

    def get_workphone(self):
        '''(Contact) -> str
        returns the workphone of the contact'''
        return self._workphone

    def set_email(self, email):
        '''(Contact, str) -> NoneType
        set the email of the contact'''
        self._email = email

    def get_email(self):
        '''(Contact) -> str
        returns the email of the contact'''
        return self._email

    def set_homeaddress(self, homeaddress):
        '''(Contact, str) -> NoneType
        set the homeaddress of the contact'''
        self._homeaddress = homeaddress

    def get_homeaddress(self):
        '''(Contact) -> str
        returns the name of the contact'''
        return self._homeaddress

    def set_fav(self):
        '''(Contact) -> NoneType
        set the contact as a fav'''
        self._fav = True

    def unset_fav(self):
        '''(Contact) -> NoneType
        set the contact as a un-fav'''
        self._fav = False

    def is_fav(self):
        '''(Contact) -> bool
        checks if the contact is fav'''
        return self._fav

    def get_primaryphone(self):
        '''(Contact) -> str
        returns the primary phone number of the contact'''
        return self._primaryphone

    def is_primaryphone(self, check):
        '''(Contact, phone) -> bool
        checks if the given phone number is primary phone number'''
        if(self._primaryphone is check):
            ret = True
        else:
            ret = False
        return ret

    def primary_name(self):
        '''(Contact) -> bool
        returns the primary name of contact'''
        if (self._surname is None):
            ret = self._name
        else:
            ret = self._surname
        return str(ret.capitalize())

    def main_name(self):
        '''(Contact) -> bool
        returns the primary name of contact without changing it'''
        if (self._surname is None):
            ret = self._name
        else:
            ret = self._surname
        return str(ret)

    def __str__(self):
        new = (self.main_name(), self._primaryphone,)
        return str(new)

    def __eq__(self, other):
        '''(Contact, Contact) -> bool
        checks if the givencontact is equal to the contact and returns bool'''
        output = (self._cellphone == other._cellphone) and \
            (self._name == other._name) and (self._surname == other._surname) \
            and (self._homephone == other._homephone) and \
            (self._workphone == other._workphone) and \
            (self._email == other._email) and \
            (self._homeaddress == other._homeaddress) and \
            (self._fav == other._fav) and \
            (self._primaryphone == other._primaryphone)
        return output


class PhoneBook(SingleLinkedList):
    def __init__(self, contact=None):
        '''(Phonebook,contact) -> NoneType
        initializes the references of an empty SLL and contact if given'''
        # Initialize the instances of linked list
        super().__init__()
        # Check if the contact is given while initializing phonebook
        if (contact is not None):
            # create a node of that given contact
            new = Node(contact)
            # set the given contact as head
            self.set_head(new)

    # CHeck if the contact exists or not
    # check given contact exists with less info then merge them
    def add(self, contact):
        '''(PhoneBook, contact) -> NoneType
        Adds the given contact in the phonebook in the alphabetical order
        REQ: First Name or Surname must be given'''
        # Set Curr as a head of the phonebook
        curr = self._head
        # Set result as a false to keep track if same nodes are being added
        result = False
        # Loop that check if the contact that is being added is already existed
        while (curr is not None) and (result is False):
            # If given contact is euqal to curr using equals method
            if(curr.get_element() == contact):
                # change result to true
                result = True
            else:
                # move the pointer
                curr = curr.get_next()
        # if the given contact is already present
        if(result is True):
            # ignore the given contact
            pass
        # else add the given contact
        else:
            # if the phonebook is empty
            if (self.get_head() is None):
                # create a node of the given contact
                new = Node(contact)
                # set the node as a head of the linked list phonebook
                self.set_head(new)
            # if the phonebook is not empty
            else:
                # set curr as head of the phonebook(linked list)
                cur = self._head
                # compare the primary names for given contact and the head
                if (cur.get_element().primary_name() > contact.primary_name()):
                    # create a node if given contact goes in front of sll
                    new = Node(contact)
                    # setthat new node as a head of phonebook
                    self._head = new
                    # set that new node's next to old phonebook
                    new.set_next(cur)
                else:
                    # create a node for give contact
                    new = Node(contact)
                    # set cur to head of the phonebook
                    curr = self._head
                    # create a variable that keep tracks of place to add a
                    # given contact
                    out = False
                    # variable that keeps tract of the previous node
                    prev = None
                    # loop through the phonebook until you find the right spot
                    # to add the given contact
                    while (curr is not None) and (out is False):
                        contact_name = contact.primary_name()
                        # if the index is found to add a contact
                        if (curr.get_element().primary_name() > contact_name):
                            # change the variable to True to get out of loop
                            out = True
                        else:
                            # else continue traversing through the list
                            prev = curr
                            curr = curr.get_next()
                    # add the node of the given contact between the previous
                    # node and the current i.e. curr node
                    prev.set_next(new)
                    new.set_next(curr)

    # IMPLEMENT __eq__
    def remove(self, contact):
        '''(PhoneBook, contact) -> NoneType
        Removes the given contact in the phonebook from the alphabetical order
        REQ: First Name or Surname must be given'''
        # check if the head of the phonebook is same as contact given
        if (self._head.get_element() == contact):
            # remove that node using method from sll
            self.remove_first()
        # if the given contact is not same as head node of phonebook sll
        else:
            # traverse through the phonebook to find the contact by
            # keeping track of nodes, setting up the variables curr and prev
            curr = self._head
            out = False
            prev = None
            # Traverse until contact not found and curr is not none
            while (curr is not None) and (out is False):
                # If given contact found
                if (curr.get_element() == contact):
                    # change the output to True to get rid of loop
                    out = True
                else:
                    # else continue traversing through the phonebook
                    prev = curr
                    curr = curr.get_next()
            # remove the node, if found
            if(out is False):
                return None
            else:
                prev.set_next(curr.get_next())

    def show_fav_list(self):
        '''(PhoneBook) -> List
        Removes the list of the favourite contact in the phonebook from the
        alphabetical order
        REQ: First Name or Surname must be given in the contact'''
        # Create Empty list
        fav_list = []
        # traverse through the phonebook using loop to find favourite contacts
        curr = self._head
        while (curr is not None):
            # If the favourite contact find
            if (curr.get_element().is_fav() is True):
                # get their primary name9i.e. surname or firstname)
                temp = curr.get_element().main_name()
                # append that name in the list
                fav_list.append(temp)
                # continue traversing through the phonebook
                curr = curr.get_next()
            else:
                # else continue traversing through the phonebook
                curr = curr.get_next()
        # return the list with all favourite contact names from the list
        return fav_list

    # 647-000-0000
    # 416-000-0000
    def toronto_phone(self):
        '''(PhoneBook) -> (PhoneBook,PhoneBook)
        Returns the phonebook of the contact starting with 416 and 647 in tuple
        from the phonebook of the  alphabetical order
        REQ: Primary phone number must be given in the contact
        REQ: the given contact must start with the 647 or 416 '''
        # Create two empty linked list for storing different phone numbers
        four_one_six = SingleLinkedList()
        six_four_seven = SingleLinkedList()

        # traverse through the list to add the phone numbers in the linked list
        # according to their starting format
        curr = self._head
        while (curr is not None):
            # get the primary phone number of the contact in the phonebook
            new = curr.get_element().get_primaryphone()
            # If the phine number starts with 647
            if(str(new)[:3] == "647"):
                # create the new node of the contact
                node = Node(curr.get_element())
                # add that contact in six_four_seven phonebook sll
                six_four_seven.add_last(node)
                # continue traversing through the list
                curr = curr.get_next()
            # If the phine number starts with 416
            elif (str(new)[:3] == "416"):
                # create the new node of the contact
                node = Node(curr.get_element())
                # add that contact in four_one_six phonebook sll
                four_one_six.add_last(node)
                # continue traversing through the list
                curr = curr.get_next()
            # if the format of primary phone number is not correct
            else:
                # raise an exception
                raise InvalidFormatPhoneNumber("Invalid Format Phone Number")
        # return the tuple with both the sll
        return (four_one_six, six_four_seven)

    def get_sublist(self, letter):
        '''(PhoneBook, str) -> PhoneBook
        Returns the phonebook of the contacts starting all contact names with
        given string of letter from the phonebook of the  alphabetical order
        REQ: First Name or Surname must be given in the contact'''
        # create an empty sll
        sub = SingleLinkedList()
        # traverse through the list to find the contact whose primary name
        # start with the given string letter
        curr = self._head
        while (curr is not None):
            # get the name of the contacts from the phonebook
            new = curr.get_element().main_name()
            # if the first letter of the contact name matches with letter given
            if(str(new)[:1] == letter):
                # create a node and add that node in sll
                node = Node(curr.get_element())
                sub.add_last(node)
                # continue traversing
                curr = curr.get_next()
            else:
                # else continue traversing
                curr = curr.get_next()
        # return the sll with given letter
        return sub

    def get_housemate(self, homephone):
        '''(PhoneBook, str) -> PhoneBook
        Returns the phonebook of the contacts whose homephones are same as
        given homephone from the phonebook of the  alphabetical order
        REQ: homephone must be given in the contact'''
        # Create an empty sll
        home = SingleLinkedList()
        # travrse through the list to get all the housemates who shares same hp
        curr = self._head
        while (curr is not None):
            # get the housephone of each contact
            new = curr.get_element().get_homephone()
            # check if housephone of contact matches given contact
            if(str(new) == homephone):
                # create a node and add that in the given list
                node = Node(curr.get_element())
                home.add_last(node)
                # continue traversing through the phonebook
                curr = curr.get_next()
            else:
                # else continue through traversing the phonebook
                curr = curr.get_next()
        # return the phonebook with housemates sharing same housephone
        return home

    def reversed_phonebook(self):
        '''(PhoneBook) -> PhoneBook
        Returns the phonebook of the contacts in the reverse order from the
        phonebook of the  alphabetical order
        REQ: phonebook must not be empty'''
        # create the empty sll for reverse contacts
        rev = SingleLinkedList()
        # if the reverse phonebook is empty
        if (rev.get_head() is None):
            # create a new node and add that element in reverse phonebook
            new = Node(self.get_head().get_element())
            # set that node as a head of the reverse phonebook
            rev.set_head(new)
        # traverse through the list & keep adding the contact in rev phonebook
        curr = self._head.get_next()
        while (curr is not None):
            # create empty node and add the element in it
            new = Node(curr.get_element())
            # keep adding notes in the front in rev phonebook
            rev.add_first(new)
            # continue traversing through the list
            curr = curr.get_next()
        # return the reversed phonebook
        return rev

    def sync_phonebook(self, phonebook):
        '''(PhoneBook, PhoneBook) -> PhoneBook
        Merges the given phonebook's contacts to the original phonebook in the
        alphabetical order
        REQ: phonebook must be given'''
        # traverse through the list to add all elements of given phonebook to
        # the origina phonebook
        curr = phonebook._head
        while (curr is not None):
            # create new nodes and add the contact in the orginal phonebook
            # copying from the givn phonebook
            new = Node(curr.get_element())
            self.add(new.get_element())
            # continue traversing through the list
            curr = curr.get_next()

    def group_remove(self, lista):
        '''(PhoneBook, list) -> NoneType
        Removes the contact given in the list from the phonebook that are
        present in the alphabetical order
        REQ: List must be given'''
        # Loop through the list until the length og the list
        for x in range(len(lista)):
            # if the head of the phonebook is same as any contact from the list
            if(self._head.get_element() == lista[x]):
                # remove that element by setting new head as its next node
                new = self._head.get_next()
                self.set_head(new)
            # Else traverse through the list and check each element from
            # phonebook is equal to the contact in the given list
            curr = self._head
            prev = None
            while (curr is not None):
                # if the given contact is equal to the contact from phonebook
                if(curr.get_element() == lista[x]):
                    # remove the contact from the phonebook
                    prev.set_next(curr.get_next())
                    # continue traversing through the phonebook
                    curr = curr.get_next()
                else:
                    # else continue traversing through the phonebook
                    prev = curr
                    curr = curr.get_next()

    # if first contact is Favourite
    def rearrange_phonebook(self):
        '''(PhoneBook) -> NoneType
        Rearrages the phonebook in a way that brings all favourite contacts in
        front of the book in alphabetical order following with all unfavourit
        contacts from the phonebook that are present in the alphabetical order
        REQ: List must be given'''
        # Create an empty sll to store all favourite contacts
        emp = SingleLinkedList()
        # set prev to None to keep pointer of the previous node
        prev = None
        # set output to false
        output = False
        curr = self._head
        # traverse through the phonebook to get all favourite contacts
        while (curr is not None):
            # check if thecontact is fav
            if (curr.get_element().is_fav() is True):
                # create a new node and add the contact in new sll created
                new = Node(curr.get_element())
                emp.add_last(new)
                # if the element in head is fav, remove the node by moving
                # pointer to the next node and setting it to head
                if(prev is None):
                    self.set_head(self._head.get_next())
                # remove the node but setting next to current node
                else:
                    prev.set_next(curr.get_next())
                # continue traversing through the list
                curr = curr.get_next()
                output = True
            else:
                # else continue traversing through the list
                prev = curr
                curr = curr.get_next()

        # it there are favourite contacts present in the phonebook
        if (output is True):
            # use the helper method reverse, which changes the order of the
            # the nodes in reversed order
            rev_fav = self.reverse(emp)
            # traverse through the list to add the favourites in the phonebook
            # in front of the list
            curr = rev_fav.get_head()
            while (curr is not None):
                # using the method of sll, add first; add the contacts up front
                self.add_first(curr)
                curr = curr.get_next()

    # HELPER
    def reverse(self, phoneb):
        '''(PhoneBook,PhoneBook) -> PhoneBook
        Reverse the contacts from the phonebook that are present in the
        alphabetical order
        REQ: List must be given'''
        # create empty sll to return the reversed link
        rev = SingleLinkedList()
        # if the reversed sll is empty
        if (rev.get_head() is None):
            # create a node and set the element from given phonebook
            new = Node(phoneb.get_head().get_element())
            # set the node head
            rev.set_head(new)
        # Traverse through the given phonebook and continue traversing
        # through the list
        curr = phoneb._head.get_next()
        while (curr is not None):
            new = Node(curr.get_element())
            rev.add_first(new)
            curr = curr.get_next()
        # return the reversed phonebook
        return rev

    def __str__(self):
        cur = self._head
        result = ""
        while (cur is not None):
            result = result + str(cur.get_element().__str__()) + ", "
            cur = cur.get_next()
        return "(" + result[:-2] + ")"
