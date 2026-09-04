import pyxel
import math
largura_mapa=1000

class Jogador:
    IMG = 0
    U = 0
    V = 0
    WIDTH = 8
    HEIGHT = 16
    DX = 2
    gravidade=1
    velocidade_maxima_queda=4
    def __init__(self):
        self.x = 80
        self.y = 40
        self.dx=0
        self.dy=0
        self.no_chão=False
        self.direcao=1
    def moverpraesquerda(self):
        self.dx = -self.DX
        self.direcao=-1
    def moverpradireita(self):
        self.dx = self.DX
        self.direcao=1
class Coisas:
    terra=(1,4)
    vazio=(0,4)
    grama=(0,5)
    solidos=[terra,grama]
class Jogo:
    def __init__(self):
        pyxel.init(244,144, title= "Super Mais Ou Menos World")
        pyxel.load("character.pyxres")
        self.camera_x=0 
        self.Jogador = Jogador()
        pyxel.run(self.update,self.draw)
    def resetar(self):
        self.Jogador=Jogador()
        self.camera_x=0
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            self.resetar()
            return
        self.Jogador.dx=0
        if pyxel.btn(pyxel.KEY_LEFT):
            self.Jogador.moverpraesquerda()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.Jogador.moverpradireita()
        self.Jogador.dy += Jogador.gravidade
        if self.Jogador.dy>self.Jogador.velocidade_maxima_queda:
                self.Jogador.dy=self.Jogador.velocidade_maxima_queda
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.Jogador.no_chão:
                self.Jogador.dy = -6
        dy_original=self.Jogador.dy
        dx_corrigido, dy_corrigido=pyxel.tilemaps[0].collide(
            self.Jogador.x,
            self.Jogador.y,
            self.Jogador.WIDTH,
            self.Jogador.HEIGHT,
            self.Jogador.dx,
            self.Jogador.dy,
            Coisas.solidos
        )
        self.Jogador.no_chão=(dy_original>0 and dy_corrigido != dy_original)
        if dy_corrigido != dy_original:
            self.Jogador.dy=0
        self.Jogador.x += dx_corrigido
        self.Jogador.y += dy_corrigido

        if self.Jogador.x<0:
            self.Jogador.x=0
        if self.Jogador.x > largura_mapa - self.Jogador.WIDTH:
            self.Jogador.x = (largura_mapa - self.Jogador.WIDTH)
        self.camera_x= (self.Jogador.x - pyxel.width // 2)
        if self.camera_x<0:
            self.camera_x=0
        limite_camera= (largura_mapa-pyxel.width)
        if self.camera_x > limite_camera:
            self.camera_x = limite_camera
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(6)
        pyxel.bltm(0,0,0,self.camera_x, 0 , pyxel.width ,pyxel.height)
        jogador_tela_x=(self.Jogador.x-self.camera_x)
        pyxel.blt(
            jogador_tela_x,
            self.Jogador.y,
            self.Jogador.IMG,
            self.Jogador.U,
            self.Jogador.V,
            self.Jogador.WIDTH*self.Jogador.direcao,
            self.Jogador.HEIGHT,
            0
        )
Jogo()
noah