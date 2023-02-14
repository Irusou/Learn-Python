numbers = [1,40, 2, 20 , 23, 54, 2, 324, 5, 39]

def printArray(array) :
    st = ""
    for i in range(len(array)) :
        st += " "+str(array[i]) 
    print("\n" + st)

printArray(numbers)

#bubble sort
def bubbleSort(numbers) :
    length = len(numbers)
    for i in range(length-1):
        for j in range(0, length-i-1):
            if numbers[j] > numbers[j + 1]:
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp  
    printArray(numbers)


bubbleSort(numbers)