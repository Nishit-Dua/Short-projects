import pandas as pd
mainDf = pd.read_csv('./user_pass.csv')
mainDf.set_index('email', inplace=True)


class User():

    def __init__(self, email: str, passwd=None):
        '''
        initializing the class
        '''
        self.email = email
        self.passwd = passwd
        if self.user_exist():
            name = mainDf.loc[self.email]['uname']
            print(f'Welcome back {name}')

    def user_exist(self):
        '''
        checks if user exists in the DataFrame of csv
        '''
        if self.email in mainDf.index:
            return all(self.passwd == mainDf.loc[self.email, ['passwd']])
        else:
            return False

    def sign_up(self):
        '''
        if email doesn't exists appends the new user to csv
        '''
        if self.email in mainDf.index:
            print('User Aready Exists!! try remembering the\
 correct password xD ')
        else:
            name = input('Enter Your Username: ')
            self.passwd = input('Enter Your New Password: ')
            while self.passwd == '!!':
                self.passwd = input('Invalid Password try again: ')
            with open('./user_pass.csv', 'a') as df:
                df.write(f'\n{",".join([name, self.email,self.passwd])}')


if __name__ == "__main__":
    print('Welcome to this short Login-System :D')
    email = input('Enter Your email address: ')
    if email not in mainDf.index:
        yn = input('You Currently dont have your email registered press\
 "y" to sign up: ')
        if yn.lower() != 'y':
            print('You need to sign up before using it, Good Bye for now')
        else:
            person = User(email)
            person.sign_up()
            print('Congrats on Signing Up yay !!')
    else:
        passwd = input('Enter your password: ')
        person = User(email, passwd)
        while not person.user_exist() or passwd == '!!':
            passwd = input('Wrong PassWord try agian or enter !! to quit: ')
            person = User(email, passwd)
