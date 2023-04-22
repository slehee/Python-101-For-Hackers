# save_user_credentials.py
from app import db, User

def save_user_credentials():
    users = User.query.all()
    with open('user_credentials.txt', 'w') as f:
        for user in users:
            f.write(f"Username: {user.username}, Password: {user.password}\n")

if __name__ == '__main__':
    save_user_credentials()
