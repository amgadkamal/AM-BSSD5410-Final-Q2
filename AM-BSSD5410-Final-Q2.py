import numpy as np
"""Adaptation of square grid. A project to work with 2D array, 
and adjust size and starting corner accoring to user input with max count number"""
#shape function
def shape(size,limit):
 a = np.arange(1,size*size+1).reshape(size,size)
 try:

    a[1][0] = a[0][1]
    a[2][0] = a[1][1] = a[0][2]
    a[3][0] = a[2][1] = a[1][2] = a[0][3]
    a[4][0] = a[3][1] = a[2][2] = a[1][3]= a[0][4]
    a[5][0] = a[4][1] = a[3][2] = a[2][3] = a[1][4]=a[0][5]
    a[6][0] = a[5][1] = a[4][2] = a[3][3] = a[2][4]=a[1][5]=a[0][6]
    a[7][0] = a[6][1] = a[5][2] = a[4][3]= a[3][4]=a[2][5]=a[1][6]=a[0][7]

 except IndexError:
    pass

 FindLimitValue=np.where(a>limit)
 a[FindLimitValue]=0
 return a
#end def shape

#function for starting corner
def Top_Right(array):
 array2 = np.flip(array, 1)
 print(array2)

def Bottom_Right(array):
 array2= np.flip(array, (1, 0))
 print(array2)

def Bottom_Left(array):
 array2=np.flip(array,0)
 print(array2)

def Top_Left(array):
 print(array)

#menu
def menu():
    print("Choose starting corner \n","BL \n","TL \n","TR \n","BR \n")
#end def menu

#switcher
class Switcher(object):
    def indirect(self, method_name):
        method = getattr(self, method_name, lambda: 'Invalid')
        return method()

    def TR(self):
        return Top_Right

    def BL(self):
        return Bottom_Left

    def BR(self):
        return Bottom_Right

    def TL(self):
        return Top_Left
#end class switcher

#operation function
def operation(a,array):
    s = Switcher()
    w = s.indirect(a)
    return w(array)
#end operaion function

#main function
def main():
    size = int(input("Please enter the size of the grid between 1 and 8"))
    limit = int(input("Which you would like to stop in the count ?"))
    menu()
    corner = input()
    array = shape(size, limit)
    operation(corner, array)
#end def main

if __name__ == '__main__':
    main()