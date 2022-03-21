


class Spartan:

    def __init__(self, spartan_id, first_name, last_name, birth_year, birth_month, birth_day, course, stream):
        self.spartan_id = spartan_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.course = course
        self.stream = stream

    def get_spartan_id(self):
        return self.spartan_id

    def set_spartan_id(self, new_spartan_id):
        if new_spartan_id > 0:
            self.spartan_id = new_spartan_id
            print(f"Spartan's ID is {self.spartan_id}")
        else:
            return print("The Spartan ID is Invalid")

    def get_first_name(self):
        return self.first_name()

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name
        print(f"Spartan's first name is {self.first_name}")

    def get_last_name(self):
        return self.last_name()

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name
        print(f"Spartan's last name is {self.last_name}")

    def get_birth_year(self):
        return self.birth_year

    def set_birth_year(self, new_birth_year):
        if new_birth_year > 0:
            self.birth_year = new_birth_year
            print(f"Spartan's birth year is {self.birth_year}")

    def get_birth_month(self):
        return self.birth_month

    def set_birth_month(self, new_birth_month):
        if new_birth_month > 0:
            self.birth_month = new_birth_month
            print(f"Spartan's birth month is {self.birth_month}")

    def get_birth_day(self):
        return self.birth_day

    def set_birth_day(self, new_birth_day):
        if new_birth_day > 0:
            self.birth_day = new_birth_day
            print(f"Spartan's birth day is {self.birth_day}")

    def get_course(self):
        return self.course

    def set_course(self, new_course):
            self.course = new_course
            print(f"Spartan's course is {self.course}")

    def get_stream(self):
        return self.stream

    def set_stream(self, new_stream):
        self.stream = new_stream
        print(f"Spartan's stream is {self.stream}")

    def print_spartan_data(self):
        spartan = {"Spartan ID": self.spartan_id,
                   "Spartan's First Name": self.first_name,
                   "Spartan's Last Name": self.last_name,
                   "Spartan's Day of Birth": self.birth_day,
                   "Spartan's Month of Birth": self.birth_month,
                   "Spartan's Year of Birth": self.birth_year,
                   "Spartan's Course": self.course,
                   "Spartan's Stream": self.stream}

        return print(spartan)

    def __str__(self):
        return f"sparta_id: {self.spartan_id} -  First Name: {self.first_name} - Last Name: {self.last_name} - birth_year:{self.birth_year}-birth_month:{self.birth_month}- birth_day:{self.birth_day}-course:{self.course}-stream:{self.stream} "




