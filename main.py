from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cryptography.fernet import Fernet
import os
import sys

app = FastAPI()

KEY_FILE = "secret.key"

class DataModel(BaseModel):
    data: str

class EncryptedModel(BaseModel):
    encrypted_data: str

def write_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        raise HTTPException(status_code=404, detail="Key not found. Please generate a key first.")
    return open(KEY_FILE, "rb").read()

def encrypt_data(data: str) -> str:
    key = load_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data.decode()

def decrypt_data(encrypted_data: str) -> str:
    key = load_key()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data.encode())
    return decrypted_data.decode()

@app.post("/generate_key")
async def generate_key():
    try:
        write_key()
        return {"message": "Key generated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/encrypt")
async def encrypt(data: DataModel):
    try:
        encrypted = encrypt_data(data.data)
        return {"encrypted_data": encrypted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/decrypt")
async def decrypt(encrypted: EncryptedModel):
    try:
        decrypted = decrypt_data(encrypted.encrypted_data)
        return {"decrypted_data": decrypted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import uvicorn
print(f"Starting server on http://127.0.0.1:8000")
uvicorn.run(app, host="127.0.0.1", port=8000)