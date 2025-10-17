import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


def _download_nltk_if_needed():
    # Baixa 'punkt' e 'stopwords' se estiverem ausentes
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)


def tokenize_fallback(text):
    """Tokenização simples por regex usada quando o NLTK não está disponível.

    Retorna uma lista de tokens (palavras e sinais de pontuação).
    Exemplo: "Olá, mundo!" -> ['Olá', ',', 'mundo', '!']
    """
    # regex: captura sequências de caracteres alfanuméricos (\w+) ou
    # qualquer caractere de pontuação isolado ([^\w\s]).
    # Usa [^\w\s] em vez de listar aspas para evitar conflitos com
    # delimitadores de string no código.
    return re.findall(r"\w+|[^\w\s]", text, flags=re.UNICODE)


def remover_stopwords_de_arquivo(entrada='musicas.json', saida='musicas_sem_stopwords.json'):
    _download_nltk_if_needed()

    try:
        stopwords_pt = set(stopwords.words('portuguese'))
    except Exception:
        print('ERRO: stopwords não disponíveis.')
        return

    punctuation = set(string.punctuation)

    try:
        with open(entrada, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except Exception as e:
        print(f'ERRO ao ler {entrada}: {e}')
        return

    musicas = dados.get('musicas', [])
    resultado = []
    for m in musicas:
        titulo = m.get('titulo', '')
        letra = m.get('letra', '') or ''

        # tenta usar word_tokenize; se falhar, usa o fallback
        try:
            tokens = word_tokenize(letra.lower())
        except Exception:
            tokens = tokenize_fallback(letra.lower())

        filtrados = [t for t in tokens if t not in stopwords_pt and t not in punctuation]
        letra_limpa = ' '.join(filtrados)

        resultado.append({
            'titulo': titulo,
            'album': m.get('album'),
            'ano': m.get('ano'),
            'letra_sem_stopwords': letra_limpa
        })

    out = {'banda': dados.get('banda'), 'musicas': resultado}
    try:
        with open(saida, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print(f'Arquivo gerado: {saida}')
    except Exception as e:
        print(f'ERRO ao salvar {saida}: {e}')


if __name__ == '__main__':
    remover_stopwords_de_arquivo()