arr = []
for i in range(int(input())) :
	query_value = []
	query_value = input().split()
	if query_value[0] == "1" :
		arr.append(query_value[1])
	elif query_value[0] == "2" :
		arr.pop(0)
	else :
		print(arr[0])
	