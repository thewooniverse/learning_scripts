import pickle
import os


with open(f'{os.getcwd()}{os.path.sep}BOA{os.path.sep}customers{os.path.sep}18238591.pkl', 'rb') as f:
    customer = pickle.load(f)
    print(customer.name)


