desconto = 20
preco_pizza = 30

print("Olá, meu nome é Ada!")
cliente = input("Como você se chama?\n")
print(cliente, ", seja bem-vindo(a) à Pizzaria Ada Lovelace!")
print("Estamos com uma promoção imperdível.")
print("Qualquer pedido hoje tem", desconto, "% de desconto")

numero_de_pizzas = int(input("De quantas pizzas você gostaria?\n"))

print("Excelente escolha!")
print("Agora, deixe-me calcular o valor total do seu pedido")

total = numero_de_pizzas*preco_pizza
total_com_desconto = total - total*(desconto/100)

print("O preço total do seu pedido é R$", total, ",00")
print("mas com o desconto exclusivo de ", desconto "%")
print("o valor total do seu pedido fica em R$", total_com_desconto)
