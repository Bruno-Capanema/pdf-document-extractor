
# 📄 PDF Document Extractor

Script em Python para extrair automaticamente páginas de arquivos PDF que contenham “documento” no nome e salvar cada página como imagem PNG organizada por cliente.

---

## 🚀 O que o script faz

✔ Percorre automaticamente todas as subpastas dentro de `DOCUMENTOS`  
✔ Identifica PDFs que contenham "documento" no nome  
✔ Extrai cada página como imagem PNG  
✔ Cria automaticamente a pasta `IMAGENS_EXTRAIDAS`  
✔ Nomeia as imagens no formato:

NOME_DA_PASTA_pagina_1.png  
NOME_DA_PASTA_pagina_2.png  

✔ Remove espaços extras e caracteres inválidos  
✔ Trata erros de PDF corrompido  
✔ Não interrompe a execução em caso de erro isolado  

---

## ▶️ Como Executar

1. Ajuste a variável `base_path` no script.
2. Execute:

python extrair.py

---

## 🛠 Dependência

pip install pymupdf
