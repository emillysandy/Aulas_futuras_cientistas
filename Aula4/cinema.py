# Nesta aula iremos exercitar os conceitos de múltiplas verificações

valor_do_ingresso = 25
desconto = 50
avatar =  1
gato_de_botas = 2
crepusculo = 3
dia = "segunda"
estudante = "sim"

print("Olá, bem-vindo ao Cine Dark!")
print("Esse são os filmes em cartaz:")
print("1- Avatar")
print("2- Gato de botas")
print("3 - Crepusculo")
filme = (input("Digite o número do filme que deseja assistir\n"))
  if filme == 1:
    print("O filme escolhido foi Avatar")
  elif filme == 2:
    print("O filme escolhido foi Gato de botas")
  else:
    print("O filme escolhido foi Crepusculo")
print("Estamos com uma promoção, na segunda todos pagam meia")
ingresso = int(input("Quantos ingressos você vai querer?\n"))
print("Espere um momento enquanto calculamos o valor do ingresso")
valor_total = valor_do_ingresso * ingresso
valor_com_desconto = valor_total - valor_total * (desconto/100)
print("O valor total dos seus ingressos é de: ", valor_total)
print("Mas com desconto ficará:", valor_com_desconto)

#condição de desconto
#escolher o filme e o horário
#escolher a cadeira
#inserir compra de lanches


# Segunda ou estudantes pagam meia no ingresso
