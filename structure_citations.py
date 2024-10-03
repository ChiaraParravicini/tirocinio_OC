import os
import gzip
import json
from grobid_client.grobid_client import GrobidClient

# Crea il client GROBID - Modifica il path al config.json se necessario
client = GrobidClient(config_path="./config.json")

# Parametri principali
input_file = "0.json.gz"  # Nome del file gz con citazioni non strutturate
max_lines = 100  # Numero massimo di citazioni per ogni file .txt
service_name = "processCitationList"

# Creare una cartella per salvare le citazioni non strutturate
if not os.path.exists("unstructured"):
    os.makedirs("unstructured")

reference_list = []

# Leggere il file .json.gz e estrarre le citazioni non strutturate
with gzip.open(input_file, 'rb') as file_gz:
    json_file = file_gz.read().decode('utf-8')

json_content = json.loads(json_file)
items = json_content['items']

# Iterare attraverso gli item per estrarre le citazioni non strutturate
for item in items:
    if item.get('reference'):
        for reference in item['reference']:
            if reference.get("unstructured"):
                reference_list.append(reference['unstructured'])

# Funzione per scrivere le citazioni su file di testo
def write_references(reference_list, max_lines):
    file_index = 1
    current_line = 0
    file_path = f"unstructured/unstructured_{file_index}.txt"
    file = open(file_path, 'w')

    for reference in reference_list:
        cleaned_citation = reference.replace("\n", " ").replace("\r", " ")
        file.write(cleaned_citation + '\n')
        current_line += 1

        if current_line >= max_lines:
            file.close()
            file_index += 1
            file_path = f"unstructured/unstructured_{file_index}.txt"
            file = open(file_path, 'w')
            current_line = 0

    file.close()

# Scrivere le citazioni non strutturate nei file .txt
write_references(reference_list, max_lines)

# Crea una cartella per salvare i file XML strutturati
if not os.path.exists("structured"):
    os.makedirs("structured")

# Processa le citazioni e ottieni il risultato strutturato in formato XML
client.process(service_name, input_path="unstructured", output="structured", n=10, verbose=True, force=True)

print("Processing complete! The structured files are in the 'structured' directory.")
