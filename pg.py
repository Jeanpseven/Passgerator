import itertools

def generate_passwords(min_length, max_length, has_letters, has_numbers, has_special_chars, has_uppercase, has_lowercase):
    chars = ""
    if has_letters:
        if has_uppercase:
            chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if has_lowercase:
            chars += "abcdefghijklmnopqrstuvwxyz"
    if has_numbers:
        chars += "0123456789"
    if has_special_chars:
        chars += "!@#$%^&*()_+=-{}[]<>?,./"

    passwords = []
    for length in range(min_length, max_length+1):
        for combination in itertools.product(chars, repeat=length):
            passwords.append("".join(combination))
    
    return passwords

# Obter critérios do usuário
min_length = int(input("Digite a quantidade mínima de caracteres: "))
max_length = int(input("Digite a quantidade máxima de caracteres: "))
has_letters = input("A senha deve conter letras? (s/n): ").lower() == "s"
has_uppercase = input("A senha deve conter letras maiúsculas? (s/n): ").lower() == "s"
has_lowercase = input("A senha deve conter letras minúsculas? (s/n): ").lower() == "s"
has_numbers = input("A senha deve conter números? (s/n): ").lower() == "s"
has_special_chars = input("A senha deve conter caracteres especiais? (s/n): ").lower() == "s"
output_file = input("Digite o nome do arquivo de saída: ")

# Gerar as senhas
passwords = generate_passwords(min_length, max_length, has_letters, has_numbers, has_special_chars, has_uppercase, has_lowercase)

# Salvar as senhas no arquivo de saída
with open(output_file, "w") as file:
    for password in passwords:
        file.write(password + "\n")

print("Senhas geradas e salvas com sucesso!")
