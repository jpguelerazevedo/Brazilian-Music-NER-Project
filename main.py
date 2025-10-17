import spacy
import json
from collections import Counter

# --- CONFIGURAÇÃO ---
CAMINHO_DO_MODELO = "spacyConfig/output/model-best"
ARQUIVO_JSON_MUSICAS = "musicas.json"
ARQUIVO_SAIDA_RELATORIO = "relatorio_final.txt"


def carregar_modelo_customizado(caminho):
    print(f"Carregando modelo customizado de: '{caminho}'...")
    try:
        nlp = spacy.load(caminho)
        print("Modelo carregado com sucesso!")
        return nlp
    except Exception as e:
        print(f"--- ERRO: Não foi possível carregar o modelo do diretório '{caminho}'. Detalhe: {e}")
        return None

def main():
    nlp_custom = carregar_modelo_customizado(CAMINHO_DO_MODELO)
    if not nlp_custom:
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
    
    # --- MUDANÇA 1: Adicionado um novo contador para os TIPOS de entidade ---
    contador_tipos = Counter()

    print("\nIniciando a análise das músicas com o modelo treinado...")
    for musica in musicas:
        titulo = musica.get('titulo', 'Título Desconhecido')
        letra = musica.get('letra', '')
        
        doc = nlp_custom(letra)
        ents = [(ent.text, ent.label_) for ent in doc.ents]
        
        entidades_por_musica.append((titulo, ents))

        # --- MUDANÇA 2: Populamos o novo contador de tipos ---
        for ent_text, ent_label in ents:
            contador_tipos[ent_label] += 1

    # Escrita do relatório final
    with open(ARQUIVO_SAIDA_RELATORIO, 'w', encoding='utf-8') as f:
        f.write("====================================================\n")
        f.write("    RELATÓRIO DE ENTIDADES - MODELO CUSTOMIZADO     \n")
        f.write("====================================================\n\n")

        for titulo, ents in entidades_por_musica:
            f.write(f"== {titulo.upper()} ==\n")
            if not ents:
                f.write("(Nenhuma entidade detectada)\n\n")
                continue
            for text, label in sorted(ents):
                f.write(f"- {text:<30} [{label}]\n")
            f.write('\n')

        f.write('\n==================================\n')
        f.write('  RESUMO AGREGADO POR CATEGORIA\n')
        f.write('==================================\n')
        
        # --- MUDANÇA 3: O loop de resumo foi substituído por este ---
        # Itera sobre o contador de tipos e escreve no formato solicitado.
        for tipo, contagem in contador_tipos.most_common():
            f.write(f"- tipo {tipo} - ocorrência: {contagem}\n")

    print(f"\nAnálise concluída! Relatório salvo em: '{ARQUIVO_SAIDA_RELATORIO}'")


if __name__ == '__main__':
    main()