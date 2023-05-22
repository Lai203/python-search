#Buatlah sebuah fungsi yang menggunakan binary search untuk mencari posisi sisipan 
#sebuah elemen dalam sebuah daftar yang sudah diurutkan secara menaik. Jika elemen 
#sudah ada dalam daftar, fungsi akan mengembalikan indeksnya. Jika elemen tidak ada 
#dalam daftar, fungsi akan mengembalikan indeks tempat elemen tersebut dapat disisipkan 
#untuk menjaga urutan daftar tetap terurut.

def binary_search_index (data, key) :
    low = 0 
    high = len(data) - 1

    while low <= high :
        mid = (low + high) // 2
        if data[mid] == key :
            return mid 
        elif data[mid] < key :
            low = mid + 1
        else :
            high = mid - 1
    return -1

def binary_search_insert (data, key) :
    low = 0 
    high = len(data) - 1

    while low <= high :
        mid = (low + high) // 2
        if data[mid] == key :
            return 
        elif data[mid] < key :
            low = mid + 1
        else :
            high = mid - 1
    return low


my_list = [2, 4, 6, 8, 10, 12, 14]
key = 15
index = binary_search_index(my_list, key)
if index != -1:
    print (f"Elemen Sudah Ada di Index adalah")
else :
    index = binary_search_insert(my_list, key)
    my_list.insert(index, key)
    print ("Elemen", key , "Tidak Ditemukan. Maka Disisipkan di Index",index," Sehingga Menjadi ", my_list)