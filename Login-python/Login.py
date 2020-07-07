import pandas as pd
mainDf = pd.read_csv('./user_pass.csv')
mainDf.set_index('email', inplace=True)


class User():

    def __init__(self, email, passwd):
        '''
        initializing the class
        '''
        self.email = email
        self.passwd = passwd
        if self.user_exist():
            name = mainDf.loc[self.email]['uname']
            print(f'Welcome back {name}')
        else:
            print('Sorry We could not find you in our records\
 are you sure you entered the correct email and password ?\nIf You\
 Haven\'t signed up yet! sign up Now!!! ')

    def user_exist(self):
        '''
        checks if user exists in the DataFrame of csv
        '''
        if self.email in mainDf.index:
            return all(self.passwd == mainDf.loc[self.email, ['passwd']])
        else:
            return False


User('f20180620@gmail.com', 'lmaomyass')
