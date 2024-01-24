max = 500


# Structure of Employee
class employee:
    def __init__(self):
        self.name = ''
        self.code = 0
        self.designation = ''
        self.exp = 0
        self.age = 0


num = 0
emp = [employee() for i in range(max)]
tempemp = [employee() for i in range(max)]
sortemp = [employee() for i in range(max)]
sortemp1 = [employee() for i in range(max)]


# Function to build the given datatype
def build():
    global num, emp

    print("Birden çok kişi gir")
    print("Maksimum: ", max)

    num = int(input("Giriş Sayısı: "))

    if num > max:
        print("Giriş sayısı en fazla 500 olabilir")
        num = 500

    print("Aşağıdaki bilgileri girin")
    for i in range(num):
        emp[i].name = input("İsim-Soyisim: ")
        emp[i].code = int(input("TC No.: "))
        emp[i].designation = input("Designation: ")
        emp[i].exp = int(input("Experience: "))
        emp[i].age = int(input("Yaş: "))

    showMenu()


# Function to insert the data into
# given data type
def insert():
    global num, emp

    if num < max:
        i = num
        num += 1

        print("Öğrenci bilgilerini gir")
        emp[i].name = input("İsim-Soyisim: ")
        emp[i].code = int(input("TC No.: "))
        emp[i].designation = input("Designation: ")
        emp[i].exp = int(input("Experience: "))
        emp[i].age = int(input("Yaş: "))
    else:
        print("Maksimum öğrenci sayısına ulaşıldı")

    showMenu()


# Function to delete record at index i
def deleteIndex(i):
    global num, emp

    for j in range(i, num - 1):
        emp[j].name = emp[j + 1].name
        emp[j].code = emp[j + 1].code
        emp[j].designation = emp[j + 1].designation
        emp[j].exp = emp[j + 1].exp
        emp[j].age = emp[j + 1].age


# Function to delete record
def deleteRecord():
    global num, emp

    code = int(input("Öğrenci silmek için TC No. girin "))

    for i in range(num):
        if emp[i].code == code:
            deleteIndex(i)
            num -= 1
            break

    showMenu()


def searchRecord():
    global num, emp

    code = int(input("Öğrenci sorgulamak için TC No. girin "))

    for i in range(num):
        # If the data is found
        if emp[i].code == code:
            print("Ad-Soyad", emp[i].name)
            print("TC No.: ", emp[i].code)
            print("Designation:", emp[i].designation)
            print("Experience:", emp[i].exp)
            print("Yaş", emp[i].age)
            break

    showMenu()


# Function to show menu
def showMenu():
    print("-------------------------Mezunlar Platformu-------------------------\n")
    print("Seçenekler:\n")
    print("Birden çok kişi gir (1)")
    print("Yeni kişi gir (2)")
    print("Öğrenci sil	 (3)")
    print("Öğrenci ara	 (4)")
    print("Çıkış			 (5)")

    # Input Options
    option = int(input())

    # Call
    if option == 1:
        build()
    elif option == 2:
        insert()
    elif option == 3:
        deleteRecord()
    elif option == 4:
        searchRecord()
    elif option == 5:
        return
    else:
        print("Expected Options")
        print("are 1/2/3/4/5")
        showMenu()


# Driver code
showMenu()
