class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username


class Appointment:
    def __init__(self, name, contact, appointment_type, date, time):
        self.name = name
        self.contact = contact
        self.appointment_type = appointment_type
        self.date = date
        self.time = time

    def __str__(self):
        return f"Name: {self.name}\nContact: {self.contact}\nType: {self.appointment_type}\nDate: {self.date}\nTime: {self.time}"


class AppointmentSystem:
    def __init__(self):
        self.users = []
        self.appointments_teacher = []
        self.appointments_student = []

    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        print("Registration successful!")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print(f"Login successful! Welcome, {user.username}!")
                return True
        print("Invalid username or password. Login failed.")
        return False

    def make_appointment(self):
        appointee = input("Who would you like to appoint with (teacher/student)? ")

        if appointee.lower() == "teacher":
            name = input("Enter the name of the teacher: ")
            contact = input("Enter the contact of the teacher: ")
            appointment_type = input("Choose appointment type (virtual/face-to-face): ")
            date = input("Enter the appointment date: ")
            time = input("Enter the appointment time: ")
            appointment = Appointment(name, contact, appointment_type, date, time)
            self.appointments_teacher.append(appointment)
            print("Appointment with a teacher has been scheduled.")
        elif appointee.lower() == "student":
            name = input("Enter your name: ")
            contact = input("Enter your contact: ")
            appointment_type = input("Choose appointment type (virtual/face-to-face): ")
            date = input("Enter the appointment date: ")
            time = input("Enter the appointment time: ")
            appointment = Appointment(name, contact, appointment_type, date, time)
            self.appointments_student.append(appointment)
            print("Appointment with a student has been scheduled.")
        else:
            print("Invalid appointee. Please try again.")

    def view_appointments(self, appointee):
        if appointee.lower() == "teacher":
            if len(self.appointments_teacher) == 0:
                print("No appointments with teachers.")
            else:
                print("Teacher's Appointments:")
                for index, appointment in enumerate(self.appointments_teacher, start=1):
                    print(f"Appointment {index}:")
                    print(appointment)
                    print("------------------------")
        elif appointee.lower() == "student":
            if len(self.appointments_student) == 0:
                print("No appointments with students.")
            else:
                print("Student's Appointments:")
                for index, appointment in enumerate(self.appointments_student, start=1):
                    print(f"Appointment {index}:")
                    print(appointment)
                    print("------------------------")
        else:
            print("Invalid appointee. Please try again.")

    def delete_appointment(self, appointee):
        if appointee.lower() == "teacher":
            self.view_appointments("teacher")
            appointments = self.appointments_teacher
        elif appointee.lower() == "student":
            self.view_appointments("student")
            appointments = self.appointments_student
        else:
            print("Invalid appointee. Please try again.")
            return

        if len(appointments) == 0:
            print("No appointments to delete.")
            return

        appointment_index = input("Enter the index of the appointment to delete: ")
        try:
            appointment_index = int(appointment_index)
            if appointment_index > 0 and appointment_index <= len(appointments):
                deleted_appointment = appointments.pop(appointment_index - 1)
                print(f"Appointment with {deleted_appointment.name} has been deleted.")
            else:
                print("Invalid appointment index.")
        except ValueError:
            print("Invalid appointment index.")

    def update_appointment(self, appointee):
        if appointee.lower() == "teacher":
            self.view_appointments("teacher")
            appointments = self.appointments_teacher
        elif appointee.lower() == "student":
            self.view_appointments("student")
            appointments = self.appointments_student
        else:
            print("Invalid appointee. Please try again.")
            return

        if len(appointments) == 0:
            print("No appointments to update.")
            return

        appointment_index = input("Enter the index of the appointment to update: ")
        try:
            appointment_index = int(appointment_index)
            if appointment_index > 0 and appointment_index <= len(appointments):
                appointment = appointments[appointment_index - 1]
                print("Enter new appointment details (leave blank to keep current value):")
                name = input(f"Name [{appointment.name}]: ") or appointment.name
                contact = input(f"Contact [{appointment.contact}]: ") or appointment.contact
                appointment_type = input(f"Appointment type [{appointment.appointment_type}]: ") or appointment.appointment_type
                date = input(f"Date [{appointment.date}]: ") or appointment.date
                time = input(f"Time [{appointment.time}]: ") or appointment.time

                appointment.name = name
                appointment.contact = contact
                appointment.appointment_type = appointment_type
                appointment.date = date
                appointment.time = time

                print("Appointment has been updated successfully.")
            else:
                print("Invalid appointment index.")
        except ValueError:
            print("Invalid appointment index.")


# Main program
appointment_system = AppointmentSystem()

while True:
    print("Welcome to the Appointment System!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        appointment_system.register_user(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if appointment_system.login(username, password):
            while True:
                print("Appointment System Menu:")
                print("1. Make Appointment")
                print("2. View Appointments")
                print("3. Delete Appointment")
                print("4. Update Appointment")
                print("5. Logout")
                choice = input("Enter your choice (1-5): ")

                if choice == "1":
                    appointment_system.make_appointment()
                elif choice == "2":
                    appointee = input("View appointments of teacher or student? ")
                    appointment_system.view_appointments(appointee)
                elif choice == "3":
                    appointee = input("Delete appointment of teacher or student? ")
                    appointment_system.delete_appointment(appointee)
                elif choice == "4":
                    appointee = input("Update appointment of teacher or student? ")
                    appointment_system.update_appointment(appointee)
                elif choice == "5":
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif choice == "3":
        print("Thank you for using the Appointment System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        