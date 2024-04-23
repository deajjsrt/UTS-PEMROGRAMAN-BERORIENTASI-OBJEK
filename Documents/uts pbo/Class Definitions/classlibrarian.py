class Librarian:
    def __init__(self, member_id, name, address, date_of_birth, email):
        self.member_id = member_id
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth
        self.email = email

    def get_member_id(self):
        return self.member_id

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_email(self):
        return self.email

member1 = Librarian("422023017", "Yonathan Dea", "Tanjung Duren, Jakarta Barat", "2004-08-09", "yonathandea0@gmail.com")

print("Member Information:")
print("Member ID:", member1.get_member_id())
print("Name:", member1.get_name())
print("Address:", member1.get_address())
print("Date of Birth:", member1.get_date_of_birth())
print("Email:", member1.get_email())