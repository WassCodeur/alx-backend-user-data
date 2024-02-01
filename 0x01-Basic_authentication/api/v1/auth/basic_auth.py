#!/usr/bin/env python3
"""Basic authentication"""

from api.v1.auth.auth import Auth
from base64 import *
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """basic auth class inherit from
    Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """to extract base64 authorization header

        Arguments
           - authorization_header: str

        Return
           - str
        """
        if authorization_header is None or\
                type(authorization_header) is not str:
            return None
        else:
            auth_header = authorization_header.split(" ")
            if auth_header[0] == "Basic":
                return auth_header[1]
            else:
                return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """decode base64 authorization header
        Arguments
           - base64_authorization_header: str
        Return
           - str
        """
        if base64_authorization_header is None or \
                type(base64_authorization_header) is not str:
            return None
        else:
            try:
                b64_to_b = b64decode(base64_authorization_header)
                return b64_to_b.decode('utf-8')
            except Exception:
                return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """decode base64 authorization header

        Arguments
            - decoded_base64_authorization_header: str
        Return
            - str
        """
        ptr = (r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+:[a-zA-Z0-9_.+-]+$')

        if decoded_base64_authorization_header is None\
                or type(decoded_base64_authorization_header) is not str:
            return (None, None)
        else:
            """if re.search(pattern, decoded_base64_authorization_header):"""
            if decoded_base64_authorization_header.count(':') == 1:
                to_list = decoded_base64_authorization_header.split(":")
                return tuple(to_list)
            else:
                return (None, None)

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """user object from credentials

        Arguments
            - user_email: str
            - user_pwd: str
        Return
            - TypeVar('User')
        """
        if user_email is None or type(user_email) is not str or\
                user_pwd is None or type(user_pwd) \
                is not str or not User.search({"email": user_email}):
            return None
        else:
            result = User.search({"email": user_email})
            if result[0].is_valid_password(user_pwd):
                return result[0]
            else:
                return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user

        Arguments
            - request: request
        Return:
            - TypeVar('User')
        """
        auth = self.authorization_header(request)
        if auth:
            b64_auth = self.extract_base64_authorization_header(auth)
            if b64_auth:
                b64_decode = self.decode_base64_authorization_header(b64_auth)
                if b64_decode:
                    user_crd = self.extract_user_credentials(b64_decode)
                    if len(user_crd) == 2:
                        user = self.user_object_from_credentials(user_crd[0],
                                                                 user_crd[1])
                        return user
