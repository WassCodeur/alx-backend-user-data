#!/usr/bin/env python3
""" Main 5
"""
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = "wachioubouraima@gmail.com"
user_clear_pwd = str(uuid.uuid4())
user = User()
user.email = user_email
user.first_name = "wass"
user.last_name = "codeur"
user.password = user_clear_pwd
print("New user: {}".format(user.display_name()))
user.save()