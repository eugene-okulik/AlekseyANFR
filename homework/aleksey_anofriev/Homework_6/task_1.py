# Задание №1
# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте 
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero” 
# и после этого выводит получившийся текст на экран. Знаки препинания не должны оказаться внутри слова. 
# Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова, 
# но уже преобразованного.

text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

words = text.split()
fin_words = []

for word in words:
    if word.endswith(','):
        new_word = word[:-1] + "ing" + ','
    elif word.endswith('.'):
        new_word = word[:-1] + "ing" + '.'
    else:
        new_word = word + "ing"
    fin_words.append(new_word)
print(' '.join(fin_words))
