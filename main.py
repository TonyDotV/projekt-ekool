class School:
   def __init__(self):
      pass

class Student: # õpilaste andmed
   def __init__(self, nimi, kursus):
      self.nimi=nimi
      self.kursus=kursus
      self.hinded = []

   def lisa_hinne(self, aine, hinne):
      hinne = float(hinne)
      self.hinded.append((aine, hinne))

   def keskmine(self):
      if len(self.hinded) == 0:
         return None
      
      summa = 0
      arv = 0
      for aine, hinne in self.hinded:
         summa += hinne
         arv += 1
      return summa / arv
   
   def keskmine_aine_kaupa(self):
      if len(self.hinded) == 0:
         return {}
      
      aine_map = {}

      # kogume hinded aine kaupa
      for aine, hinne in self.hinded:
         if aine not in aine_map:
            aine_map[aine] = []
         aine_map[aine].append(hinne)

      # arvutame iga aine keskmise hinde
      aine_keskmised = {}
      for aine in aine_map:
         summa = 0
         arv = 0
         for hinne in aine_map[aine]:
            summa += hinne
            arv += 1
         aine_keskmised[aine] = summa / arv
      return aine_keskmised

   def __str__(self):
      return f"{self.nimi}, {self.kursus}"
   
class StudentList: # õpilaste nimekirja välja toomiseks
   def __init__(self):
      self.arr = []

   def addStudent(self, student):
      self.arr.append(student)

   def displayInfo(self):
      for s in self.arr:
         print(s)

   def find_by_name(self, nimi):
      for s in self.arr:
         if s.nimi == nimi:
            return s
      return None
   
   def display_grades(self, nimi):
      student = self.find_by_name(nimi)
      if student is None:
         print("Õpilast sellise nimega ei leitud.")
         return
      if not student.hinded:
         print(f"{student.nimi} hinnetelehte ei ole.")
         return
      
      print(f"\nHinded õpilasele {student.nimi}: ")
      for aine, hinne in student.hinded:
         print(f"{aine}: {hinne}")

class Teacher: 
   def __init__(self, nimi, kursused):
      self.nimi=nimi
      self.kursused=kursused

   def __str__(self):
      return f"{self.nimi}, {self.kursused}"
   
class TeacherList: # õpetajate nimekirja välja toomiseks
   def __init__(self):
      self.arr = []

   def addTeacher(self, teacher):
      self.arr.append(teacher)

   def displayInfo(self):
      for t in self.arr:
         print(t)

class User:
   def __init__(self, username, password, role):
      self.username = username
      self.password = password
      self.role = role # õpilane, õpetaja või admin

class LoginSystem: 
   def __init__(self):                 # KASUTAJANIMED JA PAROOLID TESTIMISEKS
      self.users = {
         'opilane1': User('opilane1', 'pass123', 'student'),
         'õpetaja1': User('õpetaja1', 'teach123', 'teacher'),
         'admin': User('admin', 'admin123', 'admin')
      }
      self.current_user = None

   def login(self): # Sisselogimissüsteem
      attempts = 3
      while attempts > 0:
         username = input("Kasutajanimi: ")
         password = input("Parool: ")

         if username in self.users and self.users[username].password == password:
            self.current_user = self.users[username]
            print(f"\nEdukalt sisselogitud kui {self.current_user.role}!")
            return True
         else:
            attempts -= 1
            if attempts > 0:
               print(f"Vale kasutajanimi või parool. Sul on {attempts} katset alles.\n")
            else:
               print("Liiga palju ebaõnnestunud katseid.")
      return False
   
   def logout(self): # välja logimissüsteem
      print(f"\n{self.current_user.username} logiti välja.")
      self.current_user = None

   def register_user(self, username, password, role): # uue kasutaja registreerimissüsteem
      """Admin saab registreerida uusi kasutajaid"""
      if username in self.users:
         print("See kasutajanimi on juba olemas.")
         return False
      self.users[username] = User(username, password, role)
      print(f"Kasutaja {username} registreeriti kui {role}.")
      return True
   
# Menüü
def student_menu(login_system, student_list): # õpilase valikud
   while True:
      print("\n--- ÕPILASE MENÜÜ ---")
      print("1. Vaata õpilaste nimekirja")
      print("2. Logi välja")
      choice = input("Vali tegevus: ")

      if choice == '1':
         student_list.displayInfo()
      elif choice == '2':
         login_system.logout()
         break
      else:
         print("Vale valik!")

def teacher_menu(login_system, student_list, teacher_list): # õpetaja valikud
   while True:
      print("\n--- ÕPETAJA MENÜÜ ---")
      print("1. Vaata õpilaste nimekirja")
      print("2. Vaata õpetajate nimekirja")
      print("3. Vaata õpilase hindeid")
      print("4. Lisa õpilasele hinne")
      print("5. Vaata õpilase keskmist hinnet")
      print("6. Logi välja")
      choice = input("Vali tegevus: ")

      if choice == '1':
         student_list.displayInfo()
      elif choice == '2':
         teacher_list.displayInfo()
      elif choice == '3': # ajutine, lisan hiljem
         nimi = input("Sisesta õpilase täisnimi: ")
         student_list.display_grades(nimi)
      elif choice == '4': # ajutine, lisan hiljem
         nimi = input("Õpilase täisnimi: ")
         student = student_list.find_by_name(nimi)
         if student is None:
            print("Õpilast sellise nimega ei leitud.")
         else:
            aine = input("Aine: ")
            hinne = input("Hinne: ")
            student.lisa_hinne(aine, hinne)
            print("Hinne lisatud!")
      elif choice == '5':
         nimi = input("Sisesta õpilase täisnimi: ")
         student = student_list.find_by_name(nimi)
         if student is None:
            print("Õpilast sellise nimega ei leitud.")
         else:
            avg = student.keskmine()
            if avg is None:
               print("Õpilasel ei ole veel hindeid")
            else:
               print(f"Õpilase {student.nimi} üldine keskmine hinne: {avg:.2f}")
               # vaata keskmist hinnet aine kaupa
               aine_keskmised = student.keskmine_aine_kaupa()
               print("Keskmised hinded aine kaupa: ")
               for aine, k in aine_keskmised.items():
                  print(f"{aine}: {k:.2f}")
      elif choice == '6':
         login_system.logout()
         break
      else:
         print("Vale valik!")

def admin_menu(login_system, student_list, teacher_list): # admini valikud
   while True:
      print("\n--- ADMINI MENÜÜ ---")
      print("1. Vaata õpilaste nimekirja")
      print("2. Lisa uus õpilane")
      print("3. Vaata õpetajate nimekirja")
      print("4. Lisa uus õpetaja")
      print("5. Registreeri uus kasutaja")
      print("6. Logi välja")
      choice = input("Vali tegevus: ")

      if choice == '1':
         student_list.displayInfo()
      elif choice == '2':
         nimi = input("Õpilase nimi: ")
         kursus = input("Kursus: ")
         student_list.addStudent(Student(nimi, kursus))
         print("Õpilane lisatud!")
      elif choice == '3':
         teacher_list.displayInfo()
      elif choice == '4':
         nimi = input("Õpetaja nimi: ")
         kursused = input("Kursused (komaga eraldatud): ")
         teacher_list.addTeacher(Teacher(nimi, kursused))
         print("Õpetaja lisatud!")
      elif choice == '5':
         username = input("Uus kasutajanimi: ")
         password = input("Parool: ")
         role = input("Roll(õpilane, õpetaja): ")
         login_system.register_user(username, password, role)
      elif choice == '6':
         login_system.logout()
         break
      else:
         print("Vale valik!")

def main():
   login_system = LoginSystem()
   student_list = StudentList()
   teacher_list = TeacherList()

   # Ajutised andmed
   student_list.addStudent(Student("Mari Maasikas", "10A"))
   student_list.addStudent(Student("Jaan Tamm", "10B"))
   teacher_list.addTeacher(Teacher("Kalle Kask", "Matemaatika, Füüsika"))

   print("--- KOOLI SÜSTEEM ---")

   while True:
      if login_system.login():
         role = login_system.current_user.role
         
         if role == 'student':
            student_menu(login_system, student_list)
         elif role == 'teacher':
            teacher_menu(login_system, student_list, teacher_list)
         elif role == 'admin':
            admin_menu(login_system, student_list, teacher_list)
      
      retry = input("\nKas soovid uuesti sisse logida? (jah/ei): ")
      if retry.lower() != 'jah':
         print("Head aega!")
         break

if __name__ == "__main__":
   main()