#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#
# merge sort (ascending)
#----------------------------------------------#

def merge_Sort (data, depth=0):
    indent = " " * depth # indentadi berdasarkan level rekrusif
    print(f"{indent} merge_sort{data}")

    if len(data) <= 1:
        return data


    #devine : membagi data menjadi 2 bagian
    mid = len(data) //2
    left = data[:mid] # slicing bagian kiri
    rigth = data[mid:] #slicing bagian kanan
    
    indent = " " * depth # indentadi berdasarkan level rekrusif
    print(f"{indent} devide -> left = {left}| right = {rigth}")

    #8 ==> left 4 right 4
    #left 4 ==> merge sort ==>
    #    left 2 ==> merge sort
    #    right 2 ==> merge sort


    #recrusive call
    left_sorted = merge_Sort(left)
    rigth_sorted = merge_Sort(rigth)

    merged = merge (left_sorted, rigth_sorted)
    print(f"{indent}merge -> {left_sorted} + {rigth_sorted} = {merged}")

    return merge(left_sorted, rigth_sorted)

def merge(left,right):
    
    result = []
    i = 0
    j = 0

    #membanndingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right [j]:
           result.append(left[i])
           i+=1
        else: 
            result.append(right[j])
            j+=1
    #menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result


angka = [13,7,28,5,19,36,4]
print("Hasil Sorting: ", merge_Sort(angka))
