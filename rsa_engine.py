# -*- coding: UTF-8 -*-
import random


file = open('./file.txt', 'r')
file = file.read()

'''
Calcula o totiente do numero primo
'''

def totient(number): 
    if(prime(number)):
        return number-1
    else:
        return False

'''
Verifica se um numero gerado é primo
'''

def prime_velho(n): # não é o melhor método
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True

def prime(n): # outro método
    result = True
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:  
                # não é primo
                result = False
                break
            #else:
                # é primo
                pass
    else:  
        # não é primo
        result = False

    return result

'''
Gera um numero aleatório E, satisfazendo as condições
'''

def generate_E(num): 
    def mdc(n1,n2):
        rest = 1
        while(n2 != 0):
            rest = n1%n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e

'''
Gera um numero primo aleatório
'''

def generate_prime(): # generate the prime number - p e q
    while True: # 2**2048 is the RSA standard keys
        x=random.randrange(1,100) # define the range of the primes
        if(prime(x)==True):
            return x

'''
Função modular entre dois números
'''

def mod(a,b): # mod function
    if(a<b):
        return a
    else:
        c=a%b
        return c

'''
Cifra um texto
'''

def cipher(file,e,n):
    tam = len(file)
    i = 0
    lista = []
    while(i < tam):
        letter = file[i]
        k = ord(letter)
        k = k**e
        d = mod(k,n)
        lista.append(d)
        i += 1
    return lista

'''
Descriptografa um texto criptografado
'''
def descifra(cifra,n,d):
    lista = []
    i = 0
    tamanho = len(cifra)
    # texto=cifra ^ d mod n
    while i < tamanho:
        result = cifra[i]**d
        texto = mod(result,n)
        letra = chr(texto)
        lista.append(letra)
        i += 1
    return lista

'''
Calcula a chave privada
'''
def calculate_private_key(toti,e):
    d = 0
    while(mod(d*e,toti)!=1):
        d += 1
    return d

'''
principal/main
'''
def main():
    text = file
    p = generate_prime() # generates random P
    q = generate_prime() # generates random Q
    n = p*q # compute N
    y = totient(p) # compute the totient of P
    x = totient(q) # compute the totient of Q
    totient_de_N = x*y # compute the totient of N
    e = generate_E(totient_de_N) # generate E
    public_key = (n, e)

    print('Chave pública:', public_key)
    text_cipher = cipher(file,e,n)
    print('Mensagem encriptada:', text_cipher)
    d = calculate_private_key(totient_de_N,e)
    print('Mensagem desencriptada:', d)
    original_text = descifra(text_cipher,n,d)
    print('Mensagem original:', original_text) 


'''
chamando função principal/main
'''
if __name__ == '__main__':
    main()
