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
3. [Instalação](#instalação)
4. [Como Utilizar](#como-utilizar)
   - [Parâmetros de Simulação](#parâmetros-de-simulação)
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

```bash
pip install streamlit pandas numpy
