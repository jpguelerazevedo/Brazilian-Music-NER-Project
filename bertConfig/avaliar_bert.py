# Arquivo: avaliar_bert.py (VERSÃO CORRIGIDA)
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    TrainingArguments,
    Trainer,
    DataCollatorForTokenClassification,
)
import numpy as np
import evaluate # <--- MUDANÇA 1: Novo import

# --- CONFIGURAÇÃO ---
CAMINHO_DO_MODELO = "./bert-ner-enghaw"

try:
    from dados_treino import DADOS_DE_VALIDACAO_IOB
except ImportError:
    print("ERRO: Arquivo 'dados_treino.py' não encontrado na mesma pasta.")
    exit()


print(f"1/4: Carregando modelo e tokenizador de '{CAMINHO_DO_MODELO}'...")
tokenizer = AutoTokenizer.from_pretrained(CAMINHO_DO_MODELO)
model = AutoModelForTokenClassification.from_pretrained(CAMINHO_DO_MODELO)

id2label = model.config.id2label

print("2/4: Preparando dados de validação...")
def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(examples["tokens"], truncation=True, is_split_into_words=True)
    labels = []
    for i, label_str_list in enumerate(examples["ner_tags_str"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            if word_idx is None: label_ids.append(-100)
            elif word_idx != previous_word_idx: label_ids.append(model.config.label2id.get(label_str_list[word_idx], 0))
            else: label_ids.append(-100)
            previous_word_idx = word_idx
        labels.append(label_ids)
    tokenized_inputs["labels"] = labels
    return tokenized_inputs

dataset_validacao_hf = Dataset.from_list(DADOS_DE_VALIDACAO_IOB)
tokenized_eval_dataset = dataset_validacao_hf.map(tokenize_and_align_labels, batched=True)

# --- MUDANÇA 2: Carregando a métrica com a nova biblioteca ---
metric = evaluate.load("seqeval")

def compute_metrics(p):
    predictions, labels = p
    predictions = np.argmax(predictions, axis=2)
    true_predictions = [[id2label[p] for (p, l) in zip(prediction, label) if l != -100] for prediction, label in zip(predictions, labels)]
    true_labels = [[id2label[l] for (p, l) in zip(prediction, label) if l != -100] for prediction, label in zip(predictions, labels)]
    results = metric.compute(predictions=true_predictions, references=true_labels)
    return {"precision": results["overall_precision"], "recall": results["overall_recall"], "f1": results["overall_f1"]}

print("3/4: Configurando o avaliador...")
training_args = TrainingArguments(output_dir="./temp_eval")

trainer = Trainer(
    model=model,
    args=training_args,
    eval_dataset=tokenized_eval_dataset,
    tokenizer=tokenizer,
    data_collator=DataCollatorForTokenClassification(tokenizer=tokenizer),
    compute_metrics=compute_metrics,
)

print("4. Executando a avaliação...")
resultados = trainer.evaluate()

print("\n--- SCORE FINAL DO MODELO BERT ---")
print("   (Baseado nos dados de validação)")
print("------------------------------------")
for metrica, valor in resultados.items():
    if "eval" in metrica:
        print(f"{metrica}: {valor:.4f}")