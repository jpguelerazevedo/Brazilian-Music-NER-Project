from transformers import pipeline, AutoTokenizer
import json
from collections import Counter

# --- CONFIGURAÇÃO ---
CAMINHO_DO_MODELO = "./bertConfig/bert-ner-enghaw"
ARQUIVO_JSON_MUSICAS = "musicas.json"
ARQUIVO_SAIDA_RELATORIO = "relatorio_final_BERT.txt"


def carregar_pipeline_bert(caminho):
    """Carrega o pipeline e o tokenizador do modelo BERT treinado."""
    print(f"Carregando pipeline e tokenizador do modelo BERT de: '{caminho}'...")
    try:
        # Carregamos o pipeline SEM a estratégia de agregação
        nlp_pipeline = pipeline("ner", model=caminho, tokenizer=caminho)
        # Carregamos o tokenizador separadamente para poder juntar as palavras
        tokenizer = AutoTokenizer.from_pretrained(caminho)
        print("Pipeline e tokenizador do BERT carregados com sucesso!")
        return nlp_pipeline, tokenizer
    except Exception as e:
        print(f"--- ERRO: Não foi possível carregar o modelo/tokenizador do diretório '{caminho}'. Detalhe: {e}")
        return None, None

def agrupar_entidades(resultados_ner, tokenizer):
    """
    Função inteligente para juntar as subpalavras (ex: 'Fi', '##del')
    em entidades completas (ex: 'Fidel').
    """
    entidades_agrupadas = []
    entidade_atual = []

    for res in resultados_ner:
        palavra = res['word']
        label = res['entity']

        if label.startswith("B-"):
            # Se já havia uma entidade sendo formada, salva ela antes de começar uma nova
            if entidade_atual:
                tokens = [p['word'] for p in entidade_atual]
                texto_completo = tokenizer.convert_tokens_to_string(tokens)
                label_completa = entidade_atual[0]['entity'].replace("B-", "")
                entidades_agrupadas.append((texto_completo, label_completa))
            
            # Começa uma nova entidade
            entidade_atual = [res]
        
        elif label.startswith("I-") and entidade_atual:
            # Continua a entidade atual, adicionando o pedaço
            entidade_atual.append(res)
        
        else: # Se a label for "O" ou se começou uma entidade sem "B-"
            # Salva a entidade que estava sendo formada (se houver)
            if entidade_atual:
                tokens = [p['word'] for p in entidade_atual]
                texto_completo = tokenizer.convert_tokens_to_string(tokens)
                label_completa = entidade_atual[0]['entity'].replace("B-", "")
                entidades_agrupadas.append((texto_completo, label_completa))
            
            # Zera a entidade atual
            entidade_atual = []
            
    # Caso a última palavra do texto seja parte de uma entidade
    if entidade_atual:
        tokens = [p['word'] for p in entidade_atual]
        texto_completo = tokenizer.convert_tokens_to_string(tokens)
        label_completa = entidade_atual[0]['entity'].replace("B-", "")
        entidades_agrupadas.append((texto_completo, label_completa))

    return entidades_agrupadas


def main():
    nlp_pipeline, tokenizer = carregar_pipeline_bert(CAMINHO_DO_MODELO)
    if not nlp_pipeline:
        return

    try:
        with open(ARQUIVO_JSON_MUSICAS, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        musicas = dados.get('musicas', [])
        print(f"Arquivo '{ARQUIVO_JSON_MUSICAS}' com {len(musicas)} músicas lido com sucesso.")
    except Exception as e:
        print(f"--- ERRO: Não foi possível ler o arquivo de músicas '{ARQUIVO_JSON_MUSICAS}'. Detalhe: {e}")
        return

    entidades_por_musica = []
    contador_tipos = Counter()

    print("\nIniciando a análise das músicas com o modelo BERT treinado...")
    for musica in musicas:
        titulo = musica.get('titulo', 'Título Desconhecido')
        letra = musica.get('letra', '')
        
        # --- CORAÇÃO DA MUDANÇA ---
        if letra.strip():
            # 1. Aplicamos o pipeline, que agora retorna os pedaços (subpalavras)
            resultados_raw = nlp_pipeline(letra)
            
            # 2. Usamos nossa nova função para agrupar os pedaços
            ents = agrupar_entidades(resultados_raw, tokenizer)
        else:
            ents = []
        # ---------------------------

        entidades_por_musica.append((titulo, ents))

        for ent_text, ent_label in ents:
            contador_tipos[ent_label] += 1

    # O resto do código para gerar o relatório continua o mesmo
    with open(ARQUIVO_SAIDA_RELATORIO, 'w', encoding='utf-8') as f:
        f.write("====================================================\n")
        f.write("      RELATÓRIO DE ENTIDADES - MODELO BERT          \n")
        f.write("====================================================\n\n")

        f.write("==================================\n")
        f.write("  RESUMO AGREGADO POR CATEGORIA\n")
        f.write("==================================\n")
        for tipo, contagem in contador_tipos.most_common():
            f.write(f"- tipo {tipo} - ocorrência: {contagem}\n")
        
        f.write("\n\n")

        f.write("==================================\n")
        f.write("  ANÁLISE DETALHADA POR MÚSICA\n")
        f.write("==================================\n\n")
        for titulo, ents in entidades_por_musica:
            f.write(f"== {titulo.upper()} ==\n")
            if not ents:
                f.write("(Nenhuma entidade detectada)\n\n")
                continue
            for text, label in sorted(ents):
                f.write(f"- {text:<30} [{label}]\n")
            f.write('\n')

    print(f"\nAnálise concluída! Relatório salvo em: '{ARQUIVO_SAIDA_RELATORIO}'")


if __name__ == '__main__':
    main()