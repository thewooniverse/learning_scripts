import os
import pickle
path = f'{os.getcwd()}/BOA_49135_129.pkl'

with open(path, 'rb') as f:
    accounts = pickle.load(f)
    print(accounts)
    accounts.append("Another Object")
    print(accounts)

# prints [] so that works and can be manipulated as a list object.
