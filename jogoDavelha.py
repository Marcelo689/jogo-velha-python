import random

roboCaractere = "[o]"

def TentarVencer():
    if(SePossivelRetornaIndiceVitoria(0, campo[0],3 ,campo[3],6 ,campo[6]) != -1): #vertical 1
        indiceCampeao = SePossivelRetornaIndiceVitoria(0, campo[0],3 ,campo[3],6 ,campo[6])
        campo[indiceCampeao] = roboCaractere
    elif(SePossivelRetornaIndiceVitoria(1, campo[1],4 , campo[4], 7 , campo[7]) != -1): #vertical 2
        indiceCampeao = SePossivelRetornaIndiceVitoria(1, campo[1],4 , campo[4], 7 , campo[7])
        campo[indiceCampeao] = roboCaractere
    elif(SePossivelRetornaIndiceVitoria(2, campo[2],5 , campo[5], 8 ,campo[8]) != -1): #vertical 3
        indiceCampeao = SePossivelRetornaIndiceVitoria(2, campo[2],5 , campo[5], 8 ,campo[8])
        campo[indiceCampeao] = roboCaractere
    elif(SePossivelRetornaIndiceVitoria(0, campo[0],1 ,campo[1],2 ,campo[2]) != -1): #horizontal 1
        indiceCampeao = SePossivelRetornaIndiceVitoria(0, campo[0],1 ,campo[1],2 ,campo[2])
        campo[indiceCampeao] = roboCaractere
    elif(SePossivelRetornaIndiceVitoria(3, campo[3], 4,campo[4],5 ,campo[5]) != -1): #horizontal 2
        indiceCampeao = SePossivelRetornaIndiceVitoria(3, campo[3], 4,campo[4],5 ,campo[5])
        campo[indiceCampeao] = roboCaractere
    elif(SePossivelRetornaIndiceVitoria(6, campo[6],7 ,campo[7],8 ,campo[8]) != -1): #horizontal3 3
        indiceCampeao = SePossivelRetornaIndiceVitoria(6, campo[6],7 ,campo[7],8 ,campo[8])
        campo[indiceCampeao] = roboCaractere
    elif(SePossivelRetornaIndiceVitoria(0, campo[0],4 ,campo[4],8 ,campo[8]) != -1): #diagonal esquerda
        indiceCampeao = SePossivelRetornaIndiceVitoria(0, campo[0],4 ,campo[4],8 ,campo[8])
        campo[indiceCampeao] = roboCaractere
    elif(SePossivelRetornaIndiceVitoria(2 ,campo[2],4 , campo[4], 6 , campo[6]) != -1): #diagonal direita
        indiceCampeao = SePossivelRetornaIndiceVitoria(2 ,campo[2],4 , campo[4], 6 , campo[6])
        campo[indiceCampeao] = roboCaractere
    else:
        return False
    
    return True

indiceVazio = "[ ]"
def TurnoRobo(indices):

    venceu = TentarVencer()

    if(not venceu):
        
        if(TentarImpedirVitoria(jogador1, campo[0], campo[3], campo[6])): #vertical 1
            PreencherCelulaP1PoderiaVencer(0, campo[0],3 ,campo[3],6 ,campo[6])

        elif(TentarImpedirVitoria(jogador1 , campo[1], campo[4], campo[7])):#vertical 2
            PreencherCelulaP1PoderiaVencer(1, campo[1],4 , campo[4], 7 , campo[7])

        elif(TentarImpedirVitoria(jogador1, campo[2], campo[5], campo [8])):#vertical 3
            PreencherCelulaP1PoderiaVencer(2, campo[2],5 , campo[5], 8 ,campo[8])

        elif(TentarImpedirVitoria(jogador1, campo[0], campo[1], campo [2])):#horizontal 1
            PreencherCelulaP1PoderiaVencer(0, campo[0],1 ,campo[1],2 ,campo[2])

        elif(TentarImpedirVitoria(jogador1, campo[3], campo[4], campo [5])):#horizontal 2
            PreencherCelulaP1PoderiaVencer(3, campo[3], 4,campo[4],5 ,campo[5])

        elif(TentarImpedirVitoria(jogador1, campo[6], campo[7], campo [8])):#horizontal 3
            PreencherCelulaP1PoderiaVencer(6, campo[6],7 ,campo[7],8 ,campo[8])

        elif(TentarImpedirVitoria(jogador1 ,campo[0], campo[4], campo [8])):#diagonal esquerda
            PreencherCelulaP1PoderiaVencer(0, campo[0],4 ,campo[4],8 ,campo[8])

        elif(TentarImpedirVitoria(jogador1, campo[2], campo[4], campo [6])):#diagonal direita
            PreencherCelulaP1PoderiaVencer(2 ,campo[2],4 , campo[4], 6 , campo[6])

        else:
            PreencherCelulaAleatoriamente(indices)
    

def PreencherCelulaAleatoriamente(indices):
    indiceAleatorio = random.choice(indices)
    campo[indiceAleatorio] = "["+jogador2+"]"

def PreencherCelulaP1PoderiaVencer(n1i, n1, n2i, n2, n3i, n3):
    if(indiceVazio == n1 and n1 != "[o]" and n1 != "["+jogador1+"]"):
        campo[n1i] = "["+jogador2+"]"
    elif(indiceVazio == n2 and n2 != "[o]" and n2 != "["+jogador1+"]"):
        campo[n2i] = "["+jogador2+"]"
    elif(indiceVazio == n3  and n3 != "[o]" and n3 != "["+jogador1+"]"):
        campo[n3i] = "["+jogador2+"]"

def SePossivelRetornaIndiceVitoria(n1i, n1,n2i, n2,n3i, n3):
    contador = 0

    indiceVitoria = -1
    if(roboCaractere == n1):
        contador += 1
    else:
        indiceVitoria = n1i

    if(roboCaractere == n2):
        contador += 1
    else:
        indiceVitoria = n2i
    if(roboCaractere == n3):
        contador += 1
    else:
        indiceVitoria = n3i
    
    if(contador == 2 and ( n1 or n2 or n3)):
        return indiceVitoria
    else:
        return -1
def TentarImpedirVitoria(jogador, n1, n2, n3):
    contador = 0 
    # o x o
    # x o x
    # x x x
    # o o o
    roboCaractere = "[o]"
    
    if(n1 == roboCaractere):
        return False
    elif n2 == roboCaractere:
        return False
    elif n3 == roboCaractere:
        return False
    
    if("["+jogador+"]" == n1 and n1 != roboCaractere):
        contador += 1
    if("["+jogador+"]" == n2 and n2 != roboCaractere):
        contador += 1
    if("["+jogador+"]" == n3 and n3 != roboCaractere):
        contador += 1
    return contador >=2


def indicesDisponiveis():
    indices = [] 

    for indice  in range(len(campo)):
        if(campo[indice] == "[ ]"):
            indices.append(indice)

    return indices

def RoboJoga():
    indices = indicesDisponiveis()

    if(len(indices) > 0):
        TurnoRobo(indices)


def imprimeCampo():
    contador = 0
    for indice in campo:
        if(contador == 3):
            print("")
            contador = 0
        contador += 1
        print(indice, end="")

def checkSeJogadorNaoVenceu(jogadorATeste, retorno):
    retorno = True
    jogadorATeste = "["+jogadorATeste+"]"
    if(jogadorATeste == campo[0] == campo[3] == campo [6]): #vertical 1
        retorno = False
    elif(jogadorATeste == campo[1] == campo[4] == campo [7]):#vertical 2
        retorno = False
    elif(jogadorATeste == campo[2] == campo[5] == campo [8]):#vertical 3
        retorno = False
    elif(jogadorATeste == campo[0] == campo[1] == campo [2]):#horizontal 1
        retorno = False
    elif(jogadorATeste == campo[3] == campo[4] == campo [5]):#horizontal 2
        retorno =  False
    elif(jogadorATeste == campo[6] == campo[7] == campo [8]):#horizontal 3
        retorno = False
    elif(jogadorATeste == campo[0] == campo[4] == campo [8]):#diagonal esquerda
        retorno = False
    elif(jogadorATeste == campo[2] == campo[4] == campo [6]):#diagonal direita
        retorno = False
    return retorno

def ninguemVenceu():
    retorno = True

    retorno = checkSeJogadorNaoVenceu(ultimoQueJogou, retorno)
    if not retorno:
        return retorno
    
    retorno = checkSeJogadorNaoVenceu(jogador2, retorno)
    
    return retorno
    
def trocarJogador():
    if(ultimoQueJogou == jogador1):
        return jogador2
    else:
        return jogador1

campo = [
    "[ ]","[ ]","[ ]",
    "[ ]","[ ]","[ ]",
    "[ ]","[ ]","[ ]",
]

jogadorVencedor = "ninguem"

jogador1 = input("Escolha entre ( x , o ): ")
entrada  = input("Digite 1 para jogar contra robo e qualquer outra coisa para jogar contra uma pessoa\n")

ultimoQueJogou = jogador1 

jogador2 = "x"

if(jogador1 == "x"):
    jogador2 = "o"

robo = False

if(entrada == "1"):
    robo = True

proximoAJogar = jogador1
velha = False
while(ninguemVenceu()):
    
    if(not campo.__contains__("[ ]")):
        velha = True
        break
    print(proximoAJogar, "jogando")
    imprimeCampo()
    indiceJogada = int(input("\nescolha seu indice de 0 a 8 =  "))
    if(campo[indiceJogada] == "[ ]"):
        campo[indiceJogada] = "[" +proximoAJogar+ "]"
        ultimoQueJogou = proximoAJogar
        
        if(robo):
            RoboJoga()
        else:
            proximoAJogar = trocarJogador()
    else:
        print("Você digitou um indice inválido tente novamente")


imprimeCampo()
if(velha):
    print("\nDeu velha!!!! 😢😢😢😢")
else:
    print("\n",ultimoQueJogou," Venceu!!! 😁😁👍😉")