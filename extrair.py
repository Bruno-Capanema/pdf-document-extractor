import os
import fitz  # PyMuPDF

base_path = r"C:\Users\Financeiro-02\OneDrive\Desktop\DOCUMENTOS"

for pasta_cliente in os.listdir(base_path):
    caminho_cliente = os.path.join(base_path, pasta_cliente)

    if os.path.isdir(caminho_cliente):
        print(f"\n📂 Verificando {pasta_cliente}")

        pasta_saida = os.path.join(caminho_cliente, "IMAGENS_EXTRAIDAS")
        os.makedirs(pasta_saida, exist_ok=True)

        for arquivo in os.listdir(caminho_cliente):
            if arquivo.lower().endswith(".pdf") and "documento" in arquivo.lower():

                caminho_pdf = os.path.join(caminho_cliente, arquivo)
                print(f"   📄 Extraindo {arquivo}")

                pdf = fitz.open(caminho_pdf)
                nome_base = os.path.splitext(arquivo)[0]
                pasta_pdf = os.path.join(pasta_saida, nome_base)
                os.makedirs(pasta_pdf, exist_ok=True)

                for i in range(len(pdf)):
                    pagina = pdf[i]
                    pix = pagina.get_pixmap(dpi=150)
                    pix.save(os.path.join(pasta_pdf, f"pagina_{i+1}.png"))

                pdf.close()

print("\n✅ FINALIZADO")