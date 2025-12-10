# Vigenère Cipher Tool

Encrypt and decrypt text or files using the Vigenère Cipher
Supports .txt, .csv, .md, and .docx files

---

## Features

- Encrypt/decrypt text or file contents
- Supports multiple file types: .txt, .csv, .md, .docx
- Handles Windows paths and quotes automatically
- Outputs result to .txt file with automatic naming
- Menu-driven command-line interface

---

## Usage

### Run the tool

    python vigenere_cipher.py
    

### Menu Options

- Encrypt – input text or file path and keyword
- Decrypt – input text or file path and keyword
- Exit – quit the program

---

## File Paths

- Windows: C:\Users\Username\Documents\file.docx
- WSL/Linux: /mnt/c/Users/Username/Documents/file.docx
- Quotes are stripped automatically
- Backslashes are converted automatically

---

## Examples

Encrypt a file:

Encrypt, Decrypt, or Exit? encrypt
Type message or enter file path: C:/Users/asus/Downloads/example.docx
Enter keyword (letters only): SECRET
Output saved to encrypt_example.txt


Encrypt plain text:

Encrypt, Decrypt, or Exit? encrypt
Type message or enter file path: Hello World
Enter keyword (letters only): KEY
Result: Rijvs Uyvjn


---

## Requirements

- Python 3.x
- Libraries: python-docx (install with `pip install python-docx`)

---

## Skills Learned & Used

- Python: loops, functions, file I/O, string/byte manipulation
- Encryption: Vigenère Cipher, key-based encryption/decryption
- File handling: reading .docx and text files
- CLI design: menu, input validation, error handling

---

## License

MIT License
