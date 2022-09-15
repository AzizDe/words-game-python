import random # To use choices built-in function to put letters in a list randomly
class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """ A singly-linked list. """
    def __init__(self):
        """ Create an empty list. """
        self.head = None
        self.tail = None

        self.count = 0

    def iter(self):
        """ Iterate through the list. """
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def append(self, data):
        """ Append an item to the list """
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1

    def insertFirst(self, data):
        """Insert new Nodes as Head """
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        self.count += 1

    def deleteFirst(self):
        """ Delete Head from the list """
        self.head= self.head.next
        self.count -=1

    def insertLast(self, data):
        """Insert new Nodes as Tail """
        node = Node(data)

        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1


    def deleteLast(self):
        """ Delete Tail from the list """
        current = self.head
        for n in range(0, self.count-1):
            current = current.next

        self.tail=current
        current.next = None
        self.count -=1


    def delete(self, data):
        """ Delete a node from the list """
        current = self.head
        NextNode = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    NextNode.next = current.next
                self.count -= 1
                return
            NextNode = current
            current = current.next

    def search(self, data):
        """ Search through the list. Return True if data is found, otherwise
        False. """
        for node in self.iter():
            if data == node:
                return True
        return False


    def print(self):
        current=self.head
        while current != None:
            print(current.data)
            current=current.next

def readFile():
    fileObj = open('dictionary', "r")  # opens the file in read mode
    content = []
    content2=[]
    for line in fileObj:
        content.append(line)
    for i in content:
        i=i.replace("\n","")
        content2.append(i)
    return content2
readFile()


letters = "abcdefghijklmnopqrstuvwxyz"
rand = random.choices(letters,k=12) # to put letters randomly in a list
ssl=SinglyLinkedList()

print("Create your words from the following letters:")
for ll in rand:
    print(ll,end="   ")
print()

credit=0
holo1=rand[:]
num = 0
while num!="-1" :
    holo2=[]
    num = input("Please enter your next word or -1 to end\n")
    if num=="-1":
        break
    for lette in num:
        if lette in holo1:
            holo1.remove(lette)
            holo2.append(lette)
            """ to make a  new list contains the letters of entered word after checking
             the given letters"""
        elif lette not in holo1:
            print("Incorrect use of letter")
    if len(num) == len(holo2):
        if num in readFile(): # check if the word in dictionary
            if ssl.search(num) == False: # to check the duplication
                ssl.append(num) # add the word to the linked list
                credit+=1 # increase credit by 1
                print("This is Correct :)")
            else:
                print("You've already entered the word, no credit!")
        else:
            print("This word does not exist in the dictionary.")
    holo1 = rand[:] # to return the original list
print("You've entered the following correct words:")
ssl.print()
if credit>0:
    print("You've got",credit,"points. Well done!")
else:
    print("You've got",credit,"points")

""" 
output :
Create your words from the following letters:
m   c   q   m   j   o   o   h   t   k   t   o   
Please enter your next word or -1 to end
to
This is Correct :)
Please enter your next word or -1 to end
to
You've already entered the word, no credit!
Please enter your next word or -1 to end
oh
This word does not exist in the dictionary.
Please enter your next word or -1 to end
r
Incorrect use of letter
Please enter your next word or -1 to end
-1
You've entered the following correct words:
to
You've got 1 points. Well done!

Process finished with exit code 0
"""


