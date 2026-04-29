#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1 
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
#=============================================

from collections import deque

graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')

# Pertanyaan Analisis:
# 1. Node mana yang dikunjungi pertama?
#    -> Node pertama yang dikunjungi adalah 'Rumah'.
# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
#    -> Karena BFS menelusuri graph secara level per level (lapisan), 
#       sehingga jalur terpendek dari node awal ke node tujuan dapat ditemukan.
# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
#    -> Urutan kunjungan node akan berbeda sesuai dengan perubahan neighbor 
#       (tetangga) pada graph. Jika urutan atau isi neighbor diubah, 
#       maka hasil BFS juga akan berubah.
