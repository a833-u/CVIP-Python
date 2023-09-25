import random
def generate_password(length=12, character_types="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"):
  password = ""
  for i in range(length):
    password += random.choice(character_types)
  return password
def main():
  password_length = int(input("Enter the desired password length: "))
  character_types = input("Enter the desired character types (e.g. abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()): ")
  password = generate_password(password_length, character_types)
  print("Your generated password is:", password)
if __name__ == "__main__":
  main()