import re

email=input("Enter your email address: ")

pattern=r"\b[a-zA-Z]+[a-zA-Z0-9_.-]+@[a-z]+[.](com|edu){2,}\b"
match_obj = re.match(pattern,email)
print(match_obj)
