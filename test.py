from src import get_config
from src.User import User

# uid = User.register("sibidharan", "insecure_password", "insecure_password")
# print(type(uid))

try:
    User.login("sibidharan", "insecure_password1")
    print("Login Success")
except Exception as e:
    print("Login Failed", e)
