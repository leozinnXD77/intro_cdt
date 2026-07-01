'''

modulo04_lista_leonardoSales.py

'''



while True:
 frutas_lista = ['banana', 'maçã', 'laranja', 'uva', 'abacaxi']
 print('🍉🍓' * 25 + '\n')

 print('\nbem-vindo a nossa loja de frutas!\n')

 print('aqui está a lista de frutas que temos disponíveis:\n')

 print(frutas_lista)

 fruta_nova = input('\nDigite o nome da fruta que deseja adicionar: ')

 frutas_lista.append(fruta_nova)

 print(f"\na fruta {fruta_nova} foi adicionada a lista de frutas!\n")

 print('aqui está a lista de frutas atualizada:\n')

 print(frutas_lista)

 print('🍉🍓' * 25 + '\n')
 break 