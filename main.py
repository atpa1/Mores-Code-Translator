from flask import Flask, render_template, request, redirect
app = Flask(__name__)
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', " ": "/"}



@app.route('/', methods=['GET', 'POST'])
def main():
    try:
        if request.method == "POST":
            message = request.form["input"]
            mores_code = " ".join(MORSE_CODE_DICT[i] for i in message.upper())
            return render_template('index.html', output=mores_code, input=message)
    except KeyError:
        return render_template('index.html', error="Invalid character detected!")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

