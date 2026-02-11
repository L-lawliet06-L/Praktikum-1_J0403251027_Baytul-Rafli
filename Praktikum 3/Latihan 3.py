# ===== Latihan 3: Mencari Elemen dalam Doubly Linked List =====
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None
# menambahkan node baru di akhir doubly linked list
    def append(self, data):
        new_node = DNode(data)
# jika linked list kosong
        if self.head is None:
            self.head = new_node
            return
# menambahkan node baru di akhir doubly linked list
        temp = self.head
        while temp.next:
            temp = temp.next
# menambahkan node baru
        temp.next = new_node
        new_node.prev = temp
# mencari elemen dalam doubly linked list
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Doubly Linked List.")
                return
            temp = temp.next

        print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")


# ===== Program Utama =====
dll = DoublyLinkedList()
# menambahkan elemen ke doubly linked list
data = list(map(int, input("Masukkan elemen Doubly Linked List (pisahkan dengan spasi): ").split()))
# menambahkan elemen ke doubly linked list
for item in data:
    dll.append(item)
# mencari elemen dalam doubly linked list
cari = int(input("Masukkan elemen yang ingin dicari: "))
dll.search(cari)