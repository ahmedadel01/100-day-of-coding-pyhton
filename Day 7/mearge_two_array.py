# Merage two sorted array
def Merge_Array(arr):
    if len(arr) > 1 :
        # r is he point where the array is divide into two subarray
        r = len(arr) // 2
        L = arr[:r] #subarray one
        M = arr[r:] # subarray two

        # sorte the two halves
        Merge_Array(L)
        Merge_Array(M)

        i = j = k = 0 

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M) : 
            if L[i] < M[j] :
                arr[k] = L[i]
                i += 1
            else : 
                arr[k] = M[j]
                j += 1

            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1


# print array
def printList(array):
    for i in range(len(array)):
        print(array[i], end = ' ')
    print()

# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    Merge_Array(array)

    print("Sorted array is: ")
    printList(array)
