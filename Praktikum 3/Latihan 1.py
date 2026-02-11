# Implementasi Single Linked List dengan operasi penghapusan node berdasarkan nilai
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

#single linked list
class SingleLinkedList: 
    def __init__(self):
        self.head = None
# menambahkan node baru di akhir linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
# menambahkan node baru di akhir linked list
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
# menghapus node berdasarkan nilai
    def delete_node(self, key):
        temp = self.head

        # Jika node yang dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
# Mencari node yang akan dihapus
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
# Jika nilai tidak ditemukan dalam linked list
        if temp is None:
            print("Elemen tidak ditemukan.")
            return
# Menghapus node
        prev.next = temp.next
        temp = None
# Menampilkan linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# Contoh penggunaan
sll = SingleLinkedList()
data = [1, 3, 5, 7, 9]
# Menambahkan elemen ke linked list
for item in data:
    sll.append(item)
# Menampilkan linked list sebelum penghapusan
print("Linked List sebelum dihapus:")
sll.display()
# Menghapus node dengan nilai tertentu
hapus = int(input("Masukkan elemen yang ingin dihapus: "))
sll.delete_node(hapus)
# Menampilkan linked list setelah penghapusan
print("Linked List setelah dihapus:")
sll.display()