username = "poulstar"
password = "123456"

input_username = input('enter your USERNAME: ')
input_password = input('enter your PASSWORD: ')

if input_username.lower() == username and input_password == password:
    print("Eyval Dorost Umadi!")
else:
    print("Password or User is incorrect!")