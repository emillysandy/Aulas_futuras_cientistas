valor_do_ingresso = 25
desconto = 50
avatar = 1
gato_de_botas = 2
crepusculo = 3

print("Olá, bem-vindo ao Cine Dark!")
print("Esse são os filmes em cartaz:")
print("1- Avatar")
print("2- Gato de botas")
print("3 - Crepusculo")
filme = int(input("Digite o número do filme que deseja assistir\n"))
if filme == 1:
  print("O filme escolhido foi Avatar")
elif filme == 2:
  print("O filme escolhido foi Gato de botas")
else:
  print("O filme escolhido foi Crepusculo")
ingresso = int(input("Quantos ingressos você vai querer?\n"))
dia_da_semana = input("Qual o dia da semana?\n")
if (dia_da_semana == "segunda"):
  print("Estamos com uma promoção, todos pagam meia na segunda")
  valor_total = valor_do_ingresso * ingresso
  valor_com_desconto = valor_total - valor_total * (desconto / 100)
  print("O valor total dos seus ingressos é de: ", valor_total)
  print("Mas com desconto ficará:", valor_com_desconto)
else:
  estudante = input("Algum ingresso é de estudante? S/N\n")
  if estudante == "S":
    quantidade_estudante = int(input("Quantos ingressos de estudante?\n"))
    if quantidade_estudante == ingresso:
      valor_total = valor_do_ingresso * ingresso
      valor_com_desconto = valor_total - valor_total * (desconto / 100)
      print("O valor total dos seus ingressos é de: ", valor_total)
      print("Mas com desconto ficará:", valor_com_desconto)
    else:
      inteira = int(ingresso - quantidade_estudante)
      valor_com_desconto = quantidade_estudante * ingresso * (desconto / 100)
      valor_total = inteira * valor_do_ingresso + valor_com_desconto
      print("O valor total dos seus ingressos é de: ", valor_total)
  else:
    valor_total = ingresso * valor_do_ingresso
    print("O valor total dos seus ingressos é de: ", valor_total)
print("Bom filme!")
