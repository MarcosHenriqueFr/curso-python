# Constantes são em maiusculo -> Esse conceito não existe em python na linguagem
# Muitas condicoes é ruim
# Contagem de complexidade é ruim -> mais [tab]eado

velocidade = 70.5
posicao_carro = 162

LOCAL_RADAR = 160
RADAR_1 = 60
RADAR_RANGE = 5

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = posicao_carro >= (LOCAL_RADAR - RADAR_RANGE) and \
                       posicao_carro <= (LOCAL_RADAR + RADAR_RANGE)
carro_multado = velocidade_carro_passou_radar_1 and carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade carro passou da do radar 1')

if carro_multado:
    print('Carro foi multado')