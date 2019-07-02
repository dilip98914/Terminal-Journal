import click
import pickle
from datetime import datetime

FILENAME='data_pick.pkl'

def load_data(FILENAME):
    new_data=None
    try:
        with open(FILENAME,'rb') as p_file:
            new_data=pickle.load(p_file)
            print(new_data)
    except:
        print("can;t load file")
    return new_data

def save_data(FILENAME,data,shouldLoad=True,lastParam=False):
    if shouldLoad:
        new_data=load_data(FILENAME)
        if new_data is not None:
            new_data.append(data)
    elif(lastParam):
        new_data=data
    else:
        new_data=[data]   

    try:
        with open(FILENAME,'wb') as p_file:
            pickle.dump(new_data,p_file)
    except:
        print("can;t save data to file")


users=load_data(FILENAME)


@click.command()
@click.option('--username',prompt='enter your username to register', default="name", help='username')
@click.option('--password',prompt='enter your password to register', default="password", help='password')
def register(username, password):
    """Registration"""
    current_user={
        'username':username,
        'password':password
        }
    for user in users:
        if user['username'] ==current_user['username']:
            click.echo("User -%s is already register"%current_user['username'])
            return
    users.append(current_user)
    click.echo("User -%s is succesfully register"%current_user['username'])
    save_data(FILENAME,users,False,True)
    print(load_data(FILENAME))
    if click.confirm('return to main menu?'):
        click.echo('puff...')
        mainMenu()



loggedIn=False

@click.command()
@click.option('--username',prompt='enter your username to login', default="name", help='username')
@click.option('--password',prompt='enter your password to login', default="password", help='password')
def login(username, password):
    """Login"""
    current_user={
        'username':username,
        'password':password
        }
    for user in users:
        global loggedIn
        if user['username'] ==current_user['username']:
            print('username is matched')
            if user['password'] ==current_user['password']:
                click.echo('password is matched')
                click.echo("User -%s is succesfuly logged In"%current_user['username'])
                loggedIn=True
                break
    if click.confirm('return to main menu?'):
        click.echo('puff...')
        mainMenu()



# @click.command()
# def createJournal():
#     """Journal Creation"""
#     content=click.prompt('enter your new Journal content')
#     user={

#     }
#     users.append(current_user)
#     click.echo("User -%s is succesfully register"%current_user['username'])
#     save_data(FILENAME,users,False,True)
#     print(load_data(FILENAME))
#     if click.confirm('return to main menu?'):
#         click.echo('puff...')
#         mainMenu()




@click.command()
def mainMenu():

    click.echo('\n')
    click.echo('WELCOME TO COMMAND LINE JOURNAL MANAGER')
    click.echo('\n')
    
    click.echo('You will asked in multiple confimation points to enter different states of application')
    click.echo('\n')

    click.echo('Such as REgister,Login,CreateJournal,ViewJournal')
    click.echo('\n')

    click.echo('Login To create account')
    click.echo('\n')


    if click.confirm('Do you want to register?'):
        register()
    if click.confirm('Do you want to login?'):
        login()
    if click.confirm('Do you want to create journal?'):
        click.echo('create journalQ!')
    if click.confirm('Do you see journal?'):
        click.echo('view journals!')
    if click.confirm('Do you want to exit'):
        return
    mainMenu()



if __name__ == '__main__':
    mainMenu()