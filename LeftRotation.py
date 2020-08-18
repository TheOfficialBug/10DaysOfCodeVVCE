_, num_of_rotations = list(map(int, input().split()))
array = list(map(int, input().split()))
for i in range (0, num_of_rotations) :
	array.append(array[0])
	array.remove(array[0])
for i in array:
	print(i, end=" ")
