#"Desenvolva um programa em Python que leia o primeiro nome de uma pessoa e seu salário do mês de abril e na sequência mostre uma mensagem formatada.(...)"
nome = input("Digite seu Primeiro Nome: ")

parte1nome = nome[0:20]

salario = input("Digite seu salario: ")

parte3salario = salario[0:1]
parte4salario = salario[1:4]
parte5salario = salario[4:6]

salarioFormatado = parte3salario + "." + parte4salario + "," + parte5salario

RECEBIMENTO = parte1nome + " no mês de abril recebeu um salario de R$" + salarioFormatado + " reais"

print(RECEBIMENTO)


