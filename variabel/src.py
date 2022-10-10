# variabel
a ="Dadi Yusuf"
def func():
    a = "dadi"
    print ("selamat " + a)
func()
print(a)
# Definisi
def tambah():
    a = 5
    b = 3
    c = a+b
    print(c)
tambah()
# Definisi Parameter
def data(nama,nim):
    print(f"nama saya {nama} dan nim saya {nim}")
data("Dadi","123")
# Contoh
def data(sisi):
    return(sisi*sisi)
print(data(2))
def total(alas,tinggi):
    return(0.5*alas*tinggi)
print(total(2,5))