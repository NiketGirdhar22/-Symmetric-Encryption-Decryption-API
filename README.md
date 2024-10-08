
# Encryption and Decryption API

This is a FastAPI-based application that provides encryption and decryption services using symmetric encryption with the **Fernet** algorithm from the `cryptography` library. The application allows users to securely encrypt and decrypt data using a generated encryption key stored in a file.

## Features

- **Key Generation**: Generate a new encryption key stored in a file.
- **Encrypt Data**: Encrypt plain text data using the generated key.
- **Decrypt Data**: Decrypt encrypted data using the same key.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Cryptography

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/encryption-api.git
   cd encryption-api
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install fastapi uvicorn cryptography
   ```

## Running the Application

1. **Start the FastAPI server**:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server on `http://127.0.0.1:8000`.

2. **API Endpoints**:

   - **Generate Key**:
     - **URL**: `/generate_key`
     - **Method**: `POST`
     - **Description**: Generates a new encryption key and saves it to `secret.key`.

     ```bash
     curl -X POST "http://127.0.0.1:8000/generate_key"
     ```

   - **Encrypt Data**:
     - **URL**: `/encrypt`
     - **Method**: `POST`
     - **Request Body**: `{ "data": "your_text_here" }`
     - **Description**: Encrypts the provided data using the stored key.

     ```bash
     curl -X POST "http://127.0.0.1:8000/encrypt" -H "Content-Type: application/json" -d '{"data": "Hello World"}'
     ```

   - **Decrypt Data**:
     - **URL**: `/decrypt`
     - **Method**: `POST`
     - **Request Body**: `{ "encrypted_data": "your_encrypted_text_here" }`
     - **Description**: Decrypts the provided encrypted data using the stored key.

     ```bash
     curl -X POST "http://127.0.0.1:8000/decrypt" -H "Content-Type: application/json" -d '{"encrypted_data": "gAAAA..."}'
     ```

## Project Structure

```plaintext
.
├── main.py                # The main FastAPI app
├── secret.key             # Generated encryption key (created after running `/generate_key`)
└── README.md              # Project documentation
```

## Encryption Key Management

- The key used for encryption and decryption is stored in a file called `secret.key`. This key is essential for both processes, so be sure to back it up. If the key is deleted or lost, encrypted data cannot be decrypted.
- You can generate a new key by accessing the `/generate_key` endpoint.

## Usage Notes

- Ensure that the encryption key (`secret.key`) is securely stored and not shared publicly.
- The same key is used for both encrypting and decrypting data, so access to the key file should be restricted.
- If no key is present, you will get an HTTP 404 error when trying to encrypt or decrypt data.

## Author

Created by Niket Girdhar.
