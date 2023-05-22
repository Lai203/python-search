def binary_search (data, target) :
    low = 0
    high = len(data) - 1

    while low <= high :
        mid = (low + high) // 2
        if data[mid] == target :
            return mid
        elif data[mid] < target :
            low = mid + 1
        else :
            high = mid - 1

    return -1

names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "George"]
target_name = input ("Masukkan Nama Yang Ingin Dicari : ")
index = binary_search(names, target_name)

if index != -1:
    print ("Nama Ditemukan Pada Indeks", index)
else : 
    print ("Nama Tidak Ditemukan")