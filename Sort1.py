array = [687, 537, 259, 929, 381, 707, 220, 949, 880, 788, 834, 402, 146, 807, 376]

print("Sortirovka puzirkom")
for i in range(0,len(array)):
    for j in range(0,len(array)-1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
for i in range(0,len(array)):
    print(array[i])

array = [115, 992, 924, 978, 633, 273, 975, 279, 762, 698, 639, 895, 822, 398, 448]

print("Sortirovka vstavkami")
for i in range(0,len(array)):
    k = i
    while (k > 0 and array[k-1] > array[k]):
        temp = array[k-1]
        array[k-1] = array[k]
        array[k] = temp
        k -= 1
for i in range(0,len(array)):
    print(array[i])

array = [989, 572, 756, 813, 47, 443, 79, 41, 843, 475, 260, 27, 52, 524, 780]

print("Sortirovka viborom")
for i in range(0,len(array)):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        temp = array[i]
        array[i] = array[m]
        array[m] = temp
for i in range(0,len(array)):
    print(array[i])