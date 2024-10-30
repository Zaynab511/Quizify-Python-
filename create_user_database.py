import pickle
import hashlib
import os

# Function to create a pickle database
def create_user_database():
    users = {
        'Noor': hashlib.sha256('password1'.encode()).hexdigest(),
        'Zainab': hashlib.sha256('password2'.encode()).hexdigest()
    }

    # Specify the directory and file name
    directory = 'DATA'
    filename = 'users.pkl'
    
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the pickle file in the specified directory
    with open(os.path.join(directory, filename), 'wb') as f:
        pickle.dump(users, f)

create_user_database()  # Run this once to create the database
