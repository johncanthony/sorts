import random

pointerList=[0,1,2,3,4,5,6,7,8,9]
pointerList.reverse()


print(pointerList[0])
lastPiece=pointerList.pop()

print(lastPiece)
print(pointerList)

totalLength=len(pointerList)
midPoint=int(len(pointerList)/2)

left=pointerList[:midPoint]

index=0
right=pointerList[midPoint:]
random.shuffle(right)
random.shuffle(left)

index=0

print(left)
print(right)

index=0
shuffled=[0]*(totalLength+1)
print(shuffled)


while(len(left) or len(right)):

	if(len(right)):
		shuffled[index]=right.pop()
		index = shuffled[index]

	if(len(left)):
		shuffled[index]=left.pop()
		print(shuffled[index])
		index = shuffled[index]

	
shuffled[index]=lastPiece
print(shuffled)
			
