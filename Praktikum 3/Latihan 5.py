# ===== LATIHAN 5 =====
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# single linked list
class SingleLinkedList:
    def __init__(self):
        self.head = None
# menambahkan node baru di akhir linked list
    def append(self, data):
        new_node = Node(data)
# jika linked list kosong
        if self.head is None:
            self.head = new_node
            return
# menambahkan node baru di akhir linked list
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
# menampilkan linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
# membalik linked list
    def reverse(self):
        prev = None
        current = self.head
# membalik linked list
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
# memperbarui head ke node baru
        self.head = prev


# ===== PROGRAM UTAMA =====
sll = SingleLinkedList()
# menambahkan elemen ke linked list
data = list(map(int, input("Masukkan elemen untuk Linked List (pisahkan dengan spasi): ").split()))
# menambahkan elemen ke linked list
for item in data:
    sll.append(item)
# menampilkan linked list sebelum dibalik
print("Linked List sebelum dibalik:")
sll.display()
# membalik linked list
sll.reverse()
# menampilkan linked list setelah dibalik
print("Linked List setelah dibalik:")
sll.display()
