#Terdapat daftar bilangan [7, 10, 13, 6, 17, 22, 19]. 
# Temukan bilangan prima dalam daftar 
#tersebut menggunakan sequential search.

def sequential_search_prime (data):
    prime = []
    for item in data :
        x = 1
        for i in range (2, item) :
            if item % i == 0 :
                x = 0
                break
        if x == 1 :
            prime.append(item)
    return prime
            
my_list = [7, 10, 13, 6, 17, 22, 19]
prime = sequential_search_prime(my_list)
print (f"Bilangan Prima dari List Yaitu : ", prime)

