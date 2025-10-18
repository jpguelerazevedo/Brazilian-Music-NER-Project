# Análise Comparativa de NER em Letras de Músicas: spaCy vs. BERT

Este projeto de Processamento de Linguagem Natural (PLN) treina e compara dois modelos customizados para a tarefa de Reconhecimento de Entidades Nomeadas (NER). O objetivo é extrair e classificar entidades como Pessoas (`PER`), Lugares (`LOC`), Ações (`ACT`), Tempo (`TEMP`), Produtos (`PRODUTO`) e Mídia (`MIDIA`) das letras da banda brasileira Engenheiros do Hawaii.

1.  Um modelo treinado do zero com a biblioteca **spaCy**.
2.  Um modelo pré-treinado **BERT (BERTimbau)** que passa por um processo de fine-tuning com a biblioteca **Hugging Face Transformers**.

## Tecnologias Utilizadas
* Python 3.9+
* spaCy 3.x
* Hugging Face Transformers
* PyTorch
* Datasets & Evaluate (Hugging Face)

## Como Rodar o Projeto: Passo a Passo

Siga estas instruções para configurar o ambiente e depois treinar e avaliar cada modelo.

### 1. Configuração do Ambiente (Setup Comum)

Estes passos são necessários para ambos os modelos.

**1.1. Clone o Repositório:**
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
```

**1.2. Navegue até a Pasta de Trabalho:**
É crucial executar todos os comandos de dentro da subpasta `spacyConfig`.
```bash
cd seu-repositorio/NER/spacyConfig
```

**1.3. Instale as Dependências:**
```bash
pip install -r requirements.txt
```

### 2. Opção A: Treinando e Usando o Modelo spaCy

**2.1. Download do Modelo Base:**
```bash
python -m spacy download pt_core_news_lg
```

**2.2. Preparação dos Dados:**
```bash
python preparar_dados.py
```

**2.3. Treinamento:**
```bash
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy
```

**2.4. Execução da Análise:**
```bash
python mainSpacy.py
```
*Um relatório chamado `relatorio_final_Spacy.txt` será gerado.*

### 3. Opção B: Treinando e Usando o Modelo BERT

**3.1. Treinamento (Fine-tuning):**
```bash
python bertFinetunning.py
```
*O modelo final será salvo na pasta `bert-ner-enghaw`.*

**3.2. Execução da Análise:**
```bash
python mainBert.py
```
*Um relatório chamado `relatorio_final_BERT.txt` será gerado.*

---

## 🏁 Resultados Finais e Comparação

O objetivo final é comparar as métricas de performance de cada modelo para determinar qual abordagem se saiu melhor nesta tarefa específica.

### Resultados - Modelo spaCy

O treinamento com spaCy (otimizado para `accuracy`) foi um **sucesso**.

* **Pontuação Máxima (F1-Score):** O modelo atingiu um `SCORE` de **0.83**.
* **Aprendizado:** O `LOSS NER` chegou a `0.00`, confirmando que o modelo aprendeu perfeitamente os exemplos.
* **Perfil:** No seu pico, o modelo demonstrou altíssima **Precisão (92.31%)** e bom **Recall (75.00%)**, indicando que é um modelo muito confiável.

**Tabela de Progresso (spaCy):**
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

### Resultados - Modelo BERT

O fine-tuning do modelo BERT (BERTimbau) também foi um **grande sucesso**, atingindo uma performance geral superior à do modelo spaCy.

* **Pontuação Final (F1-Score):** **0.87** (`eval_f1: 0.8667`)
* **Precisão (`eval_precision`):** **92.86%**
* **Recall (`eval_recall`):** **81.25%**

**Análise Resumida:**
Com um F1-Score de **0.87**, o modelo BERT se mostrou o vencedor nesta comparação. Ele não só atingiu uma **Precisão altíssima (92.86%)**, similar à do spaCy, mas também obteve um **Recall significativamente maior (81.25% vs 75.00% do spaCy)**. Isso significa que, além de ser muito confiável quando identifica uma entidade, o modelo BERT foi menos "tímido" e conseguiu **encontrar mais entidades** corretas no texto, tornando-o o modelo mais completo e eficaz para esta tarefa.

**Porém, é importante notar um desafio técnico:** o modelo BERT, por sua natureza, quebra palavras desconhecidas em "subpalavras" (tokens), que aparecem com um prefixo `##` (ex: `Fidel` -> `Fi` + `##del`), o que inicialmente "danificou" a legibilidade do relatório de entidades. Isso demonstra que, embora o modelo BERT seja mais poderoso, ele pode ter complicações em sua execução em comparação com a saída mais direta do spaCy.

Para uma análise visual e interativa dos gráficos de treinamento do BERT, utilize o TensorBoard:
```bash
# Execute em um novo terminal, na pasta spacyConfig
tensorboard --logdir ./bert-ner-enghaw
```
*Abra o link `http://localhost:6006/` no seu navegador para ver o dashboard.*

---
_Este README documenta o fluxo de trabalho de um projeto de PLN para análise e comparação de modelos NER em letras musicais._
