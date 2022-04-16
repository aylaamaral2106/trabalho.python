#"Desenvolva um programa em Python que leia o primeiro nome de uma pessoa e seu salário do mês de abril e na sequência mostre uma mensagem formatada.(...)"
nome = input("Insira seu nome: ")

parte1nome = nome[0:10]

NomeFormatado = parte1nome + " recebeu um salario de: "

print(NomeFormatado)

salario = input("")

parte3salario = salario[0:1]
parte4salario = salario[1:4]
parte5salario = salario[4:6]

SalarioFormatado = parte3salario + "." + parte4salario + "," + parte5salario

print(SalarioFormatado)

"nome + salario" 


