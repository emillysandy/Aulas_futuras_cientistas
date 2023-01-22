valor_do_ingresso = 25
desconto = 50

print("Olá, bem-vindo ao Cine Dark!")
print("Estamos com uma promoção para todos pagarem meia no ingresso")
ingresso = int(input("Quantos ingressos você vai querer?\n"))
print("Espere um momento enquanto calculamos o valor do ingresso")
valor_total = valor_do_ingresso * ingresso
valor_com_desconto = valor_total - valor_total * (desconto/100)
print("O valor total dos seus ingressos é de: ", valor_total)
print("Mas com desconto ficará:", valor_com_desconto)

//tem como esperar um tempo entre "espere um momento..." até printar o valor na tela
//condição de desconto
//escolher o filme e o horario
//escolher a cadeira
//inserir compra de lanches
