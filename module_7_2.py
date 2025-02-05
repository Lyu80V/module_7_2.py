info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    strings_positions = {}
    number = 1
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        strings_positions[(number,file.tell())] = i
        file.write(i + '\n')
        number += 1
    file.close()
    return strings_positions





result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)