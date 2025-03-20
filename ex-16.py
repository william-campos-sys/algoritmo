# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra. 
# 1- Ler a quantidade de maças compradas
# 2 -Identificar se foram compradas menos de uma dúzia
# 2.1 - Caso tenha comprado mais de uma dúzia utilize o valor de R$1,00 para calcular e se for menos de uma dúzia utilize o valolr de R$1,30
int(input("quantas maças foram compradas"))
macasCompradas = int(input())
preco = 0
if(macasCompradas >=12):
    print("custa 1,00 a unidade!")
    preco = 1.0
else:
    print("custa 1,30 a unidade!")
    preco = 1.3
precoFinal = macasCompradas * preco
print("o preço final é: ",precoFinal)
