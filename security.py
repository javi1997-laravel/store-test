from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
	user = UserModel.find_by_username(username)
	if user and safe_str_cmp(user.password, password):
		return user

def identify(payload):
	user_id = payload['identity']
	return UserModel.find_by_id(user_id)
    
# "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDQ4NDcyOTUsImlhdCI6MTYwNDg0Njk5NSwibmJmIjoxNjA0ODQ2OTk1LCJpZGVudGl0eSI6MX0.R-PYo4R7olPYV12Zvhb5SKwPD2pfXfr4kd5o0YMeFu8"




