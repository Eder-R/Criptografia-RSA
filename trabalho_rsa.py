# -*- coding: UTF-8 -*-
import rsa_engine as rsa


import sys
if sys.version_info[0] < 3:
	print("Esse programa requer a versão \"Python 3\"\n\n")
	quit()

print("\nEncriptografia RSA.\n")
op = 1
while op:
	if op == 1:
		rsa.main()
		print('')
		op = -1
	
	op = input("entrar novo texto? (s/n): ")
	if bool(str.lower(op) == "s" or str.lower(op) == "n") == False:
		print("entrar \"s\" para \"sim\" ou \"n\" para \"não\"")
		op = -1
	elif str.lower(op) == "s":
		op = 1
	elif str.lower(op) == "n":
		print("programa encerrado\n\n")
		op = 0
