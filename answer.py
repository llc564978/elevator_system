import random
import time
import threading

"""
setup
"""
customer = {}
customer2 = {}
number_of_people = 40
count = 0

class elevator:

    def __init__(self):

        self.maximum = 5
        self.operatingTime = 1
        self.operatingSum = 0
        self.nowFloor = 1
        self.state = True
        self.inhouse = 0
        self.goOut_of_people = 0
        self.floor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
        
    def rise(self):

        if(self.nowFloor >= 9):
            self.state = False

        self.operatingSum = self.operatingSum + self.operatingTime
        self.nowFloor = self.nowFloor + 1
        #time.sleep(1)

    def down(self):

        if(self.nowFloor <= 2):
            self.state = True

        self.operatingSum = self.operatingSum + self.operatingTime
        self.nowFloor = self.nowFloor - 1
        #time.sleep(1)

    def open(self):

        self.goOut_of_people+=1
        self.operatingSum = self.operatingSum + self.operatingTime
        #time.sleep(1)

    def printInformation(self):

        print("Total Time: " , self.operatingSum)


class A(elevator):

    def __init__(self):

        super().__init__()

class B(elevator):

    def __init__(self):

        super().__init__()


A = A()
B = B()

def queue(i, eid):
    global number_of_people

    timer = random.uniform(0, 2)
    if(timer < 1):

        if(eid[0] == 'A'):

            name = "employee_{}".format(i)
            customer[name] = random.choice([ele for ele in A.floor if ele != A.nowFloor])

            number_of_people = number_of_people - 1
            A.inhouse += 1 

        else:
            name = "employeeB_{}".format(i)
            customer2[name] = random.choice([ele for ele in A.floor if ele != B.nowFloor])

            number_of_people = number_of_people - 1
            B.inhouse += 1 
        #time.sleep(1)


def main(eid):

    global number_of_people
    global count

    while A.inhouse > 0 or B.inhouse or number_of_people > 0:

        if((A.inhouse == 0 and B.inhouse == 0) and number_of_people==0):
            break

        if(number_of_people > 0 and A.inhouse < A.maximum and B.inhouse < B.maximum):
            count+=1
            queue(count, random.choices(['A','B'], k=1))

        if(eid == 'A'):

            if(A.nowFloor <= 10 and A.state == True):
                A.rise()
            else:
                A.down()

            for key, value in dict(customer).items():
                if value == A.nowFloor:  
                    A.inhouse -= 1
                    A.open()
                    del customer[key]

        elif(eid == 'B'):

            if(B.nowFloor <= 10 and B.state == True):
                B.rise()
            else:
                B.down()

            for key, value in dict(customer2).items():
                if value == B.nowFloor:  
                    B.inhouse -= 1
                    B.open()
                    del customer2[key]

        A.printInformation()
        print("-----------A--------:", customer)
        B.printInformation()
        print("-----------B--------:", customer2)


two= threading.Thread(target = main, args=('A'))
three=threading.Thread(target=main, args=('B'))
two.start()
three.start()
two.join()
three.join()


print("exit: ", A.goOut_of_people + B.goOut_of_people)
print("Done.")

