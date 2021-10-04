import re

def password_val(password):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    c_pass = re.compile(regex)
    matrix = re.search(c_pass, password)

    return matrix
