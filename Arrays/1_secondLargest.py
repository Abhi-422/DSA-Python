def secondLargest(arr):
    largestEle = -1
    secLargestEle = -1
    for i in arr:
        if i > largestEle:
            secLargestEle = largestEle
            largestEle = i
        elif i < largestEle and i > secLargestEle:
            secLargestEle = i

    return secLargestEle

if __name__ == "__main__":
    arr = list(map(int, input().split(",")))
    print(secondLargest(arr))