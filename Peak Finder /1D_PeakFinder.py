# def recursivePeakFinder(arr,n,firstIndex,lastIndex):

# 	midIndex = int(firstIndex+(lastIndex - firstIndex)/2)

# 	#DIVIDE AND CONQUER APPROACH WITH BIANRY SEARCH

# 	if(((arr[midIndex-1] <= arr[midIndex]) or (arr[midIndex-1] <= arr[midIndex])) and 
# 		((arr[midIndex+1] <= arr[midIndex]) or (midIndex == n-1))):

# 		return midIndex

# 	elif(midIndex > 0 and arr[midIndex-1] > arr[midIndex]):

# 		return recursivePeakFinder(arr,n,firstIndex,midIndex-1)

# 	else:

# 		return recursivePeakFinder(arr,n,(midIndex+1),lastIndex)







# def wrapRecursiveFunction(arr,n):
# 	return recursivePeakFinder(arr,n, 0 , n - 1)


# inputArray = [1, 3, 20, 4, 1, 0,2,4,6,21]
# print("Peak of the Array is: ",inputArray[wrapRecursiveFunction(inputArray,len(inputArray))])




# A python3 program to find a peak 
# element element using divide and conquer

# A binary search based function 
# that returns index of a peak element
def findPeakUtil(arr, low, high, n):
	
	# Find index of middle element
	# (low + high)/2 
	mid = low + (high - low)/2
	mid = int(mid)
	
	# Compare middle element with its 
	# neighbours (if neighbours exist)
	if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
		(mid == n - 1 or arr[mid + 1] <= arr[mid])):
		return mid


	# If middle element is not peak and 
	# its left neighbour is greater 
	# than it, then left half must 
	# have a peak element
	elif (mid > 0 and arr[mid - 1] > arr[mid]):
		return findPeakUtil(arr, low, (mid - 1), n)

	# If middle element is not peak and
	# its right neighbour is greater
	# than it, then right half must 
	# have a peak element
	else:
		return findPeakUtil(arr, (mid + 1), high, n)


# A wrapper over recursive 
# function findPeakUtil()
def findPeak(arr, n):

	return findPeakUtil(arr, 0, n - 1, n)


# Driver code
arr = [1, 3, 20, 45, 1, 60,21]
n = len(arr)
print("Index of a peak point is", arr[findPeak(arr, n)])
	
# This code is contributed by 
# Smitha Dinesh Semwal
