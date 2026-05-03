import tkinter as tk
from tkinter import ttk, messagebox
import re

# Baas klassid

class Student:
   '''hoiab õpilase nime, kursuse ja hinnetelehte, mis on aine-hinne enniku/tuple list. 
   Võimaldab lisada hindeid, arvutada keskmist ja keskmist aine kaupa'''
   def __init__(self, nimi, kursus):
      self.nimi=nimi
      self.kursus=kursus
      kursus = kursus.strip().upper() # kursuse nimi suurtähed ja ilma tühikuteta, et oleks ühtne ja lihtsam otsida
      if not re.fullmatch(r"(1[0-2]|[1-9])[A-Z]", kursus): # kontroll, et kursus oleks kehtivas formaadis, nt 10A, 11B, 9C jne
         raise ValueError("Kursus peab olema vormingus '10A', '11B' jne.")
      self.hinded = []

   def lisa_hinne(self, aine, hinne):
      '''lisab aine ja hinne tuple'ina hinnetelehte, hinne peab olema vahemikus 1 kuni 5
      Kui hinne pole kehtiv, tõstab ValueErrori'''
      hinne = float(hinne)
      if 1 <= hinne <= 5:  # kehtiv hinne peab olema vahemikus 1 kuni 5
         self.hinded.append((aine, hinne))
      else:
         raise ValueError("Hinne peab olema vahemikus 1 kuni 5.")

   def keskmine(self):
      '''tagastab kõigi hinnete keskmise, kui hinneteleht on tühi, tagastab None'''
      if len(self.hinded) == 0:
         return None
      summa = 0
      arv = 0
      for aine, hinne in self.hinded:
         summa += hinne
         arv += 1
      return summa / arv

   def keskmine_aine_kaupa(self):
      '''tagastab sõnastiku, kus võtmed on ainete nimed ja väärtused nende keskmised hinded. Kui hinnetelehte pole, tagastab tühja sõnastiku'''
      if len(self.hinded) == 0:
         return {}
      aine_map = {}
      for aine, hinne in self.hinded:
         if aine not in aine_map:
            aine_map[aine] = []
         aine_map[aine].append(hinne)
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
      '''tagastab õpilase nime ja kursuse'''
      return f"{self.nimi}, {self.kursus}"


class StudentList:
   '''hoiab õpilaste nimekirja, võimaldab lisada, kuvada, otsida ja kustutada õpilasi nime järgi. Otsing on case-insensitive ja ignoreerib ees- ja lõputühikud'''
   def __init__(self):
      self.arr = []

   def addStudent(self, student):
      '''lisab õpilase nimekirja, õpilane on Student klassi objekt, millel on nimi, kursus ja hinneteleht'''
      self.arr.append(student)

   def displayInfo(self):
      '''kuvab kõik õpilased koos nende kursustega'''
      for s in self.arr:
         print(s)

   def find_by_name(self, nimi):
      '''leiab õpilase nime järgi, tagastab Student objekti, kui leiti, või None, kui õpilast ei leitud. Otsing on case-insensitive ja ignoreerib ees- ja lõputühikud'''
      if nimi is None:
         return None
      nimi = nimi.strip().lower()
      for s in self.arr:
            if s.nimi.strip().lower() == nimi:
               return s
      return None

   def remove_by_name(self, nimi):
      '''kustutab õpilase nime järgi, tagastab True, kui kustutamine õnnestus, False, kui õpilast ei leitud'''
      student = self.find_by_name(nimi)
      if student is not None:
         self.arr.remove(student)
         return True
      return False

   def display_grades(self, nimi): 
      '''leiab õpilase nime järgi ja kuvab tema hinded, kui õpilane või hinneteleht puudub, annab sellest teada'''
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
   '''hoiab õpetaja nime ja kursused, mida ta õpetab'''
   def __init__(self, nimi, kursused):
      self.nimi=nimi
      self.kursused=kursused

   def __str__(self):
      '''tagastab õpetaja nime ja kursused, mida ta õpetab'''
      return f"{self.nimi}, {self.kursused}"


class TeacherList: 
   '''hoiab õpetajate nimekirja, võimaldab lisada, kuvada, otsida ja kustutada õpetajaid nime järgi. Otsing on case-insensitive ja ignoreerib ees- ja lõputühikud'''
   def __init__(self):
      self.arr = []

   def addTeacher(self, teacher): 
      '''lisab õpetaja nimekirja, õpetaja on Teacher klassi objekt, millel on nimi ja kursused'''
      self.arr.append(teacher)

   def displayInfo(self): 
      '''kuvab kõik õpetajad koos nende kursustega'''
      for t in self.arr:
         print(t)

   def find_by_name(self, nimi): 
      '''leiab õpetaja nime järgi, tagastab Teacher objekti, kui leiti, või None, kui õpetajat ei leitud. Otsing on case-insensitive ja ignoreerib ees- ja lõputühikud'''
      if nimi is None:
         return None
      nimi = nimi.strip().lower()
      for t in self.arr:
         if t.nimi.strip().lower() == nimi:
            return t
      return None

   def remove_by_name(self, nimi): 
      '''kustutab õpetaja nime järgi, tagastab True, kui kustutamine õnnestus, False, kui õpetajat ei leitud'''
      teacher = self.find_by_name(nimi)
      if teacher is not None:
         self.arr.remove(teacher)
         return True
      return False


class User: 
   '''lihtne kasutajaklass, mis hoiab kasutajanime, parooli, rolli (student, teacher, admin) ja täisnime'''
   def __init__(self, username, password, role, full_name=None):
      self.username = username
      self.password = password
      self.role = role
      self.full_name = full_name


class LoginSystem: 
   '''lihtne loginisüsteem, mis hoiab kasutajaid sõnastikus ja võimaldab registreerida, kustutada, sisse- ja välja logida'''
   def __init__(self):
      self.users = {
         'opilane1': User('opilane1', 'pass123', 'student', 'Mari Maasikas'),
         'õpetaja1': User('õpetaja1', 'teach123', 'teacher'),
         'admin': User('admin', 'admin123', 'admin')
      }
      self.current_user = None
      '''registreerib uue kasutaja, kui kasutajanimi pole juba olemas. Roll peab olema "student", "teacher" või "admin". Admini rolliga kasutaja ei saa kustutada ega muuta teisi kasutajaid'''
      def register_user(self, username, password, role, full_name=None): 
         if username in self.users:
            print("See kasutajanimi on juba olemas.")
            return False

   def delete_user(self, username): 
      '''kustutab kasutaja, kui see pole admin ja kasutajanimi on olemas'''
      if username not in self.users:
         print("Kasutajat ei leitud.")
         return None
      if username == "admin":
         print("Admin kasutajat ei saa kustutada")
         return None
      removed_user = self.users.pop(username, None)
      print(f"Kasutaja {username} kustutatud.")
      return removed_user

   def login(self, username, password): 
      '''kontrollib, kas kasutajanimi ja parool klapivad, kui jah, siis salvestab current_useri ja tagastab True, kui ei, tagastab False'''
      if username in self.users and self.users[username].password == password:
         self.current_user = self.users[username]
         return True
      return False

   def logout(self): 
      '''logib välja ja tühjendab current_useri, et saaks kontrollida, kas keegi on sisse logitud'''
      print(f"\n{self.current_user.username} logiti välja.")
      self.current_user = None

   def register_user(self, username, password, role, full_name=None): 
      '''registreerib uue kasutaja, kui kasutajanimi pole juba olemas. Roll peab olema "student", "teacher" või "admin". Admini rolliga kasutaja ei saa kustutada ega muuta teisi kasutajaid'''
      if username in self.users:
         print("See kasutajanimi on juba olemas.")
         return False
      self.users[username] = User(username, password, role, full_name)
      print(f"Kasutaja {username} registreeriti kui {role}.")
      return True


# Tkinter GUI

class App(tk.Tk):
   '''peamine rakendus, mis hoiab loginisüsteemi, õpilaste ja õpetajate nimekirju ning 
   võimaldab vahetada erinevate frame'ide vahel (LoginFrame, StudentFrame, TeacherFrame, AdminFrame)'''
   def __init__(self):
      super().__init__()
      self.title("Kooli Süsteem")
      self.resizable(False, False)
      self.configure(bg="#f7f6f2")

      # ajutine andmebaas ja loginisüsteem, et saaks rakendust testida
      self.login_system = LoginSystem()
      self.student_list = StudentList()
      self.teacher_list = TeacherList()
      self.student_list.addStudent(Student("Mari Maasikas", "10A"))
      self.student_list.addStudent(Student("Jaan Tamm", "10B"))
      self.teacher_list.addTeacher(Teacher("Kalle Kask", "Matemaatika, Füüsika"))

      self.attempts = 3 # sisselogimiskatsete arv, kui jõuab 0-ni, programm sulgub, et vältida jõhkrat sisselogimisrünnakut

      # värvipalett
      self.BG       = "#f7f6f2"
      self.SURFACE  = "#f9f8f5"
      self.BORDER   = "#d4d1ca"
      self.TEXT     = "#28251d"
      self.MUTED    = "#7a7974"
      self.PRIMARY  = "#01696f"
      self.PRI_HL   = "#cedcd8"
      self.ERROR    = "#A5001B"
      self.SUCCESS  = "#437a22"

      self.configure(bg=self.BG) # rakenduse taustavärv
      self._build_styles() # rakenduse stiilid, eriti tabelite jaoks, et need näeksid moodne ja ühtne välja

      # konteiner mis hoiab kõiki raame (LoginFrame, StudentFrame, TeacherFrame, AdminFrame) ja võimaldab nende vahel vahetada
      container = tk.Frame(self, bg=self.BG)
      container.pack(fill="both", expand=True) # täidab kogu akna, et frame'id saaksid kasutada kogu ruumi

      self.frames = {} # sõnastik, mis hoiab kõiki raame klassi järgi, nt self.frames[LoginFrame] annab LoginFrame'i isendi
      for F in (LoginFrame, StudentFrame, TeacherFrame, AdminFrame):
         frame = F(container, self)
         self.frames[F] = frame
         frame.grid(row=0, column=0, sticky="nsew")

      self.show_frame(LoginFrame) # näitab esialgu LoginFrame'i, kui rakendus käivitatakse

   def _build_styles(self): # popup tabelid (hinded, loendid)
      style = ttk.Style(self)
      style.theme_use("clam") # täielik kontroll värvide üle
      style.configure("Treeview",   # tabeli stiil
         background=self.SURFACE, foreground=self.TEXT,      # rea tausta värvid
         fieldbackground=self.SURFACE, rowheight=26,     # taust ja ridade kõrgus
         font=("Segoe UI", 10)) # veerupäise kirjastiil
      style.configure("Treeview.Heading", # veerupäise stiil
         background=self.BG, foreground=self.MUTED, # veerupäise taust ja tekst. self.muted = helehall, et eristuks veerupäisest
         font=("Segoe UI", 9, "bold"))   
      style.map("Treeview", background=[("selected", self.PRI_HL)], # valikurea taust, self.pri_hl = hele sinakasroheline, et eristuks tavalistest ridadest
                foreground=[("selected", self.PRIMARY)])

   def show_frame(self, frame_class): # näitab soovitud frame'i ja kutsub selle on_show() meetodi, kui see on olemas
      frame = self.frames[frame_class]
      if hasattr(frame, "on_show"): # 
         frame.on_show()
      frame.tkraise()


# kasutlikud funktsioonid, et luua ühtse stiiliga tkinteri elemente (nupud, sildid, sisestuskastid)

def make_label(parent, text, size=10, bold=False, color=None, bg=None):
   ''' lihtsustab ühtse stiiliga siltide loomist, võtab parameetritena vanema elemendi, teksti, suuruse, paksu fondi, teksti värvi ja taustavärvi ning tagastab tk.Labeli '''
   font = ("Segoe UI", size, "bold" if bold else "normal")
   kw = {"text": text, "font": font, "bg": bg or parent.cget("bg")} # kui taustavärv pole määratud, võtab vanema taustavärvi, et sildid sulanduksid sujuvalt taustaga
   if color:
      kw["fg"] = color
   return tk.Label(parent, **kw) 

def make_entry(parent, show=None, width=28):  
   '''sama, aga sisestuskastide jaoks. show parameeter võimaldab peita sisestatud teksti (nt paroolide puhul), width määrab kastide laiuse'''
   e = tk.Entry(parent, show=show, width=width,
                relief="flat", bd=0, # ilma raamita, et näeks moodne ja minimalistlik välja
                font=("Segoe UI", 10),
                bg="#ffffff", fg="#28251d", 
                insertbackground="#28251d", # kursori värv, et eristuks taustast
                highlightthickness=1,  # pehme raam ümber kastide, et eristuks taustast
                highlightbackground="#d4d1ca",
                highlightcolor="#01696f")
   return e

def make_button(parent, text, command, color="#01696f", fg="#ffffff", width=20): 
   '''ühtse stiiliga nuppude loomine, command on funktsioon, mis käivitatakse nupuvajutusega, color ja fg määravad tausta- ja tekstivärvi, width määrab nupu laiuse'''
   return tk.Button(parent, text=text, command=command,
                    font=("Segoe UI", 10, "bold"),
                    bg=color, fg=fg, activebackground=color, 
                    activeforeground=fg,  #  nupu värvid, kui hiirega üle lähed või vajutad
                    relief="flat", bd=0, padx=12, pady=6,
                    cursor="hand2", width=width)  # käepärane funktsioon ühtse stiiliga nuppude loomiseks

def popup_table(parent_app, title, columns, rows, col_widths=None):
   '''tabeli popupi funktsioon, mida kasutatakse hindeid ja nimekirju kuvavate akende jaoks. Võtab parameetritena vanema rakenduse, akna pealkirja, veerunimed, ridade andmed ja veergude laiused'''
   win = tk.Toplevel(parent_app)
   win.title(title)
   win.configure(bg=parent_app.BG)
   win.grab_set()
   win.resizable(False, False)
   tree = ttk.Treeview(win, columns=columns, show="headings", height=min(len(rows)+1, 14))
   '''show="headings" peidab vaikimisi veerunimedega kaasneva tühja veeru, height määrab maksimaalse ridade arvu, mida korraga näidatakse (lisame 1, et mahutada ka veerupäis)'''
   for i, col in enumerate(columns):
      w = col_widths[i] if col_widths else 160
      tree.heading(col, text=col)
      tree.column(col, width=w, anchor="w")

   for row in rows: # lisab tabelisse read, iga row on tuple, mis vastab veergudele
      tree.insert("", "end", values=row)

   if not rows: # kui ridu pole, lisab ühe tühja rea, et tabeli struktuur oleks nähtav ja kasutaja mõistaks, et andmeid pole
      tree.insert("", "end", values=("(tühi)",) + ("",) * (len(columns)-1))

   scrollbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview) # vertikaalne kerimisriba, mis on seotud tabeli yview-ga, et kerimine toimiks sujuvalt
   tree.configure(yscroll=scrollbar.set) # seob tabeli kerimisriba funktsiooniga, et kerimisriba saaks tabeli kerimist kontrollida
   tree.pack(side="left", fill="both", expand=True, padx=(10,0), pady=10) # tabel täidab kogu akna, kerimisriba on tabeli kõrval, padx ja pady lisavad veidi ruumi, et tabel ei oleks akna servadega kokku surutud
   scrollbar.pack(side="left", fill="y", pady=10, padx=(0,10))

   make_button(win, "Sulge", win.destroy, width=10).pack(pady=(0,10)) # nupp tabeli sulgemiseks, mis on eraldi kerimisriba ja tabeli alt, et oleks selgelt nähtav ja kasutajasõbralik


# Sisselogimiseraam

class LoginFrame(tk.Frame):
   '''sisselogimisraam, mis võimaldab kasutajal sisestada oma kasutajanime ja parooli ning proovida sisse logida.
   Kui sisselogimine õnnestub, suunatakse kasutaja tema rollile vastavale menüüle (õpilane, õpetaja, admin).
   Kui sisselogimine ebaõnnestub, näidatakse veateadet ja vähendatakse katsete arvu.
   Kui katseid on liiga palju, programm sulgub turvakaalutlustel'''
   def __init__(self, parent, app):
      '''konstruktor, mis kutsub üles _build() meetodi, et luua sisselogimisraami elemendid'''
      super().__init__(parent, bg=app.BG)
      self.app = app
      self._build()

   def _build(self):
      '''meetod, mis loob sisselogimisraami elemendid: pealise, sisestuskastid, nupud ja veateate sildi'''
      app = self.app
      # outer card
      card = tk.Frame(self, bg=app.SURFACE, bd=1, relief="flat",
                      highlightthickness=1, highlightbackground=app.BORDER)
      card.pack(padx=60, pady=50, fill="both", expand=True)

      make_label(card, "Kooli Süsteem", size=18, bold=True, color=app.PRIMARY).pack(pady=(30,4)) # pealise sildi loomine, mis on suurem, paksu fondiga ja erivärviga, et see paistaks silma ja annaks kohe teada, mis rakendus see on
      make_label(card, "Logi sisse oma kontoga", size=10, color=app.MUTED).pack(pady=(0,20)) # alapealdise sildi loomine, mis on väiksem, heledama värviga ja annab kasutajale vihjeid, mida teha

      self.alert_var = tk.StringVar() # muutuja, mis hoiab veateate teksti, kui sisselogimine ebaõnnestub, alguses tühi
      self.alert_lbl = tk.Label(card, textvariable=self.alert_var, # veateate sildi loomine, mis on punase tekstiga, et eristuks tavalisest tekstist ja tõmbaks tähelepanu, wraplength ja justify tagavad, et pikad veateated jagatakse mitmele reale ja on loetavad
                                font=("Segoe UI", 9), bg="#e0ced7", fg=app.ERROR,
                                wraplength=280, justify="left", padx=8, pady=4)

      form = tk.Frame(card, bg=app.SURFACE) # raam, mis hoiab sisselogimisvormi elemente (sildid ja sisestuskastid), et neid saaks ühtse stiiliga grupeerida ja positsioneerida
      form.pack(padx=30, pady=4)

      make_label(form, "Kasutajanimi", size=9, color=app.MUTED).grid(row=0, column=0, sticky="w", pady=(0,2)) # sisselogimisvormi sildi loomine, mis on väiksem, heledama värviga ja annab vihjeid, mida sisestada, grid meetod võimaldab täpsemat positsioneerimist vormi sees, pady lisab veidi ruumi siltide ja kastide vahele
      self.entry_user = make_entry(form) 
      self.entry_user.grid(row=1, column=0, pady=(0,12), ipady=4)

      make_label(form, "Parool", size=9, color=app.MUTED).grid(row=2, column=0, sticky="w", pady=(0,2)) # parooli sildi loomine, mis on väiksem, heledama värviga ja annab vihjeid, mida sisestada, grid meetod võimaldab täpsemat positsioneerimist vormi sees, pady lisab veidi ruumi siltide ja kastide vahele
      self.entry_pass = make_entry(form, show="•")
      self.entry_pass.grid(row=3, column=0, pady=(0,4), ipady=4)

      self.entry_pass.bind("<Return>", lambda e: self._do_login()) # nupu vajutamise asemel võimaldab kasutajal vajutada Enterit, et proovida sisse logida, mis on mugavam ja kiirem, eriti kui kasutaja on harjunud selle meetodiga

      make_button(card, "Logi sisse", self._do_login).pack(pady=12) # sisselogimisnupu loomine, mis on erivärviga, et eristuks tavalisest tekstist ja tõmbaks tähelepanu, command on _do_login meetod, mis käivitatakse nupuvajutusega
      make_label(card, "", size=8).pack(pady=(0,24))  # spacer

   def _do_login(self):
      '''meetod, mis proovib kasutaja sisestatud andmetega sisse logida,
      kui õnnestub, suunab vastavalt rollile õigesse menüüsse,
      kui ebaõnnestub, näitab veateadet ja vähendab katsete arvu'''
      app = self.app
      u = self.entry_user.get().strip()
      p = self.entry_pass.get()

      if app.login_system.login(u, p):
         '''sisselogimine õnnestus, resetib katsete arvu, tühjendab sisestuskastid,
         peidab veateate sildi ja suunab kasutaja tema rollile vastavale menüüle'''
         app.attempts = 3
         self.entry_user.delete(0, "end")
         self.entry_pass.delete(0, "end")
         self.alert_lbl.pack_forget()
         self.alert_var.set("")

         role = app.login_system.current_user.role
         '''suunab kasutaja tema rollile vastavale menüüle, kui roll on "student", näitab StudentFrame-i,
         kui "teacher", näitab TeacherFrame-i, kui "admin", näitab AdminFrame-i'''
         if role == "student":
            app.show_frame(StudentFrame)
         elif role == "teacher":
            app.show_frame(TeacherFrame)
         elif role == "admin":
            app.show_frame(AdminFrame)
      else:
         app.attempts -= 1
         if app.attempts <= 0:
            messagebox.showerror("Blokeeritud", "Liiga palju ebaõnnestunud katseid. Programm sulgub.")
            app.destroy()
            return
         self.alert_var.set(f"Vale kasutajanimi või parool. Sul on {app.attempts} katset alles.")
         self.alert_lbl.pack(padx=30, pady=(0,8))


# Õpilaseraam

class StudentFrame(tk.Frame):
   '''õpilaseraam, mis võimaldab õpilasel vaadata oma hindeid, aine keskmist ja kõigi ainete keskmisi.
   Samuti on siin nupud, et logida välja ja suunata tagasi sisselogimisraamile'''
   def __init__(self, parent, app):
      super().__init__(parent, bg=app.BG)
      self.app = app
      self._build()

   def on_show(self):
      '''meetod, mis täidetakse iga kord, kui see raam näidatakse, siin kasutatakse seda, et kuvada sisselogitud kasutaja nime,
      et õpilane teaks, et ta on sisse logitud ja kelle kontoga ta töötab'''
      name = self.app.login_system.current_user.full_name or self.app.login_system.current_user.username
      self.name_var.set(f"Sisselogitud: {name}")

   def _build(self):
      '''meetod, mis loob õpilaseraami elemendid: päis, nupud ja funktsioonid, mis käivituvad nupuvajutustega'''
      app = self.app

      header = tk.Frame(self, bg=app.PRIMARY) # päise raam, mis hoiab menüü pealist, sisselogitud kasutaja nime ja väljalogimise nuppu, taustavärv on erivärv, et eristuks tavalisest taustast ja tõmbaks tähelepanu
      header.pack(fill="x")
      make_label(header, "Õpilase menüü", size=13, bold=True, color="#ffffff", bg=app.PRIMARY).pack(side="left", padx=20, pady=14)
      self.name_var = tk.StringVar() # muutuja, mis hoiab sisselogitud kasutaja nime, alguses tühi, täidetakse on_show() meetodis, et kuvada kasutaja nime päises
      tk.Label(header, textvariable=self.name_var, font=("Segoe UI", 9), 
         bg=app.PRIMARY, fg=app.PRI_HL).pack(side="left", padx=4)
      make_button(header, "Logi välja", self._logout, # väljalogimise nupu loomine
         color=app.PRI_HL, fg=app.PRIMARY, width=12).pack(side="right", padx=16, pady=10)

      body = tk.Frame(self, bg=app.BG) # peamine raam, mis hoiab kõiki nuppe
      body.pack(padx=30, pady=24, fill="both", expand=True)

      btns = [
         ("Vaata oma hindeid", self._show_my_grades),
         ("Aine keskmine hinne", self._subject_avg_dialog),
         ("Kõigi ainete keskmised", self._all_avgs),
      ]
      for txt, cmd in btns:
         make_button(body, txt, cmd, width=34).pack(pady=6, ipady=4)

   def _get_student(self):
      '''abimeetod, mis leiab sisselogitud kasutajaga seotud õpilase StudentListist,
      kasutades kasutaja täisnime, kui see on olemas, või kasutajanime, kui täisnime pole'''
      name = self.app.login_system.current_user.full_name
      return self.app.student_list.find_by_name(name)

   def _show_my_grades(self):
      '''meetod, mis leiab sisselogitud kasutajaga seotud õpilase ja kuvab tema hinded tabeli popupis,
      kui õpilast või hinnetelehte ei leita, annab sellest teada'''
      s = self._get_student()
      if s is None:
         messagebox.showerror("Viga", "Selle kontoga seotud õpilast ei leitud.")
         return
      if not s.hinded:
         messagebox.showinfo("Hinded", f"{s.nimi} hinnetelehte ei ole.")
         return
      popup_table(self.app, f"Hinded — {s.nimi}",
                  ("Aine", "Hinne"), s.hinded, [200, 100])

   def _subject_avg_dialog(self):
      '''meetod, mis avab dialoogi, kus õpilane saab sisestada aine nime ja näha selle aine keskmist hinnet'''
      s = self._get_student()
      if s is None:
         messagebox.showerror("Viga", "Selle kontoga seotud õpilast ei leitud."); return
      win = tk.Toplevel(self.app)
      win.title("Aine keskmine")
      win.configure(bg=self.app.BG)
      win.grab_set()
      win.resizable(False, False)
      make_label(win, "Sisesta aine nimi:", size=10).pack(padx=24, pady=(18,4), anchor="w")
      entry = make_entry(win, width=26)
      entry.pack(padx=24, pady=(0,10), ipady=4)
      result_var = tk.StringVar()
      tk.Label(win, textvariable=result_var, font=("Segoe UI", 10),
               bg=self.app.BG, fg=self.app.TEXT, wraplength=240).pack(padx=24)

      def search():
         aine = entry.get().strip()
         avgs = s.keskmine_aine_kaupa()
         if aine in avgs:
            result_var.set(f"Keskmine aines '{aine}': {avgs[aine]:.2f}")
         else:
            result_var.set("Seda ainet ei leitud.")

      make_button(win, "Otsi", search, width=12).pack(pady=10)
      make_button(win, "Sulge", win.destroy, color="#d4d1ca", fg=self.app.TEXT, width=10).pack(pady=(0,16))

   def _all_avgs(self): 
      s = self._get_student()
      if s is None:
         messagebox.showerror("Viga", "Selle kontoga seotud õpilast ei leitud."); return
      avgs = s.keskmine_aine_kaupa()
      if not avgs:
         messagebox.showinfo("Keskmised", "Sul ei ole veel hindeid."); return
      rows = [(a, f"{k:.2f}") for a, k in avgs.items()]
      popup_table(self.app, "Ainete keskmised", ("Aine", "Keskmine"), rows, [200, 100])

   def _logout(self):
      self.app.login_system.logout()
      self.app.show_frame(LoginFrame)


# ── Teacher Frame ────────────────────────────────────────────────

class TeacherFrame(tk.Frame):
   def __init__(self, parent, app):
      super().__init__(parent, bg=app.BG)
      self.app = app
      self._build()

   def _build(self):
      app = self.app

      header = tk.Frame(self, bg="#437a22")
      header.pack(fill="x")
      make_label(header, "Õpetaja menüü", size=13, bold=True, color="#ffffff", bg="#437a22").pack(side="left", padx=20, pady=14)
      make_button(header, "Logi välja", self._logout,
                  color="#d4dfcc", fg="#437a22", width=12).pack(side="right", padx=16, pady=10)

      body = tk.Frame(self, bg=app.BG)
      body.pack(padx=30, pady=24, fill="both", expand=True)

      btns = [
         ("Vaata õpilaste nimekirja",     self._student_list),
         ("Vaata õpetajate nimekirja",    self._teacher_list),
         ("Vaata õpilase hindeid",         self._view_grades_dialog),
         ("Lisa õpilasele hinne",          self._add_grade_dialog),
         ("Õpilase keskmine hinne",        self._student_avg_dialog),
      ]
      for txt, cmd in btns:
         make_button(body, txt, cmd, color="#437a22", width=34).pack(pady=6, ipady=4)

   def _student_list(self):
      rows = [(s.nimi, s.kursus) for s in self.app.student_list.arr]
      popup_table(self.app, "Õpilaste nimekiri", ("Nimi", "Kursus"), rows, [200, 120])

   def _teacher_list(self):
      rows = [(t.nimi, t.kursused) for t in self.app.teacher_list.arr]
      popup_table(self.app, "Õpetajate nimekiri", ("Nimi", "Ained"), rows, [180, 200])

   def _view_grades_dialog(self):
      self._name_search_dialog("Vaata õpilase hindeid", self._do_view_grades)

   def _do_view_grades(self, nimi, win):
      s = self.app.student_list.find_by_name(nimi)
      if s is None:
         messagebox.showerror("Viga", "Õpilast sellise nimega ei leitud.", parent=win); return
      if not s.hinded:
         messagebox.showinfo("Hinded", f"{s.nimi} hinnetelehte ei ole.", parent=win); return
      popup_table(self.app, f"Hinded — {s.nimi}", ("Aine", "Hinne"), s.hinded, [200, 100])

   def _add_grade_dialog(self): 
      '''meetod, mis avab dialoogi, kus õpetaja saab sisestada õpilase nime, aine ja hinne,
      et lisada see õpilase hinnetelehele'''
      app = self.app
      win = tk.Toplevel(app)
      win.title("Lisa hinne")
      win.configure(bg=app.BG)
      win.grab_set()
      win.resizable(False, False)

      fields = {} # sõnastik, mis hoiab sisestuskastide viiteid, et saaks hiljem nende kaudu väärtusi lugeda ja tühjendada
      for label, key in [("Õpilase täisnimi:", "nimi"), ("Aine:", "aine"), ("Hinne:", "hinne")]:
         make_label(win, label, size=9, color=app.MUTED).pack(padx=24, pady=(10,2), anchor="w")
         e = make_entry(win, width=26)
         e.pack(padx=24, ipady=4)
         fields[key] = e

      def submit(): 
         '''funktsioon, mis käivitatakse, kui õpetaja vajutab "Lisa hinne" nuppu,
         loeb sisestatud väärtused, leiab õpilase ja lisab hinne,
         kui õpilast ei leita või hinne on vigane, näitab veateadet'''
         nimi  = fields["nimi"].get().strip()
         aine  = fields["aine"].get().strip()
         hinne = fields["hinne"].get().strip()
         teacher_name = app.login_system.current_user.full_name or app.login_system.current_user.username # leiab sisselogitud õpetaja nime, et hiljem kontrollida, kas ta õpetab sisestatud ainet
         current_teacher = app.teacher_list.find_by_name(teacher_name)
         s = app.student_list.find_by_name(nimi)
         if s is None:
            messagebox.showerror("Viga", "Õpilast sellise nimega ei leitud.", parent=win); return
         try: # kontrollib, kas hinne on kehtiv ja kas õpetaja õpetab sisestatud ainet, kui jah, lisab hinne, kui ei, näitab veateadet
            s.lisa_hinne(aine, hinne)
            messagebox.showinfo("Edukas", f"Hinne {hinne} aines '{aine}' lisatud!", parent=win)
            for e in fields.values(): e.delete(0,"end")
         except ValueError as e:
            messagebox.showerror("Viga", str(e), parent=win)

      make_button(win, "Lisa hinne", submit, width=18).pack(pady=12) 
      '''nupp, mis käivitab submit funktsiooni, et lisada hinne, erivärviga, et eristuks tavalisest tekstist ja tõmbaks tähelepanu'''
      make_button(win, "Sulge", win.destroy, color="#d4d1ca", fg=app.TEXT, width=10).pack(pady=(0,16))
      '''nupp, mis sulgeb dialoogi, erivärviga, et eristuks tavalisest tekstist ja oleks selgelt nähtav'''
   def _student_avg_dialog(self):
      '''meetod, mis avab dialoogi, kus õpetaja saab sisestada õpilase nime ja näha selle õpilase keskmist hinnet ja kõigi ainete keskmisi'''
      self._name_search_dialog("Õpilase keskmine", self._do_student_avg)

   def _do_student_avg(self, nimi, win):
      '''funktsioon, mis käivitatakse, kui õpetaja vajutab "Otsi" nuppu õpilase keskmise dialoogis,
      leiab õpilase ja kuvab tema keskmise hinde ja kõigi ainete keskmised tabeli popupis'''
      s = self.app.student_list.find_by_name(nimi)
      if s is None:
         messagebox.showerror("Viga", "Õpilast sellise nimega ei leitud.", parent=win); return
      avg = s.keskmine()
      if avg is None:
         messagebox.showinfo("Keskmine", "Õpilasel ei ole veel hindeid.", parent=win); return
      avgs = s.keskmine_aine_kaupa()
      rows = [(a, f"{k:.2f}") for a, k in avgs.items()]
      popup_table(self.app, f"Keskmised — {s.nimi} (üldine: {avg:.2f})",
                  ("Aine", "Keskmine"), rows, [200, 100])

   def _name_search_dialog(self, title, callback):
      '''abimeetod, mis avab dialoogi, kus õpetaja saab sisestada õpilase nime ja seejärel käivitada callback funktsiooni,
      mis võtab nime ja dialoogi akna parameetritena'''
      app = self.app
      win = tk.Toplevel(app)
      win.title(title)
      win.configure(bg=app.BG)
      win.grab_set()
      win.resizable(False, False)
      make_label(win, "Õpilase täisnimi:", size=9, color=app.MUTED).pack(padx=24, pady=(18,2), anchor="w")
      entry = make_entry(win, width=26)
      entry.pack(padx=24, ipady=4)
      entry.bind("<Return>", lambda e: callback(entry.get().strip(), win))
      make_button(win, "Otsi", lambda: callback(entry.get().strip(), win), width=12).pack(pady=12)
      make_button(win, "Sulge", win.destroy, color="#d4d1ca", fg=app.TEXT, width=10).pack(pady=(0,16))

   def _logout(self): 
      '''meetod, mis logib kasutaja välja ja suunab tagasi sisselogimisraamile'''
      self.app.login_system.logout()
      self.app.show_frame(LoginFrame)


# Administraatori raam

class AdminFrame(tk.Frame):
   '''administraatori raam, mis võimaldab adminil vaadata õpilaste ja õpetajate nimekirju,
   registreerida uusi kasutajaid ja kustutada olemasolevaid kasutajaid.
   Samuti on siin nupud, et logida välja ja suunata tagasi sisselogimisraamile'''
   def __init__(self, parent, app):
      super().__init__(parent, bg=app.BG)
      self.app = app
      self._build()

   def _build(self):
      '''meetod, mis loob administraatori raami elemendid: päis, nupud ja funktsioonid, mis käivituvad nupuvajutustega'''
      app = self.app

      header = tk.Frame(self, bg="#A00000")
      header.pack(fill="x")
      make_label(header, "Admini menüü", size=13, bold=True, color="#ffffff", bg="#A00000").pack(side="left", padx=20, pady=14)
      make_button(header, "Logi välja", self._logout,
                  color="#e0ced7", fg="#A00000", width=12).pack(side="right", padx=16, pady=10)

      body = tk.Frame(self, bg=app.BG)
      body.pack(padx=30, pady=24, fill="both", expand=True)

      btns = [
         ("Vaata õpilaste nimekirja", self._student_list),
         ("Vaata õpetajate nimekirja", self._teacher_list),
         ("Registreeri uus kasutaja", self._register_dialog),
         ("Kustuta kasutaja", self._delete_dialog),
      ]
      for txt, cmd in btns:
         make_button(body, txt, cmd, color="#A00000", width=34).pack(pady=6, ipady=4)

   def _student_list(self):
      '''meetod, mis kogub kõikide õpilaste nimed ja kursused ning kuvab need tabeli popupis,
      et admin saaks ülevaate kõigist õpilastest'''
      rows = [(s.nimi, s.kursus) for s in self.app.student_list.arr]
      popup_table(self.app, "Õpilaste nimekiri", ("Nimi", "Kursus"), rows, [200, 120])

   def _teacher_list(self):
      '''meetod, mis kogub kõikide õpetajate nimed ja ained ning kuvab need tabeli popupis,
      et admin saaks ülevaate kõigist õpetajatest'''
      rows = [(t.nimi, t.kursused) for t in self.app.teacher_list.arr]
      popup_table(self.app, "Õpetajate nimekiri", ("Nimi", "Ained"), rows, [180, 200])

   def _register_dialog(self):
      '''meetod, mis avab dialoogi, kus admin saab sisestada uue kasutaja andmed (roll, kasutajanimi, parool ja täisnimi),
      et registreerida uus kasutaja süsteemi, kui kasutajanimi on juba olemas või kohustuslik'''
      app = self.app
      win = tk.Toplevel(app)
      win.title("Registreeri kasutaja")
      win.configure(bg=app.BG)
      win.grab_set()
      win.resizable(False, False)

      # rolli valik, mis määrab, millised väljad registreerimisvormil kuvatakse
      make_label(win, "Roll:", size=9, color=app.MUTED).pack(padx=24, pady=(16,2), anchor="w")
      role_var = tk.StringVar(value="student")
      role_frame = tk.Frame(win, bg=app.BG)
      role_frame.pack(padx=24, anchor="w", pady=(0,8))
      tk.Radiobutton(role_frame, text="Õpilane", variable=role_var, value="student", # valikkast õpilase rolli valikuks
                     bg=app.BG, fg=app.TEXT, font=("Segoe UI",10),
                     activebackground=app.BG, selectcolor=app.PRI_HL,
                     command=lambda: toggle()).pack(side="left", padx=(0,16))
      tk.Radiobutton(role_frame, text="Õpetaja", variable=role_var, value="teacher", # valikkast õpetaja rolli valikuks
                     bg=app.BG, fg=app.TEXT, font=("Segoe UI",10),
                     activebackground=app.BG, selectcolor=app.PRI_HL,
                     command=lambda: toggle()).pack(side="left")

      fields = {} # sõnastik, mis hoiab sisestuskastide viiteid, et saaks hiljem nende kaudu väärtusi lugeda ja tühjendada
      frames = {} # sõnastik, mis hoiab erinevate rollide jaoks mõeldud raamide viiteid, et saaks neid näidata või peita vastavalt valitud rollile

      def add_field(parent, label, key, frame_key=None):
         '''abifunktsioon, mis loob sildi ja sisestuskasti, pakib need vanemraami sisse ja salvestab sisestuskasti viite fields sõnastikku,
         et saaks hiljem selle kaudu väärtusi lugeda ja tühjendada, frame_key võimaldab määrata,
         millisesse rolli spetsiifilisse raamile see väli kuulub, kui frame_key on None, lisatakse see common raami,
         mis on mõeldud mõlema rolli jaoks'''
         make_label(parent, label, size=9, color=app.MUTED).pack(padx=0, pady=(6,2), anchor="w")
         e = make_entry(parent, width=26)
         e.pack(ipady=4)
         fields[key] = e

      common = tk.Frame(win, bg=app.BG)
      common.pack(padx=24, fill="x")
      add_field(common, "Kasutajanimi:", "username")
      add_field(common, "Parool:", "password")

      details_container = tk.Frame(win, bg=app.BG)
      details_container.pack(padx=24, fill="x", pady=(6,0))

      student_frame = tk.Frame(details_container, bg=app.BG)
      teacher_frame = tk.Frame(details_container, bg=app.BG)
      frames["student"] = student_frame
      frames["teacher"] = teacher_frame

      sf = tk.Frame(student_frame, bg=app.BG); sf.pack(fill="x") # eraldi raam õpilase spetsiifiliste väljade jaoks
      add_field(sf, "Täisnimi:", "s_fullname")
      add_field(sf, "Kursus:", "s_kursus")

      tf = tk.Frame(teacher_frame, bg=app.BG); tf.pack(fill="x") # eraldi raam õpetaja spetsiifiliste väljade jaoks
      add_field(tf, "Täisnimi:", "t_fullname")
      add_field(tf, "Ained (komaga eraldatud):", "t_subjects")

      def toggle():
         for f in frames.values():
            f.pack_forget()
         frames[role_var.get()].pack(fill="x")

      toggle()

      def submit():
         '''funktsioon, mis käivitatakse, kui admin vajutab "Registreeri" nuppu,
         loeb sisestatud väärtused, kontrollib, kas kohustuslikud väljad on täidetud,
         registreerib uue kasutaja ja lisab selle õpilaste või õpetajate nimekirja,
         kui kasutajanimi on juba olemas või kohustuslikud väljad on tühjad, näitab veateadet'''
         username = fields["username"].get().strip()
         password = fields["password"].get().strip()
         role     = role_var.get()
         if not username or not password:
            messagebox.showerror("Viga", "Kasutajanimi ja parool on kohustuslikud.", parent=win); return

         if role == "student": 
            '''kui roll on õpilane, loeb täisnime ja kursuse, kontrollib, kas need on täidetud,
            registreerib uue kasutaja ja lisab selle õpilaste nimekirja,
            kui kasutajanimi on juba olemas või kohustuslikud väljad on tühjad, näitab veateadet'''
            full_name = fields["s_fullname"].get().strip()
            kursus    = fields["s_kursus"].get().strip()
            if not full_name or not kursus:
               messagebox.showerror("Viga", "Täisnimi ja kursus on kohustuslikud.", parent=win); return
            ok = app.login_system.register_user(username, password, role, full_name)
            if not ok:
               messagebox.showerror("Viga", "See kasutajanimi on juba olemas.", parent=win); return
            app.student_list.addStudent(Student(full_name, kursus))
            messagebox.showinfo("Edukas", f"Õpilane {full_name} ja konto registreeritud!", parent=win)

         elif role == "teacher":
            '''kui roll on õpetaja, loeb täisnime ja ained, kontrollib, kas täisnimi on täidetud,
            registreerib uue kasutaja ja lisab selle õpetajate nimekirja,
            kui kasutajanimi on juba olemas või kohustuslikud väljad on tühjad, näitab veateadet'''
            full_name = fields["t_fullname"].get().strip()
            subjects  = fields["t_subjects"].get().strip()
            if not full_name:
               messagebox.showerror("Viga", "Täisnimi on kohustuslik.", parent=win); return
            ok = app.login_system.register_user(username, password, role, full_name)
            if not ok:
               messagebox.showerror("Viga", "See kasutajanimi on juba olemas.", parent=win); return
            app.teacher_list.addTeacher(Teacher(full_name, subjects))
            messagebox.showinfo("Edukas", f"Õpetaja {full_name} ja konto registreeritud!", parent=win)

         for f in frames.values():
            f.pack_forget()
         frames[role_var.get()].pack(fill="x")

      make_button(win, "Registreeri", submit, color="#a12c7b", width=18).pack(pady=12)
      make_button(win, "Sulge", win.destroy, color="#d4d1ca", fg=app.TEXT, width=10).pack(pady=(0,16))

   def _delete_dialog(self):
      ''''meetod, mis avab dialoogi, kus admin saab sisestada kasutajanime, et kustutada see kasutaja süsteemist,
      kui kasutajat ei leita või admini kasutajat üritatakse kustutada, näitab veateadet, kui kustutamine õnnestub,
      eemaldab kasutaja ja sellega seotud õpilase või õpetaja nimekirjast ning annab sellest teada'''
      app = self.app
      win = tk.Toplevel(app)
      win.title("Kustuta kasutaja")
      win.configure(bg=app.BG)
      win.grab_set()
      win.resizable(False, False)
      make_label(win, "Kasutajanimi:", size=9, color=app.MUTED).pack(padx=24, pady=(18,2), anchor="w")
      entry = make_entry(win, width=26)
      entry.pack(padx=24, ipady=4)

      def submit():
         '''funktsioon, mis käivitatakse, kui admin vajutab "Kustuta" nuppu,
         loeb sisestatud kasutajanime, kontrollib, kas see on kehtiv ja kas admini kasutajat üritatakse kustutada,
         kui jah, näitab veateadet, kui ei, kustutab kasutaja ja sellega seotud õpilase või õpetaja nimekirjast ning annab sellest teada'''
         username = entry.get().strip()
         if not username:
            messagebox.showerror("Viga", "Palun sisesta kasutajanimi.", parent=win); return
         if username == "admin":
            messagebox.showerror("Viga", "Admin kasutajat ei saa kustutada.", parent=win); return
         removed = app.login_system.delete_user(username)
         if removed is None:
            messagebox.showerror("Viga", "Kasutajat ei leitud.", parent=win); return
         if removed.role == "student":
            app.student_list.remove_by_name(removed.full_name)
            messagebox.showinfo("Kustutatud", f"Kasutaja '{username}' ja seotud õpilane eemaldati.", parent=win)
         elif removed.role == "teacher":
            app.teacher_list.remove_by_name(removed.full_name)
            messagebox.showinfo("Kustutatud", f"Kasutaja '{username}' ja seotud õpetaja eemaldati.", parent=win)
         entry.delete(0, "end")

      make_button(win, "Kustuta", submit, color="#a12c7b", width=14).pack(pady=12)
      make_button(win, "Sulge", win.destroy, color="#d4d1ca", fg=app.TEXT, width=10).pack(pady=(0,16))

   def _logout(self):
      ''''meetod, mis logib kasutaja välja ja suunab tagasi sisselogimisraamile'''
      self.app.login_system.logout()
      self.app.show_frame(LoginFrame)


# ── Entry point ──────────────────────────────────────────────────

def main():
   '''entry point, mis loob rakenduse ja käivitab peamise tsükli'''
   app = App()
   app.mainloop()

if __name__ == "__main__":
   main()
