#John, Jane, Michael, dan Emily adalah empat teman yang tinggal dalam satu kompleks 
#perumahan. Mereka memiliki nomor telepon masing-masing yang tersimpan dalam buku
#telepon. John sering kali lupa menyimpan nomor telepon teman-temannya dan sering kali 
#harus meminta nomornya lagi. Kali ini, John ingin mencari nomor telepon Jane. 
#Berdasarkan tabel buku telepon berikut:
#John Doe 081234567890
#Jane Smith 089876543210
#Michael Johnson 087811223344
#Emily Davis 082122232425
#Bantulah John untuk menemukan nomor telepon Jane menggunakan sequential search

def if_sama (phone_books, nama) :

    for phone in phone_books.values() :
        title1 = nama
        title2 = phone['name']
        if title1 in title2 :
            return phone['number']
    return None


phone_books = { 'no1' : {'name' : 'John Doe' , 'number' : '081234567890'},
                'no2' : {'name' : 'Jane Smith' , 'number' : '089876543210'},
                'no3' : {'name' : 'Michael Johnson' , 'number' : '087811223344'},
                'no4' : {'name' : 'Emily Davis' , 'number' : '082122232425'}
            }

nama = "Jane"
phone_number = if_sama(phone_books, nama)
if phone_number :
    print ("Jane Number is : ", phone_number)
else :
    print ("No Number")
