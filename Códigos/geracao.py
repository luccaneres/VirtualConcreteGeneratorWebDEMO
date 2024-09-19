import pandas as pd
import random
import numpy as np
#Titulo
global titulo_simulacao
titulo_simulacao = None

#Diretorios uteis
global diretorio_dados_simulacao
diretorio_dados_simulacao = None
global diretorio_amostra
diretorio_amostra = None
global diretorio_dados_agregados
diretorio_dados_agregados = None
global diretorio_imagens_agregados
diretorio_imagens_agregados = None

#Dados da amostra
global dados_agregados
dados_agregados = None

#Dados do SAD
#propriedades_simulacao1
global area_agregados
area_agregados = None
global qtd_mapas_bits
qtd_mapas_bits = None
#propriedades_simulacao2
global parametro_selecao
parametro_selecao = None
global parametro_ordenacao
parametro_ordenacao = None
#propriedades_avaliacao
global peso_dif_area
peso_dif_area = None
global peso_dif_gran
peso_dif_gran = None
global peso_dif_form
peso_dif_form = None
global peso_dif_sec
peso_dif_sec = None
#propriedades distribuião granulometrica
global dist_granulometrica_user
dist_granulometrica_user = None
#propriedades distribuição formato
global dist_formato_user
dist_formato_user = None
#propriedades distribuição seções
global dist_secoes_user
dist_secoes_user = None

global selecao_alternada
global ordem_posicionamento_aleatoria
global ordem_posicionamento_decrescente
global ordem_posicionamento_estatica

selecao_alternada = None
ordem_posicionamento_aleatoria = False
ordem_posicionamento_decrescente = False
ordem_posicionamento_estatica = False

global csv
global imagens
        

class Carregar_dados:
    
    def __init__(self) -> None:
        pass

    def propriedades(self, titulo, quantidade_mapas, area_agregados, tolerancia, tentativas, granulometria, empacotamento):

        self.titulo_simulacao = titulo
        self.quantidade_mapas = quantidade_mapas
        self.area_agregados = area_agregados
        self.tolerancia = tolerancia
        self.tentativas_limite = tentativas
        self.metodo_granulometria = granulometria
        self.metodo_empacotamento = empacotamento

    def parametros(self, selecao, ordenacao):
        self.parametro_selecao = selecao
        self.parametro_ordenacao = ordenacao

    def avaliacao(self, dif_area, dif_gran, dif_form, dif_sec):
        self.dif_area = dif_area
        self.dif_granulometria = dif_gran
        self.dif_formato = dif_form
        self.dif_secoes = dif_sec

    def granulometria(self, dist_granulometrica):
        self.dist_granulometrica = dist_granulometrica

    def formato(self, formato):
        self.dist_formato = formato

    def secoes(self, secoes):
        self.dist_secoes = secoes

    def dados(self, csv, imagens):
        self.csv = csv
        print("csv")
        print(csv)
        self.imagens = imagens

    def dados_agregados(self):
        #Diretorios
        global diretorio_amostra
        #Variaveis globais
        global dados_agregados
        global imagens

        dados_agregados = pd.read_csv(self.csv)
        imagens = self.imagens

        print(dados_agregados)

    def propriedades_simulacao1(self):
        #Diretorios
        global diretorio_dados_simulacao
        #Variaveis globais
        global titulo_simulacao
        global area_agregados
        global qtd_mapas_bits
        global metodo_granulometria
        global metodo_empacotamento
        global tolerancia
        global tentativas_limite

        titulo_simulacao = self.titulo_simulacao

        qtd_mapas_bits = self.quantidade_mapas
        area_agregados = self.area_agregados
        metodo_granulometria = self.metodo_granulometria
        metodo_empacotamento = self.metodo_empacotamento
        tolerancia = self.tolerancia
        tentativas_limite = self.tentativas_limite

        #print(qtd_mapas_bits, area_agregados)

    def propriedades_simulacao2(self):
        #Diretorios
        global diretorio_dados_simulacao
        #Variaveis globais
        global parametro_selecao
        global parametro_ordenacao

        parametro_selecao = self.parametro_selecao
        parametro_ordenacao = self.parametro_ordenacao

        #print(parametro_selecao, parametro_ordenacao)

    def propriedades_avaliacao(self):
        #Diretorios
        global diretorio_dados_simulacao
        #Variaveis globais
        global peso_dif_area
        global peso_dif_gran
        global peso_dif_form
        global peso_dif_sec

        peso_dif_area = self.dif_area
        peso_dif_gran = self.dif_granulometria
        peso_dif_form = self.dif_formato
        peso_dif_sec = self.dif_secoes

        #print(peso_dif_area, peso_dif_sec, peso_dif_form, peso_dif_gran)

    def propriedades_dist_granulometrica(self):
        #Diretorios
        global diretorio_dados_simulacao
        #Variaveis globais
        global dist_granulometrica_user

        print(self.dist_granulometrica)

        dist_granulometrica_user = pd.DataFrame(list(self.dist_granulometrica.items()), columns=['granulometria', 'porcentagem_granulometria'])

        print(dist_granulometrica_user)

    def propriedades_dist_formato(self):
        #Diretorios
        global diretorio_dados_simulacao
        #Variaveis globais
        global dist_formato_user

        dist_formato_user = pd.DataFrame(list(self.dist_formato.items()), columns=['formato', 'porcentagem_formato'])

        print(dist_formato_user)

    def propriedades_dist_secoes(self):
        #Diretorios
        global diretorio_dados_simulacao
        #Variaveis globais
        global dist_secoes_user

        dist_secoes_user = pd.DataFrame(list(self.dist_secoes.items()), columns=['secao', 'porcentagem_secao'])

        print(dist_secoes_user)


class Definicao_probabilidades:

    def __init__(self) -> None:
        self.mapeamento_dist_granulometrica = None
        self.mapeamento_dist_formato = None
        self.mapeamento_dist_secoes = None
        self.probabilidade_total = None
        self.dados_completos_agregados = None


    def mapear(self):
        global dist_granulometrica_user
        global dist_formato_user
        global dist_secoes_user

        print(dist_granulometrica_user)

        # Convertendo para string para garantir a consistência
        self.mapeamento_dist_granulometrica = {str(k): str(v) for k, v in zip(dist_granulometrica_user['granulometria'], dist_granulometrica_user['porcentagem_granulometria'])}
        self.mapeamento_dist_formato = dict(zip(dist_formato_user['formato'], dist_formato_user['porcentagem_formato']))
        self.mapeamento_dist_secoes = dict(zip(dist_secoes_user['secao'], dist_secoes_user['porcentagem_secao']))


    #Método com o objetivo de calcular a probabilidade simples de cada agregado
    def calcular_probabilidade(self, agregado):
        # Convertendo os valores de granulometria para string para garantir a consistência
        granulometria_nbr_str = str(agregado['granulometria_nbr'])
        granulometria_pdi_str = str(agregado['granulometria_pdi'])

        if metodo_granulometria == 'NBR NM 248':
            probabilidade_nivel_peneira = self.mapeamento_dist_granulometrica.get(granulometria_nbr_str, 0)
            print(probabilidade_nivel_peneira)
        else:
            probabilidade_nivel_peneira = self.mapeamento_dist_granulometrica.get(granulometria_pdi_str, 0)
            print(probabilidade_nivel_peneira)

        probabilidade_formato = self.mapeamento_dist_formato.get(agregado['formato'], 0)
        probabilidade_secao = self.mapeamento_dist_secoes.get(agregado['secao'], 0)

        # Convertendo os valores para float antes da multiplicação
        probabilidade_nivel_peneira = float(probabilidade_nivel_peneira)
        probabilidade_formato = float(probabilidade_formato)
        probabilidade_secao = float(probabilidade_secao)

        print(f"Granulometria: {probabilidade_nivel_peneira}, Formato: {probabilidade_formato}, Seção: {probabilidade_secao}")

        if probabilidade_formato != 0 and probabilidade_nivel_peneira != 0 and probabilidade_secao != 0:
            resultado = probabilidade_formato * probabilidade_nivel_peneira * probabilidade_secao
        else:
            resultado = 0  # Ou outro valor padrão apropriado

        return resultado
    
    #Método com o objetivo de calcular a probabilidade de escolha do agregado em face da probabilidade de escolha dos demais
    #Também com o objetivo de armazenar estas informações no dataframe correspondente
    def definir_probabilidade(self):
        print("definindo probabilidade")
        global diretorio_dados_simulacao
        global diretorio_dados_agregados
        global dados_agregados

        dados_agregados['probabilidade'] = dados_agregados.apply(self.calcular_probabilidade, axis=1)
        self.probabilidade_total = dados_agregados['probabilidade'].sum()
        dados_agregados['probabilidade_ofc'] = dados_agregados['probabilidade'] / self.probabilidade_total

        soma_probabilidades_oficiais = dados_agregados['probabilidade_ofc'].sum()


class Roleta:

    def __init__(self) -> None:
        print("roletinha")
        pass

    def selecionar_agregados(self):

        print("selecionando agregados")
        global area_agregados
        global dados_agregados
        global agregados_selecionados

        print(dados_agregados)
        print(area_agregados)

        agregados_selecionados = []
        area_ocupada = 0.0
        roleta = []
        

        # Crie uma cópia do dataframe para evitar modificações indesejadas
        dados_agregados_copia = dados_agregados.copy()

        for index, row in dados_agregados_copia.iterrows():
            agregado_info = {col: row[col] for col in dados_agregados_copia.columns}
            roleta.append(agregado_info)

        cumulative_probs = [sum(agregado_info['probabilidade_ofc'] for agregado_info in roleta[:i+1]) for i in range(len(roleta))]


        while area_ocupada < (float(float(area_agregados)/100) * (300*300)):

            random_value = random.uniform(0, 1)

            for i, agregado_info in enumerate(roleta):

                if random_value <= cumulative_probs[i]:
                    # Adicione o dicionário completo do agregado à lista de agregados selecionados
                    agregados_selecionados.append(agregado_info)
                    area_ocupada += agregado_info['area_pixel']

                    print(area_ocupada)
                    print(agregados_selecionados)
                    break


class Parametros:

    def __init__(self) -> None:
        print("definindo parametros")

    def definir_parametros(self):

        global parametro_selecao
        global parametro_ordenacao

        print(parametro_ordenacao)

        global selecao_alternada
        global ordem_posicionamento_decrescente
        global ordem_posicionamento_aleatoria
        global ordem_posicionamento_estatica

        if parametro_selecao == 'contínua':
            selecao_alternada = True
        else:
            selecao_alternada = False

        if parametro_ordenacao == 'decrescente':
            ordem_posicionamento_decrescente = True
        elif parametro_ordenacao == 'aleatoria':
            ordem_posicionamento_aleatoria = True
        else:
            ordem_posicionamento_estatica = True


#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Codigos')))
from esferas import Empacotador_esferas
from retangulos import Empacotador_retangulos
from contornos_quadrantes import Empacotador_contornos_quadrantes

class Gerador_concreto:

    def __init__(self) -> None:
        print("gerando concreto")
        self.roleta = Roleta()

    def alternar_selecao(self, num):
        global selecao_alternada
        if (not selecao_alternada) and num == 1:
            self.roleta.selecionar_agregados()
        if selecao_alternada:
            self.roleta.selecionar_agregados()

    def ordenar_selecionados(self):
        global agregados_selecionados

        global ordem_posicionamento_decrescente
        global ordem_posicionamento_aleatoria
        global ordem_posicionamento_estatica

        if ordem_posicionamento_decrescente:
            agregados_selecionados.sort(key=lambda x: x['area_pixel'], reverse=True)
        elif ordem_posicionamento_aleatoria:
            random.shuffle(agregados_selecionados)
        elif ordem_posicionamento_estatica:
            pass

    def gerar_mapa(self):

        saidas = []

        empacotador_esferas = Empacotador_esferas()
        empacotador_retangulos = Empacotador_retangulos()
        empacotador_contornos_quadrantes = Empacotador_contornos_quadrantes()

        for i in range(1, int(qtd_mapas_bits)+1):

            self.alternar_selecao(i)
            self.ordenar_selecionados()

            if metodo_empacotamento == 'esferas':
                empacotador_esferas.empacotar_agregados(imagens, titulo_simulacao, parametro_ordenacao,i, area_agregados, qtd_mapas_bits, agregados_selecionados, tentativas_limite, dist_granulometrica_user, dist_formato_user, dist_secoes_user, peso_dif_area, peso_dif_gran, peso_dif_form, peso_dif_sec)
                retorno1, retorno2, porcentagem_area = empacotador_esferas.gerar_mapa(metodo_empacotamento, tolerancia)

                saida = {
                    'indice': i,
                    'imagem': retorno1,  # Aqui você deve ajustar conforme o retorno desejado
                    'imagem2': retorno2,
                    'porcentagem_area': porcentagem_area
                }

            if metodo_empacotamento == 'retângulos':
                empacotador_retangulos.empacotar_agregados(imagens, titulo_simulacao, parametro_ordenacao,i, area_agregados, qtd_mapas_bits, agregados_selecionados, tentativas_limite, dist_granulometrica_user, dist_formato_user, dist_secoes_user, peso_dif_area, peso_dif_gran, peso_dif_form, peso_dif_sec)
                retorno1, retorno2, porcentagem_area = empacotador_retangulos.gerar_mapa(metodo_empacotamento, tolerancia)

                saida = {
                    'indice': i,
                    'imagem': retorno1,  # Aqui você deve ajustar conforme o retorno desejado
                    'imagem2': retorno2,
                    'porcentagem_area': porcentagem_area
                }

            if metodo_empacotamento == 'contornos quadrantes':
                empacotador_contornos_quadrantes.empacotar_agregados(imagens, titulo_simulacao, parametro_ordenacao,i, area_agregados, qtd_mapas_bits, agregados_selecionados, tentativas_limite, dist_granulometrica_user, dist_formato_user, dist_secoes_user, peso_dif_area, peso_dif_gran, peso_dif_form, peso_dif_sec)
                retorno1, retorno2, porcentagem_area = empacotador_contornos_quadrantes.gerar_mapa(metodo_empacotamento, tolerancia)

                saida = {
                    'indice': i,
                    'imagem': retorno1,  # Aqui você deve ajustar conforme o retorno desejado
                    'imagem2': retorno2,
                    'porcentagem_area': porcentagem_area
                }



            saidas.append(saida)
        
        return saidas