import random

end=random.randint(3,20)


#print(pointerList[0])


def cycle_shuffle(_len):


    index=0
    shuffled=[0]*(_len)
    pointerList=range(0,_len)
    pointerList.reverse()
    lastPiece=pointerList.pop() 

    midPoint=int((_len-1)/2)

    left=pointerList[:midPoint]
    right=pointerList[midPoint:]
    random.shuffle(right)
    random.shuffle(left)

    while(len(left) or len(right)):

	if(len(right)):
		shuffled[index]=right.pop()
		index = shuffled[index]

	if(len(left)):
		shuffled[index]=left.pop()
		index = shuffled[index]

	
    shuffled[index]=lastPiece
    
    return shuffled








x = -99


while(x==-99):

    print("Enter any positive integer greater than 2 (Enter -1 for a random):")
    x = input()

    if(not (isinstance(x,int))):
        print("Err: Please input an integer")
        x=-99
        continue
    
    if(x==-1):
        x=random.randint(2,20)
    

    if(x<2):
        print("Err: Please input a number greater than 2")
        x=-99
        continue


    shuf = cycle_shuffle(x)
    print(shuf)
