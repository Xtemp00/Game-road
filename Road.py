from pygame import*
from random import*
import sys
init()

def Game():
    global surf
    surf = display.set_mode((0,0),FULLSCREEN)
    metre=0
    run = True
    Roadfont= font.Font("Ailerons-Regular.otf",30)


    Position=0
    Positiony=0
    barrer=image.load("barriere.png").convert_alpha()
    barrer2=image.load("barriere.png").convert_alpha()
    player=image.load("boule.png").convert_alpha()
    #utiliser transform.scale pour changer la taille de la balle
    player = transform.scale(player,(40,40))
    position_player=player.get_rect()
    position_barrer= barrer.get_rect()
    position_barrer2= barrer2.get_rect()
    position_barrer.right=display.Info().current_w/6-2
    position_barrer2.left=5*display.Info().current_w/6+5
    position_player.x=500
    position_player.y=750


    def Road(Vitesse):
        global surf
        draw.line(surf,(255,255,255),(display.Info().current_w/6,0),(display.Info().current_w/6,display.Info().current_h),20)
        draw.line(surf,(255,255,255),(5*display.Info().current_w/6,0),(5*display.Info().current_w/6,display.Info().current_h),20)
        draw.line(surf,(255,255,255),(display.Info().current_w/2,0+Vitesse),(display.Info().current_w/2,200+Vitesse),20)
        draw.line(surf,(255,255,255),(display.Info().current_w/2,300+Vitesse),(display.Info().current_w/2,500+Vitesse),20)
        draw.line(surf,(255,255,255),(display.Info().current_w/2,600+Vitesse),(display.Info().current_w/2,800+Vitesse),20)
        draw.line(surf,(255,255,255),(display.Info().current_w/2,-300+Vitesse),(display.Info().current_w/2,-100+Vitesse),20)
        draw.line(surf,(255,255,255),(display.Info().current_w/2,-600+Vitesse),(display.Info().current_w/2,-400+Vitesse),20)
        draw.line(surf,(255,255,255),(display.Info().current_w/2,900+Vitesse),(display.Info().current_w/2,1100+Vitesse),20)
        draw.rect(surf,(35,166,33),(0,0,display.Info().current_w/6-2,display.Info().current_h))
        draw.rect(surf,(35,166,33),(5+5*display.Info().current_w/6,0,display.Info().current_w,display.Info().current_h))

    List=[]

    global Vitesse
    Vitesse=1
    while run:
        global Positiony
        global Position
        global Vitesse
        global metre

        Information=Roadfont.render("{} mètres".format(int(metre)),1,(255,255,255))
        for events in event.get():
            if events.type==KEYDOWN and events.key==K_ESCAPE:
                run = False
            if events.type == QUIT:
                run = False
            if events.type==KEYDOWN:
                List.append(events.key)
            if events.type==KEYUP and events.key in List:
                List.remove(events.key)

        #recherche de la touche utiliser plus deplacement
        if K_LEFT in List:
            if position_player.left>0 and position_player.left<display.Info().current_w:
                position_player.x-=3
        if K_RIGHT in List:
            if position_player.right<display.Info().current_w and position_player.right>0:
                    position_player.x +=3
        if K_UP in List:
            if position_player.top>0 and position_player.top<display.Info().current_h:
                position_player.y-=3
        if K_DOWN in List:
            if position_player.bottom>0 and position_player.bottom<display.Info().current_h:
                position_player.y+=3
        #recherche d'un depassement de map
        if position_player.top>display.Info().current_h:
            position_player.y+=30
        if position_player.bottom<0:
            position_player.y-=30
        if position_player.left<0:
            position_player.x+=30
        if position_player.right>display.Info().current_w:
            position_player.x-=30
        if Vitesse>600:
            Vitesse=0
        Vitesse+=1
        position_barrer.y+=1
        position_barrer2.y+=1
        def rand():
            return randint(0,1000)
        if position_barrer.y>=display.Info().current_h:
            position_barrer.y=-100-rand()
        if Rect.colliderect(position_barrer, position_player): #utiliser colliderect
            position_barrer.y=display.Info().current_h+500
        if position_barrer2.y>=display.Info().current_h:
            position_barrer2.y=-100-rand()
        if Rect.colliderect(position_barrer2, position_player): #utiliser colliderect
            position_barrer2.y=display.Info().current_h+500
        Road(Vitesse)
        surf.blit(Information,Rect(display.Info().current_w/5,display.Info().current_h/15,200,100))
        metre+=0.05
        surf.blit(barrer,position_barrer)
        surf.blit(barrer2,position_barrer2)
        surf.blit(player,position_player)
        display.flip()
        surf.fill(0)





quit()