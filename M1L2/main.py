import random 
possivel = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

user = int(input("Quantos caracteres deseja na senha?:"))

password = ""
for i in range(user):
    password += random.choice(possivel)

print(password)

