import random

def generate_password(lenghtPassword=15):
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*"
    return ''.join(random.choice(CHARACTERS) for _ in range(lenghtPassword))
def write_file(service="Senha sem serviço especificado"):
    with open("Python\passwordPythonProject\passwords.txt", "a", encoding="utf-8") as passwordsFile:
        strPassword = generate_password()
        passwordsFile.write(f"{service}: {strPassword} \n")
    
def main():
    service = str(input("Digite o serviço onde a senha será usada: "))
    write_file(service)
    
if __name__ == "__main__":
    main()