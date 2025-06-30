def moveZerosToEnd(arr):
    l = 0
    r = len(arr)-1
    while r>l:
        if arr[r] ==0:
            r-=1
        elif arr[l]!=0:
            l+=1
        else:
            arr[l],arr[r] = arr[r],arr[l]

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    moveZerosToEnd(arr)
    print("Array after moving zeros to the end:", arr)

# 1 2 3 4 5 6 7 8
# 2 3 0 3 4 5 0 0
# 0 1 2 3 4 5 6 7