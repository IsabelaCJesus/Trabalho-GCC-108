import pandas as pd
entradaArq = pd.read_csv('exemplo2.CSV')
for row in entradaArq:
    dado = row
dado = list(dado.split(';'))

dado[0] = int(dado[0],2) #primeiro valor da entrada (em decimal)
dado[1] = int(dado[1],2) #segundo valor da entrada (em decimal)

valor1 = "1"
for i in range(dado[0]):
    valor1 = valor1 + "1" #primeiro valor da entreada (em unário)

valor2 = "1"
for i in range(dado[1]):
    valor2 = valor2 + "1"
    
entrada = valor1 + '0' + valor2 #segundo valor da entreada (em unário)

fita3 = entrada     #entrada
 
configuracao = "0001011101101110110011011011011011001101110111011011001110110111011011001110111011110111010011110110111110111010011111011011111101110100111111011011111101101"
maquina = configuracao.split("000")

maquina2 = maquina[1] # configuraçao da maquina

transicoes = maquina2.split("00") #transicoes

fita1 = transicoes  #transicoes
fita2 = "1"         #estado inicial
D = "1"             #direcao direita da maquina 
E = "11"            #direcao esquerda da maquina 
