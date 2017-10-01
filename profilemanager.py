import csv
import os.path
import re

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
            writer.writerow({'first name':profle.firstname, 'last name':profle.lastname, 'username':profle.username, 'bio':profle.bio, 'date_of_birth':profle.date_of_birth} )
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
                        new_firstname = input('Supply new first name: ')
                        pr['first name'] = new_firstname
                        print("--- Your First Name is now "+str(pr['first name']))
                    elif choice == 'b':
                        new_lastname = input('Supply new last name: ')
                        pr['last name'] = new_lastname
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
                else:
                    print('That username does not exist in our record ')

    def view_posts(self):
        with open("posts.csv", 'r') as file:
            reader = csv.DictReader(file)
            for ps in reader:
                if ps['username'] in ps['posts']:
                    print(ps['posts'])
                else:
                    print('This user has no posts')

    def set_photo(self):
        with open('media/photo.csv', 'wb') as file:
            uname = input("What\'s your username: ")
            reader = csv.DictReader(file)
            for fl in reader:
                if fl['username'] == uname:
                    choice = input(' 1. to set profile photo\n 2. to set background photo')
                    if choice == '1':
                        p_photo = input('Enter photo path')
                        fl['Profile Photo'] = p_photo
                        print(fl['Profile Photo'])
                    elif choice == '2':
                        bkground_photo = input('Enter photp path')
                        fl['Background Photo'] = bkground_photo
                        print(fl['Background Photo'])
                else:
                    print('Your username is not valid')

    def view_fiends(self):

        # file_exist = os.path.isfile('friends.csv')
        # with open('friends.csv', 'a') as file:
        #     fieldname = ['username', 'friendlist']
        #     writer = csv.DictWriter(file, fieldnames=fieldname)
        #
        #     if not file_exist:
        #         writer.writeheader()
        #     writer.writerow({'username': 'endy',
        #                      'friendlist': ['Kweku', 'Andrew']})
        #     print('Your friends have been added')

        with open('friends.csv', 'r') as file:
            reader = csv.DictReader(file)
            uname = input("What\'s your username: ")
            for fr in reader:
                if fr['username'] == uname:
                    print('Your friends are: '+ fr['friendlist'])
        pass

class Profile_input:
    def __init__(self, firstname='', lastname='' ):
        self.firstname = input('supply first name:')
        self.lastname = input('supply last name:')
        self.password = input('supply password:')
        self.username = input('supply username:')
        self.bio = input('Write a short bio:')
        self.date_of_birth = input('supply date of birth:')

def logic():
    while True:
        pf = Profile()
        request = input(" 1. to Create profles \n 2. to Update Bio \n 3. to view posts \n 4. to Update photo \n 5. to view friends \n 6. to quit")
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
            # pi = Profile_input()
            pf.view_fiends()

        elif request == '6':
            return False

logic()