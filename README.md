# Análise de Entidades em Letras de Engenheiros do Hawaii com spaCy

Este projeto utiliza Processamento de Linguagem Natural (PLN) para treinar um modelo customizado de Reconhecimento de Entidades Nomeadas (NER) com a biblioteca spaCy. O objetivo é extrair e classificar entidades como Pessoas (`PER`), Lugares (`LOC`), Ações (`ACT`), Tempo (`TEMP`), Produtos (`PRODUTO`) e Mídia (`MIDIA`) das letras da banda brasileira Engenheiros do Hawaii.


## Tecnologias Utilizadas
* Python 3.9+
* spaCy 3.x

## Como Rodar o Projeto: Passo a Passo

Siga estas instruções para configurar o ambiente, treinar seu modelo do zero e executar a análise final. Todos os comandos devem ser executados de dentro da pasta `spacyConfig`.

### 1. Configuração do Ambiente (Setup)

Estes passos preparam seu computador para rodar o projeto.

**1.1. Clone o Repositório:**
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
```

**1.2. Instale as Dependências:**
Este comando lê o arquivo `requirements.txt` e instala a versão correta do spaCy.
```bash
pip install -r requirements.txt
```

### 2. Treinamento do Modelo NER Customizado

Esta etapa cria o seu modelo de IA a partir dos dados anotados, certifique de que você esta na pasta `spacyConfig`.

**2.1. Download do Modelo Base:**
O modelo customizado usa os "vetores de palavras" de um modelo grande do spaCy como ponto de partida. Baixe-o com o comando:
```bash
python -m spacy download pt_core_news_lg
```

**2.2. Preparação dos Dados de Treino:**
Este comando lê as anotações do arquivo `dados_treino.py` e as converte para o formato binário (`.spacy`) que o spaCy utiliza.
```bash
python preparar_dados.py
```
*Isso irá gerar os arquivos `train.spacy` e `dev.spacy` nesta pasta.*

**2.3. Execução do Treinamento:**
Este é o comando principal, que usa todos os arquivos de configuração e dados para treinar o modelo. O processo pode levar vários minutos.
```bash
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy
```
*Ao final, a pasta `output/model-best` será criada, contendo seu modelo treinado e pronto para uso.*

### 3. Execução da Análise (usando o `main.py`)

Com o modelo treinado, agora você pode usá-lo para analisar as músicas.

**3.1. Rode o Script Principal:**
Certifique-se de que você está fora da pasta `spacyConfig` e execute:
```bash
python main.py
```

**3.2. Verifique o Resultado:**
O script irá carregar seu modelo da pasta `spacyConfig/output/model-best`, analisar todas as músicas do arquivo `musicas.json` e gerar um relatório completo chamado **`relatorio_final.txt`** na mesma pasta.

---

## Resultados do Treinamento

O modelo foi treinado com sucesso utilizando os dados e configurações descritos neste repositório. O processo de treinamento foi executado até que a pontuação no conjunto de validação parasse de melhorar, garantindo que salvamos a melhor versão do modelo.

Abaixo está a tabela de progresso gerada pelo spaCy durante o treinamento:

```
 E     #     LOSS TOK2VEC  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
---  ------  ------------  --------  ------  ------  ------  ------
  0       0          0.00     65.81    0.00    0.00    0.00    0.00
 32     200         13.79   1272.75   82.76   92.31   75.00    0.83
 72     400         22.62     67.94   77.42   80.00   75.00    0.77
121     600         14.23     32.41   75.00   75.00   75.00    0.75
180     800          3.14      5.84   66.67   81.82   56.25    0.67
247    1000         29.81     44.99   66.67   81.82   56.25    0.67
338    1200         37.74     53.58   78.57   91.67   68.75    0.79
438    1400          6.15      9.35   75.86   84.62   68.75    0.76
538    1600          0.00      0.00   75.86   84.62   68.75    0.76
712    1800          0.00      0.00   75.86   84.62   68.75    0.76
```

### Entendendo a Tabela

* **`E` (Época):** Cada "época" representa um ciclo completo de aprendizado sobre todos os dados de treino.
* **`LOSS NER` (Erro):** Mostra o "erro" do modelo. O objetivo é que este número chegue o mais perto possível de zero, o que indica que o modelo aprendeu os exemplos.
* **`ENTS_P` (Precisão):** De todas as entidades que o modelo *identificou*, qual a porcentagem de acerto.
* **`ENTS_R` (Recall/Abrangência):** De todas as entidades que *existiam* no texto, qual a porcentagem que o modelo conseguiu encontrar.
* **`ENTS_F` / `SCORE`:** A pontuação final e mais importante. É um balanço entre a Precisão e o Recall. Quanto mais perto de `1.00` (ou 100.00), melhor.

### Análise Resumida dos Resultados

O treinamento foi um **sucesso**.

O modelo atingiu uma pontuação máxima (`SCORE`) de **0.83** (na época 32), o que é um **resultado excelente** para um modelo customizado com este volume de dados.

-   **Aprendizado:** O `LOSS NER` chegou a `0.00`, confirmando que o modelo foi poderoso o suficiente para aprender perfeitamente os exemplos fornecidos.
-   **Performance:** No seu pico, o modelo demonstrou uma **Precisão** altíssima de **92.31%** e um **Recall** muito bom de **75.00%**. Isso significa que ele é extremamente confiável nas entidades que aponta e consegue encontrar a maioria das entidades existentes no texto.

O spaCy salva automaticamente o melhor modelo deste treinamento na pasta `spacyConfig/output/model-best`, que é o utilizado pelo script `main.py` para a análise final.

---
_Este README documenta o fluxo de trabalho de um projeto de PLN para análise de letras musicais._
