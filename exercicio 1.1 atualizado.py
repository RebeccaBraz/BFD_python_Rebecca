# # 1-Conversor de Temperatura


# #Menu com duas opções


print ("Conversor de Temperatura")
print("Escolha uma opção:")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")


# #O usuário escolhe a opção digitando um número


opcao = int(input("Digite sua opção (1 ou 2): "))


# #Opção 1 Celsius para Fahrenheit


if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("A temperatura em Fahrenheit é:", fahrenheit)


# #Opção 2 Fahrenheit para Celsius


elif opcao == 2:
     fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
     celsius = (fahrenheit - 32) * 5/9
     print("A temperatura em Celsius é:", celsius)
