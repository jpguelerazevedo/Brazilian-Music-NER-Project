import spacy
from spacy.tokens import DocBin
import re

try:
    from dados_treino import DADOS_DE_TREINO, DADOS_DE_VALIDACAO
except ImportError:
    print("ERRO: Não foi possível encontrar o arquivo 'dados_treino.py'.")
    exit()

def converter_dados_inteligente(nome_arquivo, dados):
    nlp = spacy.blank("pt")
    db = DocBin()

    for text, anots in dados:
        doc = nlp.make_doc(text)
        ents = []
        
        # --- LÓGICA INTELIGENTE ---
        # Converte o formato (palavra, label) para (inicio, fim, label)
        for palavra, label in anots:
            # Usa regex para encontrar a palavra exata no texto
            # re.escape lida com caracteres especiais como '?' ou '.'
            matches = list(re.finditer(re.escape(palavra), text, re.IGNORECASE))
            if matches:
                # Pega o primeiro match encontrado
                start, end = matches[0].span()
                span = doc.char_span(start, end, label=label)
                if span:
                    ents.append(span)
                else:
                    # Este aviso agora é mais sério, indica um problema de tokenização
                    print(f"Aviso de Alinhamento: Span não criado para '{palavra}' em '{text}'")
            else:
                print(f"Aviso de Busca: Palavra '{palavra}' não encontrada no texto '{text}'")
        
        try:
            doc.ents = ents
            db.add(doc)
        except ValueError:
            print(f"Aviso: Anotações sobrepostas no texto: '{text}'. Exemplo pulado.")

    db.to_disk(nome_arquivo)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

if __name__ == "__main__":
    print("Iniciando a conversão dos dados (MÉTODO INTELIGENTE)...")
    converter_dados_inteligente("./train.spacy", DADOS_DE_TREINO)
    converter_dados_inteligente("./dev.spacy", DADOS_DE_VALIDACAO)
    print("\nConversão concluída!")