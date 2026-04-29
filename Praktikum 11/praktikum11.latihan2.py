#=============================================
# Nama :Baytul Rafli
# NIM  :J0403251027
# Kelas: BP/1 
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur)
#=============================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()
print("\nDFS dari A:")
dfs(graph, 'A', visited)

# Pertanyaan Analisis:
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
#    -> Karena DFS menelusuri jalur secara rekursif hingga tidak ada 
#       neighbor lagi, baru kembali ke atas (backtracking).
# 2. Apa yang terjadi jika urutan neighbor diubah?
#    -> Urutan kunjungan node akan berbeda sesuai urutan neighbor 
#       yang ditentukan dalam graph.
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
#    -> BFS menelusuri node secara level (lapisan), sedangkan DFS 
#       menelusuri node secara mendalam (depth). 
#       Hasil urutan kunjungan akan berbeda: BFS lebih lebar, DFS lebih dalam.
