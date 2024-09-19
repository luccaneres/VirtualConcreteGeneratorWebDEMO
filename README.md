# VCGen - Virtual Concrete Generator

## DEMO para visualização de conceitos básicos

Este é um aplicativo web desenvolvido utilizando **Streamlit**, com o objetivo de simular modelos computacionais de concretos. A aplicação foi criada como parte de uma pesquisa de iniciação tecnológica vinculada à **Universidade Estadual do Oeste do Paraná (UNIOESTE)**. Por se tratar de um DEMO, a aplicação não contempla todas as funcionalidades desenvolvidas no estudo. Para mais informações contate um dos desenvolvedores.

### Desenvolvedores

- **Prof. Dr. Rogério Luis Rizzi** - [rogerio.rizzi@unioeste.br](mailto:rogerio.rizzi@unioeste.br)
- **Lucca Abbado Neres** - [lucca.neres1@unioeste.br](mailto:lucca.neres1@unioeste.br)

---

## Índice

1. [Visão Geral](#visão-geral)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Acesso](#execução)
   - [Requisitos](#requisitos)
   - [Url](#acesso)
4. [Como Utilizar](#como-utilizar)
   - [Propriedades da Simulação](#propriedades-da-simulação)
   - [Distribuição Granulométrica](#distribuição-granulométrica)
   - [Upload de Arquivos](#upload-de-arquivos)
   - [Geração de Simulações](#geração-de-simulações)
5. [Funcionalidades](#funcionalidades)
6. [Contribuição](#contribuição)
7. [Licença](#licença)

---

## Visão Geral

O **VCGen - Virtual Concrete Generator** é uma aplicação que permite a simulação de concretos virtuais com diferentes propriedades granulométricas, de formato e três metodologias de empacotamento. Ele possibilita a realização de diversas simulações com base em parâmetros ajustáveis pelo usuário, como porcentagem ideal de área ocupada por agregados e número de tentativas.

---

## Tecnologias Utilizadas

- **Streamlit**: Framework principal para a construção da interface web interativa.
- **Python**: Linguagem de programação utilizada para cálculos e geração de dados.
- **Pandas**: Para manipulação de dados de entrada e resultados.
- **Numpy**: Para cálculos matemáticos e geração de distribuições granulométricas.
- **OpenCV** e **Pillow**: Para manipulação e tratamento de imagens.

---

## Execução

### Requisitos

- Um Navegador com acesso à internet.

### Acesso

- Para acessar basta visitar o link [https://virtual-concrete-generator-eaicti-2024.streamlit.app/](https://virtual-concrete-generator-eaicti-2024.streamlit.app/).

## Como Utilizar

É **NECESSÁRIO** clicar em **ENVIAR** após o preenchimento de cada conjunto de campos!!!

### Propriedades da Simulação

Nesta seção, você pode ajustar os principais parâmetros da simulação:

- **Quantidade de Simulações**: Define quantas simulações serão executadas (quanto mais simulações mais tempo de execução).
- **Porcentagem Ideal de Área Ocupada por Agregados**: Percentual de área desejado de ocupação dos agregados (quanto mais porcentagem de área mais tempo de execução).
- **Número de Tentativas Limite**: Número máximo de tentativas de empacotamento com sobreposição antes de descartar o agregado (quanto mais tentativas mais tempo de execução).
- **Granulometria**: Escolha entre a classificação para o agregado determinada por algum dos padrões **PDI** ou **NBR NM 248**.
- **Método de Empacotamento**: Selecione entre **esferas**, **retângulos** ou **contornos quadrantes**.

### Método de seleção

Nesta seção, você pode escolher entre gerar uma seleção de agregados para todas as simulações (única) e uma seleção para cada simulação (contínua).

### Distribuição Granulométrica

Aqui o usuário pode definir manualmente a distribuição granulométrica dos agregados nas frações (em porcentagem de massa):

Uma aproximação para os valores encontrados no estudo é:

- 19.5 mm - 0
- 12.5 mm - 46
- 9.5 mm - 44
- 6.3 mm - 9
- 4.7 mm - 1

### Distribuição de Formato

Aqui o usuário pode definir manualmente a distribuição de formato dos agregados nas frações (em porcentagem de massa):

Uma aproximação para os valores encontrados no estudo é:

- Cubica - 99
- Alongada - 1

### Upload de Arquivos

O usuário pode fazer upload de arquivos CSV contendo dados relacionados aos agregados e suas respectivas imagens:

- **CSV**: Carregar arquivo contendo os dados dos agregados.
- **Imagens**: Upload de imagens no formato **PNG**, **JPG**, **JPEG** para visualização e processamento.

### Geração de Simulações

Após ajustar os parâmetros e realizar o upload dos arquivos necessários, clique em **Gerar Simulações** para iniciar o processo e visualizar os resultados. Uma vez que inseridos os arquivos na etapa **Upload de Arquivos**, os demais parâmetros podem ser alterados livremente, restando apenas o custo computacional de gerar as simulações com estes parâmetros.

