from flask import Flask, render_template, request

app = Flask(__name__)

# Morse code dictionary
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

inverse_morse_dict = {v: k for k, v in morse_dict.items()}

def encrypt(text):
    words = text.strip().split()
    encrypted_words = []
    for word in words:
        encrypted_letters = []
        for char in word.upper():
            if char in morse_dict:
                encrypted_letters.append(morse_dict[char])
        encrypted_words.append(' '.join(encrypted_letters))
    return ' / '.join(encrypted_words)

def decrypt(morse_code):
    words = [word for word in morse_code.strip().split(' / ') if word]
    decrypted_words = []
    for word in words:
        letters = word.split()
        decrypted_letters = []
        for letter in letters:
            if letter in inverse_morse_dict:
                decrypted_letters.append(inverse_morse_dict[letter])
        decrypted_words.append(''.join(decrypted_letters))
    return ' '.join(decrypted_words)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'encrypt':
            input_text = request.form.get('input_text')
            result = encrypt(input_text)
        elif action == 'decrypt':
            input_text = request.form.get('input_text')
            result = decrypt(input_text)
        else:
            result = "Invalid action"
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == "__main__":
    app.run(debug=True)