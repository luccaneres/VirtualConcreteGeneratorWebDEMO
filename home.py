import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#############################
###Declaração de Variáveis###
#############################

# Variáveis globais
titulo = ""
quantidade_simulacoes = ""
porcentagem_area = ""
pixels_tolerancia = ""
tentativas_limite = ""
granulometria = ""
empacotamento = ""

selecao = ""
ordenacao = ""

dif_area = ""
dif_granulometria = ""
dif_formato = ""
dif_secoes = ""

dist_granulometrica = {}
dist_formato = {}
dist_secoes = {}

global imagens_dict
global csv
csv = None
imagens = None
imagens_dict = {}

################
###Código SAD###
################

st.title("VCGen - Virtual Concrete Generator")
st.header("Geração Computacional de Concretos")

st.markdown("""
    Aplicação desenvolvida para um trabalho de conclusão de curso 
    vinculado à Universidade Estadual do Oeste do Paraná (UNIOESTE)
            
    **Prof. Dr. Rogério Luis Rizzi** - rogerio.rizzi@unioeste.br \n
    **Lucca Abbado Neres** - lucca.neres1@unioeste.br
    """)

st.markdown("-------------------------------------")

# Form 1
with st.form("Form 1"):
    st.text("Propriedades da simulação")
    #titulo = st.text_input("Título", value='teste')
    quantidade_simulacoes = st.text_input("Quantidade de simulações")

    porcentagem_area = st.text_input("Porcentagem ideal de área ocupada por agregados")

    #pixels_tolerancia = st.text_input("Pixels de tolerância para o empacotamento", value='3')

    tentativas_limite = st.text_input("Número de tentativas limite")

    
    st.markdown("-------------------------------------")
    
    granulometria = st.radio("Granulometria a ser considerada?", options=("PDI", "NBR NM 248"))
    empacotamento = st.radio("Método de empacotamento?", options=("esferas", "retângulos", "contornos quadrantes"))
    
    st.markdown("-------------------------------------")
    
    submitted1 = st.form_submit_button("Enviar")

st.markdown("-------------------------------------")

titulo = 'teste'
pixels_tolerancia = 3

# Form 2
with st.form("Form 2"):
    st.text("Método de seleção")
    selecao = st.radio("Método de seleção", options=("única", "contínua"))
    #ordenacao = st.radio("Método de ordenação", options=("estatica", "aleatoria", "decrescente"))
    
    st.markdown("-------------------------------------")
    
    submitted2 = st.form_submit_button("Enviar")

st.markdown("-------------------------------------")

ordenacao = 'decrescente'


dif_granulometria = 25
dif_formato = 25
dif_area = 25
dif_secoes = 25


# Form 4
form4=st.form("Form 4")

granulometrias = ["19.5", "12.5", "9.5", "6.3", "4.7"]
dicionario = {}

form4.text("Distribuição granulométrica idealizada")

for granulometria in granulometrias:
    valor = form4.text_input(granulometria)
    dist_granulometrica[granulometria] = float(valor) if valor else 0.0

form4.form_submit_button("Enviar")

st.markdown("-------------------------------------")


# Form 5
with st.form("Form 5"):
    formatos = ["cubica", "alongada"]
    dist_formato = {formato: st.text_input(formato) for formato in formatos}

    submitted5 = st.form_submit_button("Enviar")

st.markdown("-------------------------------------")


secoes = ["redimensionado_30", "redimensionado_70", "original"]
valores = [5, 5, 100]
dist_secoes = dict(zip(secoes, valores))

# Form 7
with st.form("Form 7"):
    
    st.text("Insira as imagens dos agregados e arquivo csv respectivo")
    csv = st.file_uploader("Selecione o arquivo csv", accept_multiple_files=False, type=["csv"])
    imagens = st.file_uploader("Selecione os arquivos de imagem", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

    if imagens is not None:
        for imagem in imagens:
            imagem_name = imagem.name
            imagem_tratada = Image.open(imagem)
            imagem_array = np.array(imagem_tratada)
            #imagem_final = cv2.cvtColor(imagem_array, cv2.COLOR_RGBA2BGR)
            imagem_final = imagem_array
            imagens_dict[imagem_name] = imagem_final

    submitted7 = st.form_submit_button("Enviar")

st.markdown("-------------------------------------")

import geracao as gerador_simulacoes

def parse_input(value, dtype):
    try:
        if dtype == int:
            return int(value)
        elif dtype == float:
            return float(value)
        elif dtype == str:
            return str(value)
        # Adicione mais tipos conforme necessário
    except (ValueError, TypeError):
        return None

def convert_values():
    global quantidade_simulacoes, porcentagem_area, pixels_tolerancia, tentativas_limite
    global dif_area, dif_granulometria, dif_formato, dif_secoes
    global dist_granulometrica, dist_formato, dist_secoes

    quantidade_simulacoes = parse_input(quantidade_simulacoes, int)
    porcentagem_area = parse_input(porcentagem_area, float)
    pixels_tolerancia = parse_input(pixels_tolerancia, int)
    tentativas_limite = parse_input(tentativas_limite, int)
    dif_area = parse_input(dif_area, float)
    dif_granulometria = parse_input(dif_granulometria, float)
    dif_formato = parse_input(dif_formato, float)
    dif_secoes = parse_input(dif_secoes, float)

    dist_granulometrica = {key: parse_input(value, float) for key, value in dist_granulometrica.items()}
    dist_formato = {key: parse_input(value, float) for key, value in dist_formato.items()}
    dist_secoes = {key: parse_input(value, float) for key, value in dist_secoes.items()}

def geracao_simulacoes(csv, imagens_dict):

    global simulacoes

    convert_values()

    func_SDA1 = gerador_simulacoes.Carregar_dados()
    func_SDA2 = gerador_simulacoes.Definicao_probabilidades()
    func_SDA3 = gerador_simulacoes.Roleta()
    func_SDA4 = gerador_simulacoes.Parametros()
    func_SDA5 = gerador_simulacoes.Gerador_concreto()

    func_SDA1.propriedades(titulo, quantidade_simulacoes, porcentagem_area, pixels_tolerancia, tentativas_limite, granulometria, empacotamento)
    func_SDA1.parametros(selecao, ordenacao)
    func_SDA1.avaliacao(dif_area, dif_granulometria, dif_formato, dif_secoes)
    func_SDA1.granulometria(dist_granulometrica)
    func_SDA1.formato(dist_formato)
    func_SDA1.secoes(dist_secoes)
    func_SDA1.dados(csv, imagens_dict)

    func_SDA1.dados_agregados()
    func_SDA1.propriedades_simulacao1()
    func_SDA1.propriedades_simulacao2()
    func_SDA1.propriedades_avaliacao()
    func_SDA1.propriedades_dist_granulometrica()
    func_SDA1.propriedades_dist_formato()
    func_SDA1.propriedades_dist_secoes()

    func_SDA2.mapear()
    func_SDA2.definir_probabilidade()

    #func_SDA3.selecionar_agregados()

    func_SDA4.definir_parametros()

    simulacoes_geradas = func_SDA5.gerar_mapa()

    return simulacoes_geradas

cores = {
    19.5: (0, 0, 255),
    12.5: (255, 165, 0),
    9.5: (0, 128, 0),
    6.3: (255, 0, 0),
    4.7: (128, 0, 128)
}


with st.form("Form 9"):
    st.text("Gerar simulações")
    submitted9 = st.form_submit_button("Gerar")
    
    if submitted9:
        # Gerar imagem com as posições aleatórias
        simulacoes = geracao_simulacoes(csv, imagens_dict)

        # Adicionando a legenda
        st.markdown("### Lista de Simulações")
        st.markdown("Legenda de cores por granulometria")
        legendas = []
        
        for granulometria, cor in cores.items():
            legendas.append(f"<div style='display: inline-block; width: 20px; height: 20px; background-color: rgb{cor}; border: 1px solid black; margin-right: 5px;'></div>{granulometria} mm")

        # Exibir a legenda com cores
        st.markdown("".join(legendas), unsafe_allow_html=True)

        colunas = st.columns(2)
        
        for imagem_dict in simulacoes:
            indice = imagem_dict['indice']
            imagem = imagem_dict['imagem']
            imagem2 = imagem_dict['imagem2']
            porcentagem_area = imagem_dict['porcentagem_area']
            
            # Converter a imagem numpy para PIL para exibir no Streamlit
            imagem_pil = Image.fromarray(imagem)
            imagem2_pil = Image.fromarray(imagem2)
            
            # Exibir a imagem final no Streamlit
            with colunas[0]:
                st.image(imagem_pil, caption=f'Simulação {indice} - Porcentagem empacotamento = {porcentagem_area:.2f}')
            with colunas[1]:
                st.image(imagem2_pil, caption=f'Empacotamento Simulação {indice}')

st.markdown("-------------------------------------")


