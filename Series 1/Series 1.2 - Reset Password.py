print ("Reset password... ")
print ("Password must be longer then 8 and use captials and lowercase")
#tells user conditions for password
print ()
password1 = input("Enter new password: ")
#user enters new password once
password = input ("Enter new password again: ")
#use enters new password again

if password1 != password:
    print("""Doesn't match. Try Again.""")
#compares 2 entered passwords to check they are the same
elif len(password) <8:
    print ("Password is too short.")
#if password is too short has to start again
else:
    password.lower()== password and password.upper()==password
    print ("Password meets conditions.")
#only accepts password if it meets conditions
