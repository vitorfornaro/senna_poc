import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MAPS_DIR = os.path.join(BASE_DIR, "..", "maps")
    
    # Pastas fonte e destino
    ENCRYPTED_FOLDER = os.path.join(MAPS_DIR, "encrypted")
    DECRYPTED_FOLDER = os.path.join(MAPS_DIR, "decrypted")
    PROCESSED_ENCRYPTED_FOLDER = os.path.join(ENCRYPTED_FOLDER, "processed")
    PROCESSED_DECRYPTED_FOLDER = os.path.join(DECRYPTED_FOLDER, "processed")

    # Pastas para os outputs
    OUTPUT_FOLDER = os.path.join(MAPS_DIR, "outputs")
    CSV_OUTPUT = os.path.join(OUTPUT_FOLDER, "csv")
    JSON_OUTPUT = os.path.join(OUTPUT_FOLDER, "json")

    # Criar pastas se não existirem
    os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
    os.makedirs(DECRYPTED_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_ENCRYPTED_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_DECRYPTED_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    os.makedirs(CSV_OUTPUT, exist_ok=True)
    os.makedirs(JSON_OUTPUT, exist_ok=True)