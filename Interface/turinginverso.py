import pygame as pg
import math
import random
import protMqtt as mqtt
import graficos as graf
import time
import pygame
from pygame import display, event, font 
from pygame.image import load
from playsound import playsound


#Botão circular
class Button:
    def __init__(self, xpos, ypos, sizex,sizey, color_light, color_dark,text,circle):
        self.xpos = xpos
        self.ypos = ypos
        self.sizex = sizex
        self.sizey = sizey
        self.color_light = color_light
        self.color_dark = color_dark
        self.text = text
        self.circle = circle

    def putText(self,tela):
        if self.circle:
            tela.blit(self.text,(self.xpos-12,self.ypos-15))
        else:
            tela.blit(self.text,(self.xpos+8,self.ypos+15))
    #Para botões circulares sizex=sizey=raio
    def isOver(self,mouse):
        if self.circle:
            if math.sqrt((self.xpos-mouse[0])**2+(self.ypos-mouse[1])**2)<self.sizex:
                return True
            else:
                return False
        else:
            if (self.xpos<mouse[0]<self.xpos+self.sizex and self.ypos<mouse[1]<self.ypos+self.sizey):
                return True
            else:
                return False
    def drawLight(self,tela):
        if self.circle:
            pg.draw.circle(tela,self.color_light,(self.xpos,self.ypos),self.sizex)
        else:
            pg.draw.rect(tela,self.color_light,[self.xpos,self.ypos,self.sizex,self.sizey])
    def drawDark(self,tela):
        if self.circle:
            pg.draw.circle(tela,self.color_dark,(self.xpos,self.ypos),self.sizex)
        else:
            pg.draw.rect(tela,self.color_dark,[self.xpos,self.ypos,self.sizex,self.sizey])



pg.init()

#Cria tela
width = 640
height =480
tela = display.set_mode(size=(width, height))
display.set_caption("Turing Inverso")

#Imagem de fundo
fundoInicio = load('./assets/images/1.png').convert()
fundoInst = load('./assets/images/2.png').convert()
fundoJogo = load('./assets/images/fundo.png').convert()
fundoFinal = load('./assets/images/fim.png').convert()
audioIcon = load('./assets/images/audioIcon.png').convert()
fundoWin = load('./assets/images/4.png').convert()
fundoLos = load('./assets/images/5.png').convert()

telaInicial=True
telaInst=False
telaJogo=False
telaWin=False
telaLos=False

audios=['./assets/audios/audio0.mp3','./assets/audios/audio1.mp3','./assets/audios/audio2.mp3','./assets/audios/audio3.mp3','./assets/audios/audio4.mp3',
'./assets/audios/audio5.mp3','./assets/audios/audio6.mp3','./assets/audios/audio7.mp3','./assets/audios/audio8.mp3','./assets/audios/audio9.mp3',
'./assets/audios/audio10.mp3','./assets/audios/audio11.mp3','./assets/audios/audio12.mp3','./assets/audios/audio13.mp3','./assets/audios/audio14.mp3']

font = pg.font.SysFont('./assets/fonts/Changa-VariableFont_wght',50)
JFont = pg.font.SysFont('./assets/fonts/Changa-VariableFont_wght',30)
RFont = pg.font.SysFont('./assets/fonts/Changa-VariableFont_wght',22)

#Botões
textJog = JFont.render('Iniciar',True,(0,0,0))
ButtonJ = Button(width/2-40,6*height/7,80,50,(210,90,90),(210,57,57),textJog,False)

textRein = RFont.render('Reiniciar',True,(0,0,0))
ButtonR = Button(width/2-40,4*height/5+10,80,50,(210,90,90),(210,57,57),textRein,False)

textA = font.render('A',True,(0,0,0))
ButtonA = Button(width/5,6*height/7,30,30,(210,90,90),(210,57,57),textA,True)

textB = font.render('B',True,(0,0,0))
ButtonB = Button(2*width/5,6*height/7,30,30,(210,90,90),(210,57,57),textB,True)

textC = font.render('C',True,(0,0,0))
ButtonC = Button(3*width/5,6*height/7,30,30,(210,90,90),(210,57,57),textC,True)

textD = font.render('D',True,(0,0,0))
ButtonD = Button(4*width/5,6*height/7,30,30,(210,90,90),(210,57,57),textD,True)



mqtt.client.connect(mqtt.Broker,mqtt.Port,mqtt.KeepAlive)


end = False
jogando = False
mqtt.client.loop_start()
while(not end):
    pg.init()


    mouse = pg.mouse.get_pos()

    if telaInicial:
        tela.blit(fundoInicio,(0,0))
        if ButtonJ.isOver(mouse):
            ButtonJ.drawLight(tela)
        else:
            ButtonJ.drawDark(tela)

        ButtonJ.putText(tela)

        pg.display.update()

        for event in pg.event.get():
                if(event.type == pg.QUIT):
                    pg.quit() 
                if (event.type == pg.MOUSEBUTTONDOWN):  
                    if ButtonJ.isOver(mouse):
                        telaInst=True
                        telaInicial=False
                        mqtt.client.publish(mqtt.user+"/E1", payload="1", qos=0, retain=False)
                        time.sleep(0.3)
                        mqtt.client.publish(mqtt.user+"/E1", payload="0", qos=0, retain=False)
                        i=0
                        mqtt.rodada=['0','0','0']
    
    elif telaInst:
        tela.blit(fundoInst,(0,0))

        if ButtonJ.isOver(mouse):
            ButtonJ.drawLight(tela)
        else:
            ButtonJ.drawDark(tela)

        ButtonJ.putText(tela)

        pg.display.update()

        for event in pg.event.get():
                if(event.type == pg.QUIT):
                    pg.quit() 
                if (event.type == pg.MOUSEBUTTONDOWN):  
                    if ButtonJ.isOver(mouse):
                        mqtt.client.publish(mqtt.user+"/E2", payload="1", qos=0, retain=False)
                        time.sleep(0.3)
                        mqtt.client.publish(mqtt.user+"/E2", payload="0", qos=0, retain=False)
                        telaJogo=True
                        telaInst=False

    elif telaJogo:

        jogando = True

        tela.blit(fundoJogo,(0,0))

        if ButtonA.isOver(mouse):
            ButtonA.drawLight(tela)
        else:
            ButtonA.drawDark(tela)

        if ButtonB.isOver(mouse):
            ButtonB.drawLight(tela)
        else:
            ButtonB.drawDark(tela)

        if ButtonC.isOver(mouse):
            ButtonC.drawLight(tela)
        else:
            ButtonC.drawDark(tela)

        if ButtonD.isOver(mouse):
            ButtonD.drawLight(tela)
        else:
            ButtonD.drawDark(tela)

        ButtonA.putText(tela)
        ButtonB.putText(tela)
        ButtonC.putText(tela)
        ButtonD.putText(tela)
        
        pg.display.update()

        if mqtt.audio==1:
            tela.blit(audioIcon,(270,200))
            pg.display.update()
            i=random.randint(0,len(audios)-1)
            playsound(audios[i])
            audios.remove(audios[i])
            pg.draw.rect(tela,(0,0,0),[270,200,100,100])
            pg.display.update()
            mqtt.client.publish(mqtt.user+"/E7", payload="1", qos=0, retain=False)
            time.sleep(0.2)
            mqtt.client.publish(mqtt.user+"/E7", payload="0", qos=0, retain=False)
            mqtt.audio=0


        for event in pg.event.get():
            if(event.type == pg.QUIT):
                pg.quit() 
            if (event.type == pg.MOUSEBUTTONDOWN):  
                if ButtonA.isOver(mouse):
                    mqtt.client.publish(mqtt.user+"/E3", payload="1", qos=0, retain=False)
                    time.sleep(0.3)
                    mqtt.client.publish(mqtt.user+"/E3", payload="0", qos=0, retain=False)
                elif ButtonB.isOver(mouse):
                    mqtt.client.publish(mqtt.user+"/E4", payload="1", qos=0, retain=False)
                    time.sleep(0.3)
                    mqtt.client.publish(mqtt.user+"/E4", payload="0", qos=0, retain=False)
                elif ButtonC.isOver(mouse):
                    mqtt.client.publish(mqtt.user+"/E5", payload="1", qos=0, retain=False)
                    time.sleep(0.3)
                    mqtt.client.publish(mqtt.user+"/E5", payload="0", qos=0, retain=False)
                elif ButtonD.isOver(mouse):
                    mqtt.client.publish(mqtt.user+"/E6", payload="1", qos=0, retain=False)
                    time.sleep(0.3)
                    mqtt.client.publish(mqtt.user+"/E6", payload="0", qos=0, retain=False)

        if mqtt.ganhou == 1:
            telaWin = True
            telaJogo= False
            mqtt.ganhou = 0

        if mqtt.perdeu == 1:
            telaLos = True
            telaJogo = False
            mqtt.perdeu = 0

    elif telaWin:
        if jogando:
            tela.blit(fundoWin,(0,0))
            pg.display.update()

            time.sleep(3)

        tela.blit(fundoFinal,(0,0))
        
        mqtt.ganhou_aux=1
        rodada =''.join(mqtt.rodada)
        textRod = font.render(str(int(rodada,2)),True,(255,0,0))
        tela.blit(textRod,(320,60))

        if jogando:
            graf.atualizaGraf()
            vitorias=load('./assets/images/graphVitorias.png').convert()
            rod=load('./assets/images/graphRodadas.png').convert()

        tela.blit(vitorias,(80,180))
        tela.blit(rod,(350,180))

        
        if ButtonR.isOver(mouse):
            ButtonR.drawLight(tela)
        else:
            ButtonR.drawDark(tela)

        ButtonR.putText(tela)

        pg.display.update()

        for event in pg.event.get():
                if(event.type == pg.QUIT):
                    pg.quit() 
                if (event.type == pg.MOUSEBUTTONDOWN):  
                    if ButtonR.isOver(mouse):
                        mqtt.client.publish(mqtt.user+"/E1", payload="1", qos=0, retain=False)
                        time.sleep(0.3)
                        mqtt.client.publish(mqtt.user+"/E1", payload="0", qos=0, retain=False)
                        mqtt.client.publish(mqtt.user+"/E2", payload="1", qos=0, retain=False)
                        time.sleep(0.3)
                        mqtt.client.publish(mqtt.user+"/E2", payload="0", qos=0, retain=False)
                        i=0
                        mqtt.rodada=['0','0','0']
                        mqtt.ganhou_aux=0
                        telaJogo=True
                        telaWin=False
                        audios=['./assets/audios/audio0.mp3','./assets/audios/audio1.mp3','./assets/audios/audio2.mp3','./assets/audios/audio3.mp3','./assets/audios/audio4.mp3',
'./assets/audios/audio5.mp3','./assets/audios/audio6.mp3','./assets/audios/audio7.mp3','./assets/audios/audio8.mp3','./assets/audios/audio9.mp3',
'./assets/audios/audio10.mp3','./assets/audios/audio11.mp3','./assets/audios/audio12.mp3','./assets/audios/audio13.mp3','./assets/audios/audio14.mp3']

        jogando = False

    elif telaLos:
        if jogando:
            tela.blit(fundoLos,(0,0))
            pg.display.update()

            time.sleep(3)

        tela.blit(fundoFinal,(0,0))

        rodada =''.join(mqtt.rodada)
        textRod = font.render(str(int(rodada,2)),True,(255,0,0))
        tela.blit(textRod,(320,60))

        if jogando:
            graf.atualizaGraf()
            vitorias=load('./assets/images/graphVitorias.png').convert()
            rod=load('./assets/images/graphRodadas.png').convert()

        tela.blit(vitorias,(80,180))
        tela.blit(rod,(350,180))

        if ButtonR.isOver(mouse):
            ButtonR.drawLight(tela)
        else:
            ButtonR.drawDark(tela)

        ButtonR.putText(tela)

        pg.display.update()

        for event in pg.event.get():
                if(event.type == pg.QUIT):
                    pg.quit() 
                if (event.type == pg.MOUSEBUTTONDOWN):  
                    if ButtonR.isOver(mouse):
                        mqtt.client.publish(mqtt.user+"/E1", payload="1", qos=0, retain=False)
                        time.sleep(0.3)
                        mqtt.client.publish(mqtt.user+"/E1", payload="0", qos=0, retain=False)
                        mqtt.client.publish(mqtt.user+"/E2", payload="1", qos=0, retain=False)
                        time.sleep(0.3)
                        mqtt.client.publish(mqtt.user+"/E2", payload="0", qos=0, retain=False)
                        i=0
                        mqtt.rodada=['0','0','0']
                        mqtt.ganhou_aux=0
                        telaJogo=True
                        telaLos=False
                        audios=['./assets/audios/audio0.mp3','./assets/audios/audio1.mp3','./assets/audios/audio2.mp3','./assets/audios/audio3.mp3','./assets/audios/audio4.mp3',
'./assets/audios/audio5.mp3','./assets/audios/audio6.mp3','./assets/audios/audio7.mp3','./assets/audios/audio8.mp3','./assets/audios/audio9.mp3',
'./assets/audios/audio10.mp3','./assets/audios/audio11.mp3','./assets/audios/audio12.mp3','./assets/audios/audio13.mp3','./assets/audios/audio14.mp3']
        
        jogando = False
            
mqtt.client.loop_stop()

pg.quit()