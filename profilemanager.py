import csv
import os.path

class Profile:
    def __init__(self):
        pass

    def create_profile(self, profle):
        file_exist = os.path.isfile('profile.csv')
        with open('profile.csv', 'a') as file:
            fieldname= ['first name', 'last name', 'password', 'username', 'bio', 'date_of_birth']
            writer = csv.DictWriter(file, fieldnames=fieldname)

            if not file_exist:
                writer.writeheader()
            writer.writerow({'first name':profle.f_name, 'last name':profle.l_name, 'username':profle.username, 'bio':profle.bio, 'date_of_birth':profle.date_of_birth} )
            print('Your profile has been created')

    def update_bio(self):
        with open('profile.csv', 'r') as file:
            nw_user = input('Supply username: ')
            reader = csv.DictReader(file)
            for pr in reader:
                if pr['username'] == nw_user:
                    # print(pr)
                    choice = input(' a to update first name\n b to update last name \n c to update bio d. update date of birth\n e to update password').lower()
                    if choice == 'a':
                        new_f_name = input('Supply new first name: ')
                        pr['first name'] = new_f_name
                        print("--- Your First Name is now "+str(pr['first name']))
                    elif choice == 'b':
                        new_l_name = input('Supply new last name: ')
                        pr['last name'] = new_l_name
                        print("--- Your Last Name is now " + str(pr['last name']))
                    elif choice == 'c':
                        new_bio = input('Supply new bio: ')
                        pr['bio'] = new_bio
                        print("Bio updated successfully")
                    elif choice == 'd':
                        new_dob = input('Supply new date of birth: ')
                        pr['date_of_birth'] = new_dob
                        print("--- Your Date-of-Birth is now " + str(pr['last name']))
                    elif choice == 'e':
                        new_password = input('Supply new password: ')
                        pr['password'] = new_password
                        print('Password changed successfully')

        """
    - first name
    - last name
    - bio
    - date of birth
    - and password.
        """
        pass

    def view_posts(self):
        pass
    def set_photo(self):
        """
        Profile photo
        Back ground photo
        """
        pass
    def view_fiends(self):
        pass

class Profile_input:
    def __init__(self, f_name='', l_name='' ):
        self.f_name = input('supply first name:')
        self.l_name = input('supply last name:')
        self.password = input('supply password:')
        self.username = input('supply username:')
        self.bio = input('Write a short bio:')
        self.date_of_birth = input('supply date of birth:')

def logic():
    while True:
        pf = Profile()
        request = input(" 1. to Create profles \n 2. to Update Bio \n 3. to view posts \n 4. to Update photo \n 5. to view friends ")
        if request == '1':
            pi = Profile_input()
            pf.create_profile(pi)
        elif request == '2':
            pf.update_bio()
        elif request== '3':
            pf.view_posts()
        elif request== '4':
            pf.set_photo()
        elif request == '5':
            pf.view_fiends()
        elif request == '6':
            return False

logic()