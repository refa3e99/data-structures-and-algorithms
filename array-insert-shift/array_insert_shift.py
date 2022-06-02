def insertShiftArray(arr, num):
    newArr = []
    mid = int(len(arr)/2)
    if len(arr) % 2 == 0:
        newArr += arr[:mid:]
        newArr.append(num)
        return newArr+arr[mid:len(arr):]
    else:
        newArr += arr[:mid+1:]
        newArr.append(num)
        return newArr + arr[mid+1:len(arr):]

print(insertShiftArray([1,2,3,4],9))