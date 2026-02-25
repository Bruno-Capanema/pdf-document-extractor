import os
import re
import fitz  # PyMuPDF

base_path = r"C:\Users\Financeiro-02\OneDrive\Desktop\DOCUMENTOS"

def limpar_nome(nome):
    """
    Remove espaços extras e caracteres inválidos no Windows
    """
    nome = nome.strip()
    nome = re.sub(r'[<>:"/\\|?*]', '', nome)
    return nome

for pasta_cliente in os.listdir(base_path):
    caminho_cliente = os.path.join(base_path, pasta_cliente)

    if os.path.isdir(caminho_cliente):
        nome_pasta_limpo = limpar_nome(pasta_cliente)

        print(f"\n📂 Verificando {pasta_cliente}")

        pasta_saida = os.path.join(caminho_cliente, "IMAGENS_EXTRAIDAS")
        os.makedirs(pasta_saida, exist_ok=True)

        for arquivo in os.listdir(caminho_cliente):
            if arquivo.lower().endswith(".pdf") and "documento" in arquivo.lower():

                caminho_pdf = os.path.join(caminho_cliente, arquivo)
                print(f"   📄 Extraindo {arquivo}")

                try:
                    pdf = fitz.open(caminho_pdf)

                    nome_base = os.path.splitext(arquivo)[0]
                    nome_base = limpar_nome(nome_base)

                    pasta_pdf = os.path.join(pasta_saida, nome_base)
                    os.makedirs(pasta_pdf, exist_ok=True)

                    for i in range(len(pdf)):
                        try:
                            pagina = pdf[i]
                            pix = pagina.get_pixmap(dpi=150)

                            nome_imagem = f"{nome_pasta_limpo}_pagina_{i+1}.png"

                            caminho_imagem = os.path.join(
                                pasta_pdf, nome_imagem
                            )

                            pix.save(caminho_imagem)

                        except Exception as erro_pagina:
                            print(f"      ⚠ Erro na página {i+1}: {erro_pagina}")

                    pdf.close()
                    print("      ✔ Concluído")

                except Exception as erro_pdf:
                    print(f"   ❌ Erro ao processar {arquivo}: {erro_pdf}")

print("\n✅ FINALIZADO")