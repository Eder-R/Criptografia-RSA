from cryptography.fernet import Fernet
key = Fernet.generate_key() # GERA UMA CHAVE RANDÔMICA, COM BASE 64
with open('Chave.key', 'wb') as Chave:
  Chave.write(key)

# abrindo a chave
with open('Chave.key', 'rb') as filekey:
  key = filekey.read()

  # usando a chave gerada
  fernet = Fernet(key)

  # abrindo o arquivo original para criptografar
  with open('texto.txt', 'rb') as file:
    original = file.read()

  # criptografar o arquivo
  encrypted = fernet.encrypt(original)

  # abrir o arquivo no modo de gravação e
  # gravar os dados criptografados
  with open('texto_Criptografado.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
