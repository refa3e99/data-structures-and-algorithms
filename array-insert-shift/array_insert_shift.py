def insertShiftArray(arr, num):
    newArr = []
    mid = int(len(arr)/2)
    newArr += arr[:mid:]
    newArr.append(num)
    return newArr+arr[mid:len(arr):]

print(insertShiftArray([1,2],9))