"""
Faça um programa que leia a idade de uma pessoa e imprima as seguintes saídas:

É obrigado a votar - se idade for maior igual a 18 e menor igual a 60
Não é obrigado a votar - se idade for maior igual a 16 ou idade maior que 60
Não pode votar - se for menor de 16
"""

idade = int(input('digite a sua idade '))
 
if idade >= 18 and idade <= 60:  # 18 <= idade <= 60
    print('É obrigado a votar ')

elif idade >= 16 or idade > 60:
    print('Não é obrigatório votar ')

else: 
    print('Não pode votar ')