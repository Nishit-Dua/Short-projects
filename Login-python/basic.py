import pandas as pd
import userClass
data = {
	'name' : ['nishit', 'dua', 'lol'],
	'email' : ['nd@gmail.com', 'd@gmail.cpo', 'lol@lol.com'],
	'pass' : ['yes', 'yes', 'no']
}

df = pd.DataFrame(data)

df['name'].