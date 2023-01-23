idade = int(input("Qual sua idade? \n"))

if idade < 18:
  if (idade < 10 and idade > 5):
    print("Você deverá pegar a pulseira de cor vermelha")
  elif idade < 5:
    print("Você deverá pegar a pulseira de cor azul")
  else:
    print("Você deverá pegar a pulseira de cor verde")
else:
  if (idade < 20):
    print("Você deverá pegar a pulseira de cor rosa")
  elif (idade > 20 and idade < 45):
    print("Você deverá pegar a pulseira de cor preta")
  elif (idade > 45 and idade < 60):
    print("Você deverá pegar a pulseira de cor laranja")
  else:
    print("Você deverá pegar a pulseira de cor branca")
