import tkinter as tk
from tkinter import ttk, messagebox

# ── Base classes (unchanged) ─────────────────────────────────────

class School:
   def __init__(self):
      pass


class Student:
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
      return f"{self.nimi}, {self.kursus}"


class StudentList:
   def __init__(self):
      self.arr = []

   def addStudent(self, student):
      self.arr.append(student)

   def displayInfo(self):
      for s in self.arr:
         print(s)

   def find_by_name(self, nimi):
      if nimi is None:
         return None
      nimi = nimi.strip().lower()
      for s in self.arr:
            if s.nimi.strip().lower() == nimi:
               return s
      return None

   def remove_by_name(self, nimi):
      student = self.find_by_name(nimi)
      if student is not None:
         self.arr.remove(student)
         return True
      return False

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


class TeacherList:
   def __init__(self):
      self.arr = []

   def addTeacher(self, teacher):
      self.arr.append(teacher)

   def displayInfo(self):
      for t in self.arr:
         print(t)

   def find_by_name(self, nimi):
      if nimi is None:
         return None
      nimi = nimi.strip().lower()
      for t in self.arr:
         if t.nimi.strip().lower() == nimi:
            return t
      return None

   def remove_by_name(self, nimi):
      teacher = self.find_by_name(nimi)
      if teacher is not None:
         self.arr.remove(teacher)
         return True
      return False


class User:
   def __init__(self, username, password, role, full_name=None):
      self.username = username
      self.password = password
      self.role = role
      self.full_name = full_name


class LoginSystem:
   def __init__(self):
      self.users = {
         'opilane1': User('opilane1', 'pass123', 'student', 'Mari Maasikas'),
         'õpetaja1': User('õpetaja1', 'teach123', 'teacher'),
         'admin': User('admin', 'admin123', 'admin')
      }
      self.current_user = None

      def register_user(self, username, password, role, full_name=None):
         if username in self.users:
            print("See kasutajanimi on juba olemas.")
            return False

   def delete_user(self, username):
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
      if username in self.users and self.users[username].password == password:
         self.current_user = self.users[username]
         return True
      return False

   def logout(self):
      print(f"\n{self.current_user.username} logiti välja.")
      self.current_user = None

   def register_user(self, username, password, role, full_name=None):
      if username in self.users:
         print("See kasutajanimi on juba olemas.")
         return False
      self.users[username] = User(username, password, role, full_name)
      print(f"Kasutaja {username} registreeriti kui {role}.")
      return True


# ── Tkinter GUI ──────────────────────────────────────────────────

class App(tk.Tk):
   def __init__(self):
      super().__init__()
      self.title("Kooli Süsteem")
      self.resizable(False, False)
      self.configure(bg="#f7f6f2")

      # shared data
      self.login_system = LoginSystem()
      self.student_list = StudentList()
      self.teacher_list = TeacherList()
      self.student_list.addStudent(Student("Mari Maasikas", "10A"))
      self.student_list.addStudent(Student("Jaan Tamm", "10B"))
      self.teacher_list.addTeacher(Teacher("Kalle Kask", "Matemaatika, Füüsika"))

      self.attempts = 3

      # colour palette
      self.BG       = "#f7f6f2"
      self.SURFACE  = "#f9f8f5"
      self.BORDER   = "#d4d1ca"
      self.TEXT     = "#28251d"
      self.MUTED    = "#7a7974"
      self.PRIMARY  = "#01696f"
      self.PRI_HL   = "#cedcd8"
      self.ERROR    = "#a12c7b"
      self.SUCCESS  = "#437a22"

      self.configure(bg=self.BG)
      self._build_styles()

      # container that holds all frames
      container = tk.Frame(self, bg=self.BG)
      container.pack(fill="both", expand=True)

      self.frames = {}
      for F in (LoginFrame, StudentFrame, TeacherFrame, AdminFrame):
         frame = F(container, self)
         self.frames[F] = frame
         frame.grid(row=0, column=0, sticky="nsew")

      self.show_frame(LoginFrame)

   def _build_styles(self):
      style = ttk.Style(self)
      style.theme_use("clam")
      style.configure("Treeview",
         background=self.SURFACE, foreground=self.TEXT,
         fieldbackground=self.SURFACE, rowheight=26,
         font=("Segoe UI", 10))
      style.configure("Treeview.Heading",
         background=self.BG, foreground=self.MUTED,
         font=("Segoe UI", 9, "bold"))
      style.map("Treeview", background=[("selected", self.PRI_HL)],
                foreground=[("selected", self.PRIMARY)])

   def show_frame(self, frame_class):
      frame = self.frames[frame_class]
      if hasattr(frame, "on_show"):
         frame.on_show()
      frame.tkraise()


# ── Helper widgets ───────────────────────────────────────────────

def make_label(parent, text, size=10, bold=False, color=None, bg=None):
   font = ("Segoe UI", size, "bold" if bold else "normal")
   kw = {"text": text, "font": font, "bg": bg or parent.cget("bg")}
   if color:
      kw["fg"] = color
   return tk.Label(parent, **kw)

def make_entry(parent, show=None, width=28):
   e = tk.Entry(parent, show=show, width=width,
                relief="flat", bd=0,
                font=("Segoe UI", 10),
                bg="#ffffff", fg="#28251d",
                insertbackground="#28251d",
                highlightthickness=1,
                highlightbackground="#d4d1ca",
                highlightcolor="#01696f")
   return e

def make_button(parent, text, command, color="#01696f", fg="#ffffff", width=20):
   return tk.Button(parent, text=text, command=command,
                    font=("Segoe UI", 10, "bold"),
                    bg=color, fg=fg, activebackground=color,
                    activeforeground=fg,
                    relief="flat", bd=0, padx=12, pady=6,
                    cursor="hand2", width=width)

def popup_table(parent_app, title, columns, rows, col_widths=None):
   """Generic popup with a ttk.Treeview table."""
   win = tk.Toplevel(parent_app)
   win.title(title)
   win.configure(bg=parent_app.BG)
   win.grab_set()
   win.resizable(False, False)

   tree = ttk.Treeview(win, columns=columns, show="headings", height=min(len(rows)+1, 14))
   for i, col in enumerate(columns):
      w = col_widths[i] if col_widths else 160
      tree.heading(col, text=col)
      tree.column(col, width=w, anchor="w")

   for row in rows:
      tree.insert("", "end", values=row)

   if not rows:
      tree.insert("", "end", values=("(tühi)",) + ("",) * (len(columns)-1))

   scrollbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
   tree.configure(yscroll=scrollbar.set)
   tree.pack(side="left", fill="both", expand=True, padx=(10,0), pady=10)
   scrollbar.pack(side="left", fill="y", pady=10, padx=(0,10))

   make_button(win, "Sulge", win.destroy, width=10).pack(pady=(0,10))


# ── Login Frame ──────────────────────────────────────────────────

class LoginFrame(tk.Frame):
   def __init__(self, parent, app):
      super().__init__(parent, bg=app.BG)
      self.app = app
      self._build()

   def _build(self):
      app = self.app
      # outer card
      card = tk.Frame(self, bg=app.SURFACE, bd=1, relief="flat",
                      highlightthickness=1, highlightbackground=app.BORDER)
      card.pack(padx=60, pady=50, fill="both", expand=True)

      make_label(card, "Kooli Süsteem", size=18, bold=True, color=app.PRIMARY).pack(pady=(30,4))
      make_label(card, "Logi sisse oma kontoga", size=10, color=app.MUTED).pack(pady=(0,20))

      self.alert_var = tk.StringVar()
      self.alert_lbl = tk.Label(card, textvariable=self.alert_var,
                                font=("Segoe UI", 9), bg="#e0ced7", fg=app.ERROR,
                                wraplength=280, justify="left", padx=8, pady=4)

      form = tk.Frame(card, bg=app.SURFACE)
      form.pack(padx=30, pady=4)

      make_label(form, "Kasutajanimi", size=9, color=app.MUTED).grid(row=0, column=0, sticky="w", pady=(0,2))
      self.entry_user = make_entry(form)
      self.entry_user.grid(row=1, column=0, pady=(0,12), ipady=4)

      make_label(form, "Parool", size=9, color=app.MUTED).grid(row=2, column=0, sticky="w", pady=(0,2))
      self.entry_pass = make_entry(form, show="•")
      self.entry_pass.grid(row=3, column=0, pady=(0,4), ipady=4)

      self.entry_pass.bind("<Return>", lambda e: self._do_login())

      make_button(card, "Logi sisse", self._do_login).pack(pady=12)
      make_label(card, "", size=8).pack(pady=(0,24))  # spacer

   def _do_login(self):
      app = self.app
      u = self.entry_user.get().strip()
      p = self.entry_pass.get()

      if app.login_system.login(u, p):
         app.attempts = 3
         self.entry_user.delete(0, "end")
         self.entry_pass.delete(0, "end")
         self.alert_lbl.pack_forget()
         self.alert_var.set("")

         role = app.login_system.current_user.role
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


# ── Student Frame ────────────────────────────────────────────────

class StudentFrame(tk.Frame):
   def __init__(self, parent, app):
      super().__init__(parent, bg=app.BG)
      self.app = app
      self._build()

   def on_show(self):
      name = self.app.login_system.current_user.full_name or self.app.login_system.current_user.username
      self.name_var.set(f"Sisselogitud: {name}")

   def _build(self):
      app = self.app

      header = tk.Frame(self, bg=app.PRIMARY)
      header.pack(fill="x")
      make_label(header, "Õpilase menüü", size=13, bold=True, color="#ffffff", bg=app.PRIMARY).pack(side="left", padx=20, pady=14)
      self.name_var = tk.StringVar()
      tk.Label(header, textvariable=self.name_var, font=("Segoe UI", 9),
               bg=app.PRIMARY, fg=app.PRI_HL).pack(side="left", padx=4)
      make_button(header, "Logi välja", self._logout,
                  color=app.PRI_HL, fg=app.PRIMARY, width=12).pack(side="right", padx=16, pady=10)

      body = tk.Frame(self, bg=app.BG)
      body.pack(padx=30, pady=24, fill="both", expand=True)

      btns = [
         ("📋  Vaata oma hindeid",          self._show_my_grades),
         ("📊  Aine keskmine hinne",         self._subject_avg_dialog),
         ("📈  Kõigi ainete keskmised",      self._all_avgs),
      ]
      for txt, cmd in btns:
         make_button(body, txt, cmd, width=34).pack(pady=6, ipady=4)

   def _get_student(self):
      name = self.app.login_system.current_user.full_name
      return self.app.student_list.find_by_name(name)

   def _show_my_grades(self):
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
         ("👥  Vaata õpilaste nimekirja",     self._student_list),
         ("🏫  Vaata õpetajate nimekirja",    self._teacher_list),
         ("📋  Vaata õpilase hindeid",         self._view_grades_dialog),
         ("➕  Lisa õpilasele hinne",          self._add_grade_dialog),
         ("📊  Õpilase keskmine hinne",        self._student_avg_dialog),
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
      app = self.app
      win = tk.Toplevel(app)
      win.title("Lisa hinne")
      win.configure(bg=app.BG)
      win.grab_set()
      win.resizable(False, False)

      fields = {}
      for label, key in [("Õpilase täisnimi:", "nimi"), ("Aine:", "aine"), ("Hinne:", "hinne")]:
         make_label(win, label, size=9, color=app.MUTED).pack(padx=24, pady=(10,2), anchor="w")
         e = make_entry(win, width=26)
         e.pack(padx=24, ipady=4)
         fields[key] = e

      def submit():
         nimi  = fields["nimi"].get().strip()
         aine  = fields["aine"].get().strip()
         hinne = fields["hinne"].get().strip()
         s = app.student_list.find_by_name(nimi)
         if s is None:
            messagebox.showerror("Viga", "Õpilast sellise nimega ei leitud.", parent=win); return
         try:
            s.lisa_hinne(aine, hinne)
            messagebox.showinfo("Edukas", f"Hinne {hinne} aines '{aine}' lisatud!", parent=win)
            for e in fields.values(): e.delete(0,"end")
         except ValueError:
            messagebox.showerror("Viga", "Sisesta kehtiv hinne (number).", parent=win)

      make_button(win, "Lisa hinne", submit, width=18).pack(pady=12)
      make_button(win, "Sulge", win.destroy, color="#d4d1ca", fg=app.TEXT, width=10).pack(pady=(0,16))

   def _student_avg_dialog(self):
      self._name_search_dialog("Õpilase keskmine", self._do_student_avg)

   def _do_student_avg(self, nimi, win):
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
      self.app.login_system.logout()
      self.app.show_frame(LoginFrame)


# ── Admin Frame ──────────────────────────────────────────────────

class AdminFrame(tk.Frame):
   def __init__(self, parent, app):
      super().__init__(parent, bg=app.BG)
      self.app = app
      self._build()

   def _build(self):
      app = self.app

      header = tk.Frame(self, bg="#a12c7b")
      header.pack(fill="x")
      make_label(header, "Admini menüü", size=13, bold=True, color="#ffffff", bg="#a12c7b").pack(side="left", padx=20, pady=14)
      make_button(header, "Logi välja", self._logout,
                  color="#e0ced7", fg="#a12c7b", width=12).pack(side="right", padx=16, pady=10)

      body = tk.Frame(self, bg=app.BG)
      body.pack(padx=30, pady=24, fill="both", expand=True)

      btns = [
         ("👥  Vaata õpilaste nimekirja",     self._student_list),
         ("🏫  Vaata õpetajate nimekirja",    self._teacher_list),
         ("➕  Registreeri uus kasutaja",      self._register_dialog),
         ("🗑   Kustuta kasutaja",             self._delete_dialog),
      ]
      for txt, cmd in btns:
         make_button(body, txt, cmd, color="#a12c7b", width=34).pack(pady=6, ipady=4)

   def _student_list(self):
      rows = [(s.nimi, s.kursus) for s in self.app.student_list.arr]
      popup_table(self.app, "Õpilaste nimekiri", ("Nimi", "Kursus"), rows, [200, 120])

   def _teacher_list(self):
      rows = [(t.nimi, t.kursused) for t in self.app.teacher_list.arr]
      popup_table(self.app, "Õpetajate nimekiri", ("Nimi", "Ained"), rows, [180, 200])

   def _register_dialog(self):
      app = self.app
      win = tk.Toplevel(app)
      win.title("Registreeri kasutaja")
      win.configure(bg=app.BG)
      win.grab_set()
      win.resizable(False, False)

      # role selection
      make_label(win, "Roll:", size=9, color=app.MUTED).pack(padx=24, pady=(16,2), anchor="w")
      role_var = tk.StringVar(value="student")
      role_frame = tk.Frame(win, bg=app.BG)
      role_frame.pack(padx=24, anchor="w", pady=(0,8))
      tk.Radiobutton(role_frame, text="Õpilane", variable=role_var, value="student",
                     bg=app.BG, fg=app.TEXT, font=("Segoe UI",10),
                     activebackground=app.BG, selectcolor=app.PRI_HL,
                     command=lambda: toggle()).pack(side="left", padx=(0,16))
      tk.Radiobutton(role_frame, text="Õpetaja", variable=role_var, value="teacher",
                     bg=app.BG, fg=app.TEXT, font=("Segoe UI",10),
                     activebackground=app.BG, selectcolor=app.PRI_HL,
                     command=lambda: toggle()).pack(side="left")

      fields = {}
      frames = {}

      def add_field(parent, label, key, frame_key=None):
         make_label(parent, label, size=9, color=app.MUTED).pack(padx=0, pady=(6,2), anchor="w")
         e = make_entry(parent, width=26)
         e.pack(ipady=4)
         fields[key] = e

      common = tk.Frame(win, bg=app.BG)
      common.pack(padx=24, fill="x")
      add_field(common, "Kasutajanimi:", "username")
      add_field(common, "Parool:", "password")

      student_frame = tk.Frame(win, bg=app.BG)
      teacher_frame = tk.Frame(win, bg=app.BG)
      frames["student"] = student_frame
      frames["teacher"] = teacher_frame

      sf = tk.Frame(student_frame, bg=app.BG); sf.pack(padx=24, fill="x")
      add_field(sf, "Täisnimi:", "s_fullname")
      add_field(sf, "Kursus:", "s_kursus")

      tf = tk.Frame(teacher_frame, bg=app.BG); tf.pack(padx=24, fill="x")
      add_field(tf, "Täisnimi:", "t_fullname")
      add_field(tf, "Ained (komaga eraldatud):", "t_subjects")

      def toggle():
         for k, f in frames.items():
            if k == role_var.get():
               f.pack(fill="x")
            else:
               f.pack_forget()

      toggle()

      def submit():
         username = fields["username"].get().strip()
         password = fields["password"].get().strip()
         role     = role_var.get()
         if not username or not password:
            messagebox.showerror("Viga", "Kasutajanimi ja parool on kohustuslikud.", parent=win); return

         if role == "student":
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
            full_name = fields["t_fullname"].get().strip()
            subjects  = fields["t_subjects"].get().strip()
            if not full_name:
               messagebox.showerror("Viga", "Täisnimi on kohustuslik.", parent=win); return
            ok = app.login_system.register_user(username, password, role, full_name)
            if not ok:
               messagebox.showerror("Viga", "See kasutajanimi on juba olemas.", parent=win); return
            app.teacher_list.addTeacher(Teacher(full_name, subjects))
            messagebox.showinfo("Edukas", f"Õpetaja {full_name} ja konto registreeritud!", parent=win)

         for e in fields.values(): e.delete(0, "end")

      make_button(win, "Registreeri", submit, color="#a12c7b", width=18).pack(pady=12)
      make_button(win, "Sulge", win.destroy, color="#d4d1ca", fg=app.TEXT, width=10).pack(pady=(0,16))

   def _delete_dialog(self):
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
      self.app.login_system.logout()
      self.app.show_frame(LoginFrame)


# ── Entry point ──────────────────────────────────────────────────

def main():
   app = App()
   app.mainloop()

if __name__ == "__main__":
   main()
