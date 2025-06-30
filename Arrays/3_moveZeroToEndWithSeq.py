def moveZeroToEndWithSeq(arr):
    left = 0
    for right in range(len(arr)):
        if arr[right]!=0:
            arr[right],arr[left]=arr[left],arr[right]
            left+=1



if __name__ == "__main__":
    arr = list(map(int, input().split()))
    moveZeroToEndWithSeq(arr)
    print(arr)