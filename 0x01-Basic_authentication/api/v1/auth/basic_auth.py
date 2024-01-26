#!/usr/bin/env python3
"""Basic authentication"""

from api.v1.auth.auth import Auth
from base64 import *

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
