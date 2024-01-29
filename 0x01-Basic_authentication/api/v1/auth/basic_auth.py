#!/usr/bin/env python3
"""Basic authentication"""

from api.v1.auth.auth import Auth
from base64 import *
from typing import TypeVar

class BasicAuth(Auth):
    """basic auth class inherit from
    Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if authorization_header is None or\
                type(authorization_header) is not str:
            return None
        else:
            auth_header = authorization_header.split(" ")
            if auth_header[0] == "Basic":
                return auth_header[1]
            else:
                return None

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if base64_authorization_header is None or type(base64_authorization_header) is not str:
            return None
        else:
            try:
               b64_to_b = b64decode(base64_authorization_header)
               return b64_to_b.decode('utf-8')
            except Exception:
                return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        #pattern = (r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+:[a-zA-Z0-9_.+-]+$')
        pattern = r":?"
        if decoded_base64_authorization_header is None or type(decoded_base64_authorization_header) is not str:
            return (None, None)
        else:
            #if re.search(pattern, decoded_base64_authorization_header):
            if decoded_base64_authorization_header.count(':') == 1:
                to_list = decoded_base64_authorization_header.split(":")
                return tuple(to_list)
                #return (to_list[0], to_list[1])
            else:
                return (None, None)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        if user_email is None or type(user_email) is not str or user_pwd is None or type(user_pwd) is not str:
            return None

