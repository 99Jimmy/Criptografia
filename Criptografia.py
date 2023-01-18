import numpy as np


def encrypt(frase):
  crypt = ""
  for e in frase:
    crypt = crypt + chr(ord(e) + s[0] * s[1])
  return crypt


def decrypt(enc):
  msg = ""
  for e in enc:
    msg = msg + chr(ord(e) - s[0] * s[1])
  return msg


ask = int(input("1-Criptografar / 2-Descriptografar: "))

if ask == 1:

  frase = input("Digite a mensagem ")
  Key_E = int(input("Crie uma chave "))
  np.random.seed(Key_E)
  s = np.random.randint(1, 100, size=2)
  print(encrypt(frase))
#   print(s)

elif ask == 2:

  enc = input("Digite a mensagem ")
  Key_D = int(input("Digite a senha "))
  np.random.seed(Key_D)
  s = np.random.randint(1, 100, size=2)
  print(decrypt(enc))
#   print(s)

else:
  print("Digite apenas 1 ou 2")
