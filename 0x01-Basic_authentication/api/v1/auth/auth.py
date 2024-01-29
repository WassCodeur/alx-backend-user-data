#!/usr/bin/env python3
"""authentication module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auhentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication
        Arguments:
             - path: str
               excluded_paths: List of stirng
        Return:
             - bool
        """
        if path and path[-1] != '/':
            path = f"{path}/"
        if path is None or excluded_paths is None or\
                path not in excluded_paths:
            return True
        elif path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """authorization_header

        Arguments:
             - resquest

        Return:
            - str
        """
        if request is None:
            return None
        elif 'Authorization' not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user
        Arguments:
            - request
        Return:
            - TypeVar
        """
        return None
