import pygame as pg
import math
import protMqtt as mqtt
import sys
import time
from pygame import display, event, font 
from pygame.image import load

class Button:
    def __init__(self, xpos, ypos, radius, color_light, color_dark,text):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.color_light = color_light
        self.color_dark = color_dark
        self.text = text

    def putText(self,tela):
        tela.blit(self.text,(self.xpos-12,self.ypos-15))

    def isOver(self,mouse):
        if math.sqrt((self.xpos-mouse[0])**2+(self.ypos-mouse[1])**2)<self.radius:
            return True
        else:
            return False
    def drawLight(self,tela):
        pg.draw.circle(tela,self.color_light,(self.xpos,self.ypos),self.radius)
    def drawDark(self,tela):
        pg.draw.circle(tela,self.color_dark,(self.xpos,self.ypos),self.radius)

pg.init()

#Cria tela
width = 300
height =500
tela = display.set_mode(size=(width, height))
display.set_caption("Turing Inverso")

#Imagem de fundo
fundoJogo = load('imagens/fundo.png')

telaInicial=True
telaInst=False
telaJogo=False
telaRes=False

font = pg.font.SysFont('Changa-VariableFont_wght',20)

#Botões
textJog = font.render('Jogar',True,(0,0,0))
ButtonJ = Button(width/2,4*height/5,30,(210,90,90),(210,57,57),textJog)

textA = font.render('A',True,(0,0,0))
ButtonA = Button(width/4,2*height/5,30,(210,90,90),(210,57,57),textA)

textB = font.render('B',True,(0,0,0))
ButtonB = Button(3*width/4,2*height/5,30,(210,90,90),(210,57,57),textB)

textC = font.render('C',True,(0,0,0))
ButtonC = Button(width/4,3*height/5,30,(210,90,90),(210,57,57),textC)

textD = font.render('D',True,(0,0,0))
ButtonD = Button(3*width/4,3*height/5,30,(210,90,90),(210,57,57),textD)


mqtt.client.connect(mqtt.Broker,mqtt.Port,mqtt.KeepAlive)

end = False
while(not end):
    pg.init()

    mouse = pg.mouse.get_pos()

    if telaInicial:
        tela.fill((0,0,0))

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
                   telaJogo=True
                   telaInicial=False

    if telaJogo:

        tela.blit(fundoJogo,(0,0))
        pg.display.update()

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

        mqtt.client.loop_start()

        for event in pg.event.get():
            if(event.type == pg.QUIT):
                pg.quit() 
            if (event.type == pg.MOUSEBUTTONDOWN):  
                if ButtonA.isOver(mouse):
                    mqtt.client.publish(mqtt.user+"/S0", payload="1", qos=0, retain=False)
                    time.sleep(0.6)
                    mqtt.client.publish(mqtt.user+"/S0", payload="0", qos=0, retain=False)
                elif ButtonB.isOver(mouse):
                    mqtt.client.publish(mqtt.user+"/S0", payload="1", qos=0, retain=False)
                    time.sleep(0.6)
                    mqtt.client.publish(mqtt.user+"/S0", payload="0", qos=0, retain=False)
                elif ButtonC.isOver(mouse):
                    mqtt.client.publish(mqtt.user+"/S0", payload="1", qos=0, retain=False)
                    time.sleep(0.6)
                    mqtt.client.publish(mqtt.user+"/S0", payload="0", qos=0, retain=False)
                elif ButtonD.isOver(mouse):
                    mqtt.client.publish(mqtt.user+"/S0", payload="1", qos=0, retain=False)
                    time.sleep(0.6)
                    mqtt.client.publish(mqtt.user+"/S0", payload="0", qos=0, retain=False)

        if mqtt.pronto == 1:
            end=True
            
        mqtt.client.loop_stop()

pg.quit()