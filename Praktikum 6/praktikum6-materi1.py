#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#
#insertion sort (ascending)
#----------------------------------------------#

def insertion_sort(data) :
    #loop mualai dari data kedua (index array ke 1)
    for i in range(1, len(data)):

        Key = data[i] #simpan nilai yang disisipkan
        j = i-1 # index elemen terakhir di bagian kiri
    
    while j>=0 and data [j] > Key:
        data[j+1] = data[j]
        j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = Key
    return data

angka = [7,8,5,2,4,6]
print("Hasil dari", insertion_sort(angka))
