import math
import pandas as pd
import random
import numpy as np
import cv2
from PIL import Image

cores = {
    19.5: (0, 0, 255),
    12.5: (255, 165, 0),
    9.5: (0, 128, 0),
    6.3: (255, 0, 0),
    4.7: (128, 0, 128)
}

class Empacotador_retangulos:

    def __init__(self) -> None:

        self.diretorio_amostra_imagens = 'Saidas/Amostras_Processadas/teste/Imagens'




    def empacotar_agregados(self, imagens, titulo_simulacao, metodo_ordenacao, i, porcentagens_preenchimento, quantidade_mapas, agregados_selecionados, tentativas_limite, dist_gran, dist_form, dist_sec, peso_area, peso_dif_gran, peso_dif_form, peso_dif_sec):

        self.imagens = imagens
        self.titulo_simulacao = titulo_simulacao
        self.metodo_ordenacao = metodo_ordenacao
        self.mapa_atual = i
        self.porcentagem_preenchimento = porcentagens_preenchimento
        self.quantidade_mapas = quantidade_mapas
        self.agregados_selecionados = agregados_selecionados
        self.tentativas_limite = tentativas_limite
        self.dist_gran = dist_gran
        self.dist_form = dist_form
        self.dist_sec = dist_sec
        self.peso_area = peso_area
        self.peso_dif_gran = peso_dif_gran
        self.peso_dif_form = peso_dif_form
        self.peso_dif_sec = peso_dif_sec  

    def verificar_sobreposicao(self, retangulos, novo_retangulo, tolerancia):
        # Ajustar as coordenadas do novo retângulo com base na tolerância
        novo_x = novo_retangulo[0] - tolerancia
        novo_y = novo_retangulo[1] - tolerancia
        novo_w = novo_retangulo[2] + tolerancia
        novo_h = novo_retangulo[3] + tolerancia
    
        for retangulo in retangulos:
            if (retangulo[0] < novo_x + novo_w and
                retangulo[0] + retangulo[2] > novo_x and
                retangulo[1] < novo_y + novo_h and
                retangulo[1] + retangulo[3] > novo_y):
                return True
        return False

    def verifica_dentro_da_tela(self, rect, largura_tela, altura_tela):
        x, y, w, h = rect
        return (x >= 0 and y >= 0 and x + w <= largura_tela and y + h <= altura_tela)

    def desenhar_contorno_azul_e_apagar(self, tela2, contorno, cor):
        # Desenhe o contorno em azul
        cv2.drawContours(tela2, [contorno], -1, cor, 2)
        cv2.imshow('Tela com Contorno Azul', tela2)
    
    def rotacionar_imagem(self, imagem, angulo):
        altura, largura = imagem.shape[:2]
        centro = (largura // 2, altura // 2)
        matriz_rotacao = cv2.getRotationMatrix2D(centro, angulo, 1.0)
        imagem_rotacionada = cv2.warpAffine(imagem, matriz_rotacao, (largura, altura))
        return imagem_rotacionada


    def gerar_mapa(self, tipo_empacotamento, tolerancia):

        #Definições de tela
        self.largura_tela = 300
        self.altura_tela = 300

        tela = 255 * np.ones((self.altura_tela, self.largura_tela, 3), dtype=np.uint8)
        tela2 = 255 * np.ones((self.altura_tela, self.largura_tela, 3), dtype=np.uint8)

        #Variaveis de interesse
        posicoes_imagens = []
        area_total = 0
        retangulos_posicionados = []
        agregados_selecionados = []
        numero_agregados_selecionados = 0
        area_agregados_selecionados = 0

        print("Agregados selecionados\n")
        print(self.agregados_selecionados)

        for agregado in self.agregados_selecionados:

            imagem_agregado = self.imagens[agregado['nome_arquivo']]

            sobreposicao = True
            tentativas = 0
            
            #Dataframe para todos os agregados selecionados
            agregados_selecionados.append({
                    'massa' : agregado['massa'],
                    'area_mm' : agregado['area_mm'],
                    'comprimento_mm' : agregado['comprimento_mm'],
                    'largura_mm' : agregado['largura_mm'],
                    'area_pixel' : agregado['area_pixel'],
                    'comprimento_pixel' : agregado['comprimento_pixel'],
                    'largura_pixel' : agregado['largura_pixel'],
                    'granulometria_nbr': agregado['granulometria_nbr'],
                    'granulometria_pdi': agregado['granulometria_pdi'],
                    'formato': agregado['formato'],
                    'secao': agregado['secao'],
                    'nome_arquivo': agregado['nome_arquivo'],
                })
            
            area_agregados_selecionados += agregado['area_pixel']
            numero_agregados_selecionados += 1

            while sobreposicao and (int(tentativas) < int(self.tentativas_limite)):

                #Geração de coordenadas e rotação do agregado
                angulo_rotacao = random.uniform(0, 360)
                imagem_agregado_rotacionada = self.rotacionar_imagem(imagem_agregado, angulo_rotacao)

                # Aplica uma rotação aleatória à imagem
                x = random.randint(2, 298 - imagem_agregado_rotacionada.shape[1])
                y = random.randint(2, 298 - imagem_agregado_rotacionada.shape[0])

                imagem_agregado_rotacionada[imagem_agregado_rotacionada[:, :, 3] == 0] = 255
                imagem_agregado_rotacionada = cv2.cvtColor(imagem_agregado_rotacionada, cv2.COLOR_BGR2GRAY)
                _, thresh = cv2.threshold(imagem_agregado_rotacionada, 254, 255, cv2.THRESH_BINARY)
                thresh = cv2.bitwise_not(thresh)
                contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                maior_contorno = max(contours, key=cv2.contourArea)
                maior_contorno[:, 0, 0] += x
                maior_contorno[:, 0, 1] += y

                x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
                novo_retangulo = (x,y,w,h)

                if not self.verificar_sobreposicao(retangulos_posicionados, novo_retangulo, tolerancia):
                    cv2.drawContours(tela, [maior_contorno], -1, cores.get(agregado['granulometria_nbr'], (0, 0, 0)), thickness=cv2.FILLED)
                    retangulos_posicionados.append(novo_retangulo)
                    sobreposicao = False

                    x, y, w, h = cv2.boundingRect(maior_contorno)

                    area_total += agregado['area_pixel']

                    cv2.rectangle(tela2, (x, y), (x + w, y + h), cores.get(agregado['granulometria_nbr'], (0, 0, 0)), 2)  # (255, 0, 0) é a cor vermelha e 2 é a espessura da borda do retângulo

                else:
                    tentativas += 1 

        porcentagem_area_total = area_total/90000

        return tela, tela2, porcentagem_area_total
