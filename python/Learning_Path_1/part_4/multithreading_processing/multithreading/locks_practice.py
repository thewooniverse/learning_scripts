

# example script that modifies a single resource "df" from ultipel threads
from threading import Thread, Lock
import pandas as pd

# Create a simple dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Create a lock object
df_lock = Lock()

# Define a function that modifies the dataframe
def modify_df(row, new_value):
    global df
    with df_lock:  # Acquire the lock
        df.loc[row, 'A'] = new_value  # Modify the dataframe
        # ... do some more operations
    # Release the lock automatically when exiting the 'with' block

# Create threads that will modify the dataframe
thread1 = Thread(target=modify_df, args=(0, 10))
thread2 = Thread(target=modify_df, args=(1, 20))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# The dataframe is now modified safely
print(df)







"""
# import pandas as pd
# df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# df.loc[2] = [5, 6]
# print(df)
OUTPUT:
   A  B
0  1  3
1  2  4
2  5  6
"""