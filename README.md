# Vigenère Cipher Tool

A beginner-friendly Python tool to encrypt and decrypt messages or files using the **Vigenère Cipher**.

## Features

- Supports `.txt`, `.csv`, `.md`, and `.docx` files
- Can encrypt/decrypt typed messages directly
- Automatically strips quotes from file paths
- Handles Windows paths (backslashes converted to forward slashes)
- Preserves uppercase/lowercase letters
- Loops until the user exits
- Automatically creates output files (`encrypt_filename.txt`, `decrypt_filename.txt`)

## Installation

1. Install Python 3 and pip
2. (Optional but recommended) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

## Install required library:
    pip install python-docx

## Run the script:
    python vigenere_cipher.py
