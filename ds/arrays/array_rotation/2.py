# reverse reversal algorithm for array 
# divide the array into two parts 0-d = A and d+1 - n = B
# reverse A = Ar
# reverse B = Br
# reverse ArBr = BA

def reverse_list_with_limits(arr, start, end):
	while start < end:
		temp = arr[start]
		arr[start] = arr[end]
		arr[end] = temp
		start +=1 
		end -=1 

def reverse_main(arr, d):
	reverse_list_with_limits(arr, 0, d-1)
	reverse_list_with_limits(arr, d, len(arr)-1)
	reverse_list_with_limits(arr, 0, len(arr)-1)

arr = [1,2,3,4,5,6,7]
reverse_main(arr, 2)
print(arr)