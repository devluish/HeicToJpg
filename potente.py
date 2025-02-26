import os
from PIL import Image
from pillow_heif import register_heif_opener

#CÓDIGO DESENVOLVIDO PARA TRANSFORMAR ARQUIVOS HEIC PARA JPG
register_heif_opener()

def convert_heic_to_jpeg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

            try:
                image = Image.open(input_path)
                image.save(output_path, "JPEG")
                print(f"Convertido: {filename} -> {output_path}")
            except Exception as e:
                print(f"Erro ao converter {filename}: {e}")

# Basta adicionar o caminho entre as pastas, para que o programa seja executado corretamente.

if __name__ == "__main__":
    input_folder = r"D:\desktop\HEIC2"
    output_folder = r"D:\desktop\AQUI"

    convert_heic_to_jpeg(input_folder, output_folder)
