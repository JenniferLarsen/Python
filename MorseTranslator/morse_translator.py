"""
Jennifer Larsen
11/28/2023
This program takes user input in Morse Code and returns the translated text.
"""

import tkinter as tk

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}


class MorseCodeTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Translator")

        self.label1 = tk.Label(root, text="Enter Morse Code:")
        self.label1.pack()

        self.morse_entry = tk.Entry(root)
        self.morse_entry.pack()

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_morse)
        self.translate_button.pack()

        self.label2 = tk.Label(root, text="Translated Text:")
        self.label2.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def translate_morse(self):
        morse_code = self.morse_entry.get()
        translated_text = self.decode_morse_code(morse_code.upper())
        self.result_label.config(text=translated_text)

    def decode_morse_code(self, morse_code):
        words = morse_code.split('   ')  # Morse code words are separated by three spaces
        decoded_text = ""

        for word in words:
            letters = word.split(' ')
            for letter in letters:
                for char, code in morse_code_dict.items():
                    if letter == code:
                        decoded_text += char
            decoded_text += ' '

        return decoded_text.strip()


if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeTranslator(root)
    root.mainloop()
