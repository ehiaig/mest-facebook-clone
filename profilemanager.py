import csv
import os.path
import re

class Profile:
    def __init__(self):
        pass

    def update_bio(self):
        with open('profile.csv', 'r') as file:
            nw_user = input('Supply username: ')
            reader = csv.DictReader(file)
            for pr in reader:
                if pr['username'] == nw_user:
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
        with open('friends.csv', 'r') as file:
            reader = csv.DictReader(file)
            uname = input("What\'s your username: ")
            for fr in reader:
                if fr['username'] == uname:
                    print('Your friends are: '+ fr['friendlist'])
def logic():
    while True:
        pf = Profile()
        request = input(" 1. to Update Bio \n 2. to view posts \n 3. to Set profile or background photo \n 4. to view friends \n 5. to exit app")
        if request == '1':
            pf.update_bio()
        elif request == '2':
            pf.view_posts()

        elif request== '3':
            pf.set_photo()

        elif request== '4':
            pf.view_fiends()

        elif request == '5':
            return False

logic()