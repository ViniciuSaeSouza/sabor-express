numeros = [1,2,3,4,5,6,7,8,9,10]

nomes = ['Saes','Victor', 'Pablo', 'Gabriel']

ano_nascimento_atual = [1995, 2024]

for numero in numeros:
    print(f'Número: {numero}')


soma_numeros_impares = 0

for index in range(1, 11, 2):
     soma_numeros_impares += index
     print(index)
print(soma_numeros_impares)
# O segundo argumento de da função range é exclusivo, então range(1, 11) inclui números de 1 a 10) com um passo de 2 (o terceiro argumento de range). Isso garante que apenas números ímpares sejam considerados.
for index in range(10, 0, -1):
    print(index)

numero_escolhido_tabuada = int(input("Digite um número: "))

for index in range(1, 11, 1):
    resultado = numero_escolhido_tabuada * index
    print(f'O Resultado de {numero_escolhido_tabuada} X {index} é igual a = {resultado}')

lista_numeros = [10, 5, 8, 3, 7]
soma_dos_elementos = 0

try:
    for numero in lista_numeros:
        soma_dos_elementos += numero
    print(f'A soma dos elementos é: {soma_dos_elementos}')
except Exception as e:
    print(f'Ocorrou um erro {e}')
    

lista_numeros = [10, 5, 8, 3, 7]

soma_valores = 0

try:
    for numero in lista_numeros:
        soma_valores += numero
        media = soma_valores / len(lista_numeros)
    print(f'A média dos valores é: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média')
except Exception as e:
    print(f'Houve um erro: {e}')