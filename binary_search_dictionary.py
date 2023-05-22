#Rani adalah seorang siswa yang rajin belajar dan sangat tertarik dengan kamus. Suatu hari, 
#Rani menemukan kamus ajaib di perpustakaan sekolahnya. Kamus tersebut memiliki 
#kemampuan untuk langsung memberikan definisi kata yang dicari. Rani ingin mencoba 
#keajaiban kamus tersebut dengan mencari definisi kata yang diinginkan. Berdasarkan 
#kamus ajaib di bawah ini, temukan definisi kata menggunakan binary search
#Apple = Buah Apel
#Banana = Buah Pisang
#Cat = Kucing
#Duck = Bebek
#Elephant = Gajah

def binary_search_kamus(kata, kamus):
    low = 0
    high = len(kamus) - 1

    while low <= high:
        mid = (low + high) // 2
        if kamus[mid][0] == kata:
            return kamus[mid][1]
        elif kamus[mid][0] < kata:
            low = mid + 1
        else:
            high = mid - 1

    return "Kata tidak ditemukan dalam kamus."

kamus_ajaib = [
    ("Apple", "Buah Apel"),
    ("Banana", "Buah Pisang"),
    ("Cat", "Kucing"),
    ("Duck", "Bebek"),
    ("Elephant", "Gajah")
]

kata_dicari = input ("Cari Kata : ")
definisi = binary_search_kamus(kata_dicari, kamus_ajaib)
print("Definisi kata", kata_dicari, "adalah:", definisi)