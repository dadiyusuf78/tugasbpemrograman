import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=23306,
  user="root",
  password="p455w0rd",
  database="basis_data"
)

def menu():
    print("Pilihan")
    print("1. Tampil Data")
    print("2. Insert Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Exit")

def welcome():
    nim = 20220801132
    nama = "Dadi Yusuf"
    print ("NIM : ", nim)
    print ("NAMA : ", nama)

def tampil():
    db = mydb.cursor()
    db.execute("SELECT * FROM students")
    res = db.fetchall()
    for x in res:
        print(x)

def insert():
    nama = str(input("Nama : "))
    nim = int(input("NIM : "))
    db = mydb.cursor()
    sql = "INSERT INTO students (name, nim) VALUES (%s, %s)"
    val = (nama, nim)
    db.execute(sql, val)
    mydb.commit()
    print(db.rowcount, "berhasil insert")

def update():
    nim = int(input("NIM Baru : "))
    id = int(input("ID Mahasiswa : "))
    db = mydb.cursor()
    sql = "UPDATE students SET nim = %s WHERE id = %s"
    val = (nim, id)
    db.execute(sql, val)
    mydb.commit()
    print(db.rowcount, "berhasil update")

def delete():
    id = int(input("ID Mahasiswa : "))
    db = mydb.cursor()
    sql = "DELETE FROM students WHERE id = %s"
    val = (id, )
    db.execute(sql, val)
    mydb.commit()
    print(db.rowcount, "berhasil dihapus")

while True:
    welcome()
    menu()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        tampil()
    elif pil == 2:
        insert()
    elif pil == 3:
        update()
    elif pil == 4:
        delete()
    elif pil == 5:
        break
    else:
        print ("pilihan salah")