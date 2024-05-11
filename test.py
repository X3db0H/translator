from googletrans import Translator
from art import tprint

result = ''
translator = Translator()
tprint("Translator")
tprint("For")
tprint("Viktoria")
dest_lan = str(input("Выбери язык [ru/en]: "))
file_name = input("Введи имя файла: ")
file_name += '.txt'
print("\nПеревожу...")


with open(file_name, 'r', encoding='utf-8') as in_f:
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

with open(file_name, 'w', encoding='utf-8') as out_f:
    out_f.write(result)

print('\n')
print("Перевод завершен.")
input("Press enter to exit")