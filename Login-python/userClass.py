import pandas as pd
mainDf = pd.read_csv('./user_pass.csv')


class User():

    def __init__(self, username, passwd, email):
        '''
        initializing the class
        '''
        self.passwd = passwd
        self.username = username
        self.email = email

    def get_password(self):
        '''
        gets the pass word from ./user_pass.csv
        will raise some error if user_pass.csv is not
        in the current directory
        '''
        return mainDf.iloc([self.email], ['password'])

    def pass_correct(self):
        '''
        checks if user has entered the passwor
        in the database
        '''
        if self.passwd == self.get_password(self.username):
            return True

        else:
            return False

    def GoodPassword(password):
        '''
        if password is strong --> stonks
        if weak --> not stonks
        '''
        def hasNumbers(String):
            return any(char.isdigit() for char in String)

        if password.__len__() > 8 and hasNumbers(password):
            return True

    def changePassword(self):
        '''
        changes the self pass and updates the user_pass.csv
        '''
        current_pass = input('Enter current password')

        if current_pass == self.passwd:
            tempNewPass = input('Enter new password')

            if self.GoodPassword(tempNewPass):
                self.passwd = tempNewPass
                mainDf.loc[self.email, 'Passwords'] = self.passwd
                # TODO update the password in the csv
            else:
                print('Weak password try again\n')

        else:
            print('wrong password try again\n')

    def removeUser(self):
        # TODO add this
        pass


def check_existance(email):
    if email in mainDf['email']:
        return True
    else:
        return False


def signUp(email, username, password):
    # TODO: Create this lol
    pass
