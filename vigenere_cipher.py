from docx import Document
import os

def vigenere_cipher(text, keyword, mode='encrypt'):
    result = ""
    keyword = keyword.upper()
    keyword_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            if mode == 'decrypt':
                shift = -shift
            result += chr((ord(char) - base + shift) % 26 + base)
            keyword_index += 1
        else:
            result += char
    return result

def read_docx(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.txt', '.csv', '.md']:
        with open(file_path, 'r') as f:
            return f.read()
    elif ext == '.docx':
        return read_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Use .txt, .csv, .md, or .docx")

print("Vigenère Cipher Tool (supports .txt, .docx, .csv, .md)")

while True:
    mode = input("\nEncrypt, Decrypt, or Exit? ").lower()
    if mode == "exit":
        break
    if mode not in ["encrypt", "decrypt"]:
        print("Invalid option. Try again.")
        continue

    file_or_text = input("Type message or enter file path: ").strip()
    file_or_text = file_or_text.strip('"').strip("'")  # Remove quotes
    file_or_text = file_or_text.replace("\\", "/")     # Convert Windows backslashes

    keyword = input("Enter keyword (letters only): ").strip()
    if not keyword.isalpha():
        print("Keyword must contain only letters.")
        continue

    try:
        # Try reading file
        text = read_file(file_or_text)
        result = vigenere_cipher(text, keyword, mode)
        # Output file always as .txt
        output_file = f"{mode}_{os.path.basename(file_or_text).split('.')[0]}.txt"
        with open(output_file, 'w') as f:
            f.write(result)
        print(f"Output saved to {output_file}")
    except FileNotFoundError:
        # If not a file, treat as plain text
        result = vigenere_cipher(file_or_text, keyword, mode)
        print("Result:", result)
    except ValueError as ve:
        print(ve)
