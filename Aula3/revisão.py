# Aula 3 - Operadores relacionais, Expressões lógicas e tomadas de decisão de um programa

# Vamos fazer alguns exemplos:

wandinha = 13
emily_in_paris = 80
stranger_things = 55

print(wandinha > emily_in_paris) #false
print(stranger_things < wandinha) #false
print(wandinha == stranger_things) #false
print(emily_in_paris > stranger_things) #true

#Expressões lógicas
#not -> não ---> qualquer valor diferente de 0 a variável será true
#and -> e
#or -> ou

la_casa_de_papel = 36
bridgerton = 48
round_6 = 6
friends = 98
modern_family = 102
game_of_thrones = 0

print(not(friends))
print(not(game_of_thrones))

print((la_casa_de_papel > round_6)or(bridgerton < modern_family)) #true

print((friends == modern_family)and(la_casa_de_papel > modern_family)) #false

print(not(friends > round_6)) #false

print((bridgerton and game_of_thrones) or (la_casa_de_papel > game_of_thrones))#true
