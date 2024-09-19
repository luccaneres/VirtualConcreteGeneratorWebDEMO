# VCGen - Virtual Concrete Generator

## Geração Computacional de Concretos

Este é um aplicativo web desenvolvido utilizando **Streamlit**, com o objetivo de simular e analisar propriedades de concretos gerados computacionalmente. A aplicação foi criada como parte de um trabalho de conclusão de curso vinculado à **Universidade Estadual do Oeste do Paraná (UNIOESTE)**.

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

O **VCGen - Virtual Concrete Generator** é uma aplicação que permite a simulação de concretos virtuais com diferentes propriedades granulométricas, metodologias de empacotamento e seleção de agregados. Ele possibilita a realização de diversas simulações com base em parâmetros ajustáveis pelo usuário, como porcentagem ideal de área ocupada por agregados e número de tentativas.

---

## Tecnologias Utilizadas

- **Streamlit**: Framework principal para a construção da interface web interativa.
- **Python**: Linguagem de programação utilizada para cálculos e geração de dados.
- **Pandas**: Para manipulação de dados de entrada e resultados.
- **Numpy**: Para cálculos matemáticos e geração de distribuições granulométricas.

---

## Instalação

### Requisitos

- Python 3.8 ou superior
- Instalar os pacotes necessários via `pip`:

```bash
pip install streamlit pandas numpy
