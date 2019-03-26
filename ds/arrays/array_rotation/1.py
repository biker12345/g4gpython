# program to rotate a array  for the array of size n we will be asked to rotate it by d times 

def gcd(a,b):
	return a if b == 0 else gcd(b,a%b)

def rotate_array(arr,rotation_count):
	for i in range(0,gcd(len(arr),rotation_count)):
		temp, j = arr[i], i # always keep the first element of the segment saved
		j = i
		while True:
			k = rotation_count + j
			if k >= len(arr):
				k -= len(arr) 
			if k == i:
				break
			arr[j], j = arr[k], k
		arr[j] = temp
	return arr
x = [1,2,3,4,5,6,7,8,9,10,11,12]
x = rotate_array(x ,3)
print (x)