import secrets
import string
# define the alphabet
letters=string.ascii_letters
digits=string.digits
special_chars=string.punctuation
alphabet=letters+digits+special_chars
# fix password length
password_length=10
# generate a password string
password=''
for i in range(password_length):
  password +=''.join(secrets.choice(alphabet))
print(password)
# generate password meeting constraints
while True:
  password= ''
  for i in range(password_length):
    password +=''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in password) and 
      sum(char in digits for char in password)>=2):
          break
print(password)
