from random import choice
from time import sleep

print("Seja bem-vindo ao jogo da forca!")
press = int(input("Pressione 1 para iniciar o game"))
if press==1:
    print("iniciando o game aguarde...")
    sleep(2)
else:
    while press != 1:
        print("Essa opção não existe, meu caro Watson!")
        press=int(input("Pressone 1 para iniciar o game"))
        sleep(2)

continuar = "s"
while True:
    tema = int(input("Temas: \n1 - Goiaba\n2 - Manga\n3 - Morango\n4 - Abacaxi: "))
    if tema==1:
            n1='goiaba'
            n2='manga'
            n3='morango'
            n4='abacaxi'
            ways=[n1,n2,n3,n4]
            print('começando a rodada do tema: "Frutas"')
            sleep(2)
            es=choice(ways)
            if es==n1:
                while es==n1:
                    res=input('Chute a letra: ')
                    if res=="g":
                        print("G-----")
                        cht=input('Deseja chutar a resposta?[s] ou [n] ')
                        if cht=='s':
                            rp1=input('Qual resposta? ')
                            if rp1==n1:
                                print('Acertou!')
                                exit()
                            elif rp1!=n1:
                                print('Que triste... você errou!')
                                exit()

                    elif res=="o":
                        print("-O----")
                        cht1=input('Deseja chutar a resposta?[s] ou [n] ')
                        if cht1=='s':
                            rp1=input('Qual resposta? ')
                            if rp1==n1:
                                print('Acertou!')
                                exit()
                            elif rp1!=n1:
                                print('Que triste... você errou!')
                                exit()

                    elif res=="i":
                        print('--I---')
                        cht1=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht1=='s':
                            rp1=input('Qual resposta? ')
                            if rp1==n1:
                                print('acertou!')
                                exit()
                            elif rp1!=n1:
                                print('Que triste... você errou!')
                                exit()

                    if res=="a":
                        print('---A-A')
                        cht1=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht1=='s':
                            rp1=input('Qual resposta? ')
                            if rp1==n1:
                                print('Acertou!')
                                exit()
                            elif rp1!=n1:
                                print('Que triste... você errou!')
                                exit()

                        elif res=="b":
                            print('----B-')
                            cht1=input('Deseja chutar a resposta?[s] ou [n]  ')
                            if cht1=='s':
                                rp1=input('Qual resposta? ')
                                if rp1==n1:
                                    print('Acertou!')
                                exit()
                            elif rp1!=n1:
                                print('Que triste... você errou!')
                                exit()
                else:
                    print("Não há essa letra")
            if es==n2: 
                while es==n2:
                    res=input('Chute a letra: ')
                    if res=="m":
                        print("M----")
                        cht2=input('Deseja chutar a resposta?[s] ou [n] ')
                        if cht2=='s':
                            rp2=input('Qual resposta? ')
                            if rp2==n2:
                                print('Acertou!')
                                exit()
                            elif rp2!=n2:
                                print('Que triste... você errou!')
                                exit()

                    elif res=="a":
                        print("-A--A")
                        cht2=input('Deseja chutar a resposta?[s] ou [n] ')
                        if cht2=='s':
                            rp2=input('Qual resposta? ')
                            if rp2==n2:
                                print('Acertou!')
                                exit()
                            elif rp2!=n2:
                                print('Que triste... você errou!')
                                exit()

                    elif res=="g":
                        print('---G-')
                        cht2=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht2=='s':
                            rp2=input('Qual resposta? ')
                            if rp2==n2:
                                print('acertou!')
                                exit()
                            elif rp2!=n2:
                                print('Que triste... você errou!')
                                exit()

                    elif res=="n":
                        print('--N--')
                        cht2=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht2=='s':
                            rp2=input('Qual resposta? ')
                            if rp2==n2:
                                print('Acertou!')
                                exit()
                            elif rp2!=n2:
                                print('Que triste... você errou!')
                                exit()

                else:
                    print("Não há essa letra")
            if es==n3: 
                while es==n3:
                    res=input('Chute a letra: ')
                    if res=="m":
                        print("M------")
                        cht3=input('Deseja chutar a resposta?[s] ou [n] ')
                        if cht3=='s':
                            rp3=input('Qual resposta? ')
                            if rp3==n3:
                                print('Acertou!')
                                exit()
                            elif rp3!=n3:
                                print('Que triste... você errou!')
                                exit()
                    elif res=="o":
                        print("-O----O")
                        cht3=input('Deseja chutar a resposta?[s] ou [n] ')
                        if cht3=='s':
                            rp3=input('Qual resposta? ')
                            if rp3==n3:
                                print('Acertou!')
                                exit()
                            elif rp3!=n3:
                                print('Que triste... você errou!')
                                exit()
                    elif res=="r":
                        print('--R----')
                        cht3=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht3=='s':
                            rp3=input('Qual resposta? ')
                            if rp3==n3:
                                print('acertou!')
                                exit()
                            elif rp3!=n3:
                                print('Que triste... você errou!')
                                exit()
                    elif res=="a":
                        print('---A---')
                        cht3=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht3=='s':
                            rp3=input('Qual resposta? ')
                            if rp3==n3:
                                print('Acertou!')
                                exit()
                            elif rp3!=n3:
                                print('Que triste... você errou!')
                                exit()
                    elif res=="n":
                        print('----N--')
                        cht3=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht3=='s':
                            rp3=input('Qual resposta? ')
                            if rp3==n3:
                                print('Acertou!')
                                exit()
                            elif rp3!=n3:
                                print('Que triste... você errou!')
                                exit()
                    elif res=="g":
                        print('-----G-')
                        cht3=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht3=='s':
                            rp3=input('Qual resposta? ')
                            if rp3==n3:
                                print('Acertou!')
                                exit()
                            elif rp3!=n3:
                                print('Que triste... você errou!')
                                exit()                        
                else:
                    print("Não há essa letra")
                if es==n4: 
                    while es==n4:
                        res=input('Chute a letra: ')
                    if res=="a":
                        print("A-A-A--")
                        cht4=input('Deseja chutar a resposta?[s] ou [n] ')
                        if cht4=='s':
                            rp4=input('Qual resposta? ')
                            if rp4==n4:
                                print('Acertou!')
                                exit()
                            elif rp4!=n4:
                                print('Que triste... você errou!')
                                exit()
                    elif res=="b":
                        print("-B-----")
                        cht4=input('Deseja chutar a resposta?[s] ou [n] ')
                        if cht4=='s':
                            rp4=input('Qual resposta? ')
                            if rp4==n4:
                                print('Acertou!')
                                exit()
                            elif rp4!=n4:
                                print('Que triste... você errou!')
                                exit()
                    elif res=="c":
                        print('----C---')
                        cht4=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht4=='s':
                            rp4=input('Qual resposta? ')
                            if rp4==n4:
                                print('acertou!')
                                exit()
                            elif rp4!=n4:
                                print('Que triste... você errou!')
                                exit()
                    elif res=="x":
                        print('-----X-')
                        cht4=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht4=='s':
                            rp4=input('Qual resposta? ')
                            if rp4==n4:
                                print('Acertou!')
                                exit()
                            elif rp4!=n4:
                                print('Que triste... você errou!')
                                exit()
                    elif res=="i":
                        print('------I')
                        cht4=input('Deseja chutar a resposta?[s] ou [n]  ')
                        if cht4=='s':
                            rp4=input('Qual resposta? ')
                            if rp4==n4:
                                print('Acertou!')
                                exit()
                            elif rp4!=n4:
                                print('Que triste... você errou!')
                                exit()
                                            
                    else:
                        print("Não há essa letra")
    continuar = str(input("Deseja continuar? [S/N] ")[0]
    if continuar is 'Nn':
    break