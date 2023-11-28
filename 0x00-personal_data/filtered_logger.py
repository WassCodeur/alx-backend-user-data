#!/usr/bin/env python3
"""personal data"""
import logging
import re
from typing import List


def filter_datum(fields: List, redaction: str, message: str, separator: str):
    """log message obfuscated

    Arguments
    ---------
    fields: List
    redaction: str
    message: str
    separator: str

    Return
    ------
    """
    message_in_dict = {}
    paires = message.split(separator)
    for paire in paires:
        pair = paire.split('=')
        if len(pair) == 2:
            key, value = pair
        message_in_dict[key] = value

    for key in message_in_dict:
        if key in fields:
            obfuscated = re.sub(message_in_dict[key], f"{redaction}",
                                message_in_dict[key])
            message_in_dict[key] = obfuscated

    obfuscated_list = list(message_in_dict.items())

    obfuscated_message = separator.join([f"{key}={value}"
                                        for key, value in obfuscated_list])

    return obfuscated_message+separator
