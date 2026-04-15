#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1
# Latihan 1 : Membuat Node Tree
#=============================================

# Membuat Node 

#CLass node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #Child kiri
        self.right = None #Child kanan

#membuat Root

root = Node("A")

#Menampilkan isi node
print("Data pada root", root.data)
print("Data kiri root", root.left.data)
print("Data kanan root", root.right.data)

# Pembahasan : Node dibuat dengan atribut data, left, dan right.Root didefinisikan sebagai "A", lalu di tampilakn data rootnya yaitu A tetapi karena kiri dan kanan kosong jadinya none.