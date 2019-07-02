import pickle
from datetime import datetime
from pprint import pprint as print

FILENAME='data_pick.pkl'

def load_data(FILENAME):
    new_data=None
    try:
        with open(FILENAME,'rb') as p_file:
            new_data=pickle.load(p_file)
            print("loaded data: ")
            print(new_data)
    except Exception as e:
        print(e)
        print("can;t load file")
    return new_data

def save_data(FILENAME,data,data_array):
    if data!=None:
        data_array.append(data)   
    else:
        print('data not appendded as journal just updated')
    try:
        with open(FILENAME,'wb') as p_file:
            pickle.dump(data_array,p_file)
    except:
        print("can;t save data to file")



class User(object):
    def __init__(self,users):
        self.user=None
        self.users=users
        self.isLoggedIn=False


    def register(self):
        self.check_Login()
        username=input('enter username to register: ')
        password=input('enter password to register: ')
        current_user={
            'username':username,
            'password':password,
            'journals':[]
            }
        for user in self.users:
            if user['username'] ==current_user['username']:
                print("User -%s is already register"%current_user['username'])
                if input('return to main menu? ')=="1":
                    print('going to menu\n')
                    mainMenu(self)
                return    

        save_data(FILENAME,current_user,self.users)
        print("User -%s is succesfully register"%current_user['username'])
        print(self.users)
        if input('return to main menu? ')=="1":
            print('going to menu\n')
            mainMenu(self)

    def check_Login(self):
        if self.isLoggedIn:
            print('user already logged in!')
            res=input('user needs to logged out? ')
            if res =="1":
                self.logout()
            return
    def logout(self):
        if self.isLoggedIn:
            self.isLoggedIn=False
        self.user=None


    def login(self):
        self.check_Login()
        username=input('enter username to login: ')
        password=input('enter password to login: ')
        current_user={
            'username':username,
            'password':password,
            'journals':[]
            }

        for user in self.users:
            if user['username'] ==current_user['username']:
                print('username is matched\n')
                if user['password'] ==current_user['password']:
                    if self.user==None and self.isLoggedIn==False:
                        print('password is matched\n')
                        print("User -%s is succesfuly logged In\n"%current_user['username'])
                        self.isLoggedIn=True
                        self.user=user
                        break
                    else:
                        print('user seems already logged in!')
        print(self.users)
        if input('return to main menu? ')=="1":
            print('going to menu\n')
            mainMenu(self)

    def createJournal(self):
        if not self.isLoggedIn:
            print('not authenticated\n')
            if input('return to main menu?\n')=="1":
                print('going to menu\n')
                mainMenu(self)
            else:
                return

        content=input('enter your new Journal content: ')
        self.user['journals'].append({
            'content':content,
            'timestamp':datetime.now().strftime("%H:%M:%S")
        })
        print('umodified user is %s\n'%self.user)
        # index=self.users.index(self.user)
        # self.users[index]=newUser
        save_data(FILENAME,None,self.users)
        print(self.users)
        if input('return to main menu? ')=="1":
            print('going to menu\n')
            mainMenu(self)

    def viewJournals(self):
        if not self.isLoggedIn:
            print('not authenticated\n')
            if input('return to main menu?\n')=="1":
                print('going to menu\n')
                mainMenu(self)
            else:
                return

        for journal in self.user['journals']:
            print("%s"%journal)
        if input('return to main menu? ')=="1":
            print('going to menu\n')
            mainMenu(self)




def mainMenu(userObj):
    print('\nWELCOME TO COMMAND LINE JOURNAL MANAGER\n')
    print('\n1.Register\n')
    print('\n2.login\n')
    print('\n3.create new journal\n')
    print('\n4.view your journals\n')
    print('\n5.exit\n')
    choice=input('\nenter your choice: \n')
    if choice=="1":
        userObj.register()
    if choice=="2":
        userObj.login()
    if choice=="3":
        userObj.createJournal()
    if choice=="4":
        userObj.viewJournals()
    if choice=="5":
        return



def createDatabase():
    data={
        'username':'sample',
        'password':'pass',
        'journals':[{
            'content':'sample journal',
            'timestamp':datetime.now().strftime("%H:%M:%S")
        }]
    }
    save_data(FILENAME,data,[])


if __name__ == '__main__':
    # createDatabase()
    users=load_data(FILENAME)
    user=User(users)
    mainMenu(user)

