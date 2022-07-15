from cryptography.fernet import Fernet

with open('Chave.key', 'rb') as filekey:
  key = filekey.read()

fernet = Fernet(key)

# abrindo o arquivo criptografado
with open('texto.txt', 'rb') as enc_file:
    encrypted = enc_file.read()

# descriptografando o arquivo
decrypted = fernet.decrypt(encrypted)

# abrindo o arquivo no modo de gravação e
# gravando os dados descriptografados
with open('texto_Descriptografado.txt', 'wb') as dec_file:
    dec_file.write(decrypted)