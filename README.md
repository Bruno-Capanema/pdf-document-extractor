# 📄 PDF Document Extractor

Um script em Python para **extrair automaticamente páginas de arquivos PDF que contenham “documento” no nome e salvar cada página como imagem PNG**.

Esse projeto foi criado para automatizar e agilizar a organização de documentos escaneados em pastas de clientes.

---

## 📌 Por que este projeto existe

Quando você tem muitos documentos em PDF em várias pastas de clientes, extrair manualmente cada página como imagem pode ser trabalhoso.

Esse script percorre todas as pastas de clientes automaticamente e converte cada página dos PDFs relevantes em imagens. :contentReference[oaicite:0]{index=0}

---

## 🗂 Estrutura de diretórios esperada


Desktop/
└── DOCUMENTOS/
├── Cliente A/
│ ├── documento_rg.pdf
│ └── documento_cpf.pdf
├── Cliente B/
└── ...


Após a execução, cada cliente terá:


Cliente A/
└── IMAGENS_EXTRAIDAS/
├── documento_rg/
│ ├── pagina_1.png
│ ├── pagina_2.png
│ └── ...
└── documento_cpf/
├── pagina_1.png
└── ...


---

## 🛠️ Tecnologias e dependências

O projeto foi construído com:

- 🐍 **Python 3.12+**
- 📦 Biblioteca **PyMuPDF**

Para instalar a dependência:

```bash
pip install pymupdf

Ou usando o arquivo de dependências:

pip install -r requirements.txt
▶️ Como usar

Baixe ou clone este repositório.

Ajuste o caminho da variável base_path no script caso necessário.

Execute no terminal:

python extrair.py

O script irá varrer todas as subpastas dentro de DOCUMENTOS e criar a pasta IMAGENS_EXTRAIDAS com as imagens extraídas.

📁 Conteúdo do projeto

extrair.py – Script principal de extração

requirements.txt – Dependências do projeto

🧠 Melhoria e Manutenção

Esse README segue as boas práticas recomendadas pelo GitHub para documentação de projetos em Markdown, como descrever o propósito, estrutura, instalação e uso.

📝 Licença

Este projeto está sob a MIT License (opcional — adicione se desejar um arquivo LICENSE).

👤 Autor

Bruno Capanema – projeto pessoal para automação de extração de documentos
