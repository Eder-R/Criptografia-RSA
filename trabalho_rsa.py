# -*- coding: UTF-8 -*-
import rsa_engine as rsa
import cripto as cri


import sys
if sys.version_info[0] < 3:
	print("Esse programa requer a versão \"Python 3\"\n\n")
	quit()

print("\nEncriptografia RSA.\n")
cri.main()
print('')
