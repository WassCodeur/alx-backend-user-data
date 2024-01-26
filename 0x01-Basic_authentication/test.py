import re

#pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+:[a-zA-Z0-9_]+$'
#pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+:[a-zA-Z0-9_]+$'
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+:[a-zA-Z0-9_.+-]+$'

# Exemples de tests
tests = [
    "utilisateur@example.com:Adentifiant_123",
    "john.doe123@example-domain.com:ano$her_id",
    "test.email@example-domain.:my_id_456",
    "invalid-email-address",  # Cette entrée ne correspond pas au motif
    "email@domain.com:invalid_id",  # Cette entrée ne correspond pas au motif
    "bob@gmail.com:toto1234"
]

for test in tests:
    if re.match(pattern, test):
        print(f"{test} est une correspondance valide.")
    else:
        print(f"{test} ne correspond pas au motif.")

