from src import get_config
from src.User import User

# uid = User.register("sibidharan", "insecure_password", "insecure_password")
# print(type(uid))

if User.login("sibidharan", "insecure_passord"):
    print("Login Success")
else:
    print("Login Failed")
