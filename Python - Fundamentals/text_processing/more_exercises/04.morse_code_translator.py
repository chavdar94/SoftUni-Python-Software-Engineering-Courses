morse_code = input().split(" | ")

morse_code_dict = {'..-.': 'F', '-..-': 'X',
                   '.--.': 'P', '-': 'T', '..---': '2',
                   '....-': '4', '-----': '0', '--...': '7',
                   '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                   '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                   '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                   '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                   '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                   '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

message = ''
for letter in morse_code:
    for ltr in letter.split(" "):
        if ltr != '':
            message += morse_code_dict[ltr]
    message += ' '

print(message)
