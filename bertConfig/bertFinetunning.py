from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    TrainingArguments,
    Trainer,
    DataCollatorForTokenClassification,
)

try:
    from dados_treino import DADOS_DE_TREINO_IOB, DADOS_DE_VALIDACAO_IOB
except ImportError:
    print("ERRO: Arquivo 'dados_treino.py' não encontrado na mesma pasta.")
    exit()

# --- CONFIGURAÇÃO ---
MODELO_BASE_BERT = "neuralmind/bert-base-portuguese-cased"
NOME_DO_MODELO_FINETUNED = "bert-ner-enghaw"

print("1/4: Lendo dados no formato IOB2...")
dados_treino_iob = DADOS_DE_TREINO_IOB
dados_validacao_iob = DADOS_DE_VALIDACAO_IOB

todas_as_labels_unicas = sorted(list(set(tag.split('-')[-1] for data in dados_treino_iob + dados_validacao_iob for tag in data['ner_tags_str'] if tag != "O")))

b_labels = [f"B-{label}" for label in todas_as_labels_unicas]
i_labels = [f"I-{label}" for label in todas_as_labels_unicas]
all_ner_labels = ["O"] + b_labels + i_labels
ner_label2id = {label: i for i, label in enumerate(all_ner_labels)}
id2label = {i: label for i, label in enumerate(all_ner_labels)}

print(f"Labels encontradas e mapeadas: {', '.join(todas_as_labels_unicas)}")

print("2/4: Carregando tokenizador e modelo base do BERTimbau...")
tokenizer = AutoTokenizer.from_pretrained(MODELO_BASE_BERT)

def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(examples["tokens"], truncation=True, is_split_into_words=True)
    labels = []
    for i, label_str_list in enumerate(examples["ner_tags_str"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != previous_word_idx:
                label_ids.append(ner_label2id.get(label_str_list[word_idx], 0))
            else:
                label_ids.append(-100)
            previous_word_idx = word_idx
        labels.append(label_ids)
    tokenized_inputs["labels"] = labels
    return tokenized_inputs

print("3/4: Criando e processando datasets...")
dataset_treino_hf = Dataset.from_list(dados_treino_iob)
dataset_validacao_hf = Dataset.from_list(dados_validacao_iob)

tokenized_train_dataset = dataset_treino_hf.map(tokenize_and_align_labels, batched=True)
tokenized_eval_dataset = dataset_validacao_hf.map(tokenize_and_align_labels, batched=True)

model = AutoModelForTokenClassification.from_pretrained(
    MODELO_BASE_BERT, num_labels=len(all_ner_labels), id2label=id2label, label2id=ner_label2id
)

print("4/4: Configurando e iniciando o treinamento...")
# --- BLOCO CORRIGIDO PARA VERSÕES ANTIGAS ---
training_args = TrainingArguments(
    output_dir=NOME_DO_MODELO_FINETUNED,
    num_train_epochs=100,
    per_device_train_batch_size=8,
)
# -----------------------------------------

data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

trainer.train()

trainer.save_model(f"./{NOME_DO_MODELO_FINETUNED}")
print(f"Treinamento concluído! Modelo salvo em './{NOME_DO_MODELO_FINETUNED}'")