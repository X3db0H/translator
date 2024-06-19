from googletrans import Translator
from art import tprint

result = ''
translator = Translator()
tprint("Translator")
dest_lan = str(input("На какой язык перевести? [ru/en]: "))
print("\nПеревожу...")


with open('translate.txt', 'r', encoding='utf-8') as in_f:
    text = in_f.read()

while True:
    first_dot_index = text.find('.')
    if first_dot_index != -1:
        sentence = text[:first_dot_index]
        text = text[first_dot_index + 1:]
        sentence = translator.translate(sentence, src='auto', dest=dest_lan)
        result += sentence.text + '. '
    elif first_dot_index == -1:
        break

# out_f = open('output.txt', 'w', encoding='utf-8')
# out_f.write(result)
# out_f.close()

with open('translate.txt', 'w', encoding='utf-8') as out_f:
    out_f.write(result)

print('\n')
print("Перевод завершен.")
input("Press enter to exit")
