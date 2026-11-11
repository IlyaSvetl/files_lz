import re
from collections import Counter
from docx import Document

#  Чтение текста из docx 
document = Document('lion.docx')
doc = '\n'.join(p.text for p in document.paragraphs)

# Статистика по словам
words = re.findall(r"[А-Яа-яЁёA-Za-z]+(?:-[А-Яа-яЁёA-Za-z]+)*", doc)
total_words = len(words)
word_counts = Counter(words)
sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

# Запись таблицы слов в файл
with open('word_statistics.txt', 'w', encoding='utf-8') as f:
    f.write('Слово\tЧастота встречи, раз\tЧастота встречи в %\n')
    for word, count in sorted_words:
        percent = count / total_words * 100
        f.write(f'{word}\t{count}\t{percent:.2f}\n')

print(f'Всего слов: {total_words}')
print('Статистика  word_statistics.txt') #статистика сохранена в txt файл

# Статистика по буквам 
letters = [ch.lower() for ch in doc if re.match(r'[А-Яа-яЁёA-Za-z]', ch)]
letter_counts = Counter(letters)
sorted_letters = sorted(letter_counts.items())

print('\nВстречаемость букв:')
for letter, count in sorted_letters:
    bar = '#' * (count * 40 // max(letter_counts.values()))
    print(f'{letter} | {count:6d} | {bar}')