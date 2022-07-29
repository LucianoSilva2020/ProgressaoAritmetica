primeiro = int(input('Primeiro termo Nº:'))
razao = int(input('Razão Nº:'))
decimo = primeiro + (10 - 1) * razao
for var in range (primeiro, decimo + razao, razao):
    print(f'{var}', end='→ ')
print('ACABOU')    