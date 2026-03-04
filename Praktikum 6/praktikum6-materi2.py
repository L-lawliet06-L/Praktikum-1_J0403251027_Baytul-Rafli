#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#
#insertion sort (ascending)
#----------------------------------------------#

def insertion_sort(data):
    print("data awal : ", data)
    print("="*50)

    for i in range(1, len(data)):
        Key = data[i]
        j = i - 1

        print("iterasi ke-", i)
        print("Nilai key =", Key)
        print("bagian kiri (terurut)", data[:i])
        print("bagian kanan (belum terurut)", data[i:])

        # geser elemen ke kanan selama lebih besar dari Key
        while j >= 0 and data[j] > Key:
            data[j+1] = data[j]
            j -= 1

        # sisipkan Key ke posisi yang benar
        data[j+1] = Key

        print("setelah disisipkan ke kiri:", data)
        print("-"*50)

    return data

angka = [7, 8, 5, 2, 4, 6]
print("Hasil dari", insertion_sort(angka))