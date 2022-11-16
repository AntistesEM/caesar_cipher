print('Добро пожаловать в программу для шифрования текста')
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def step_word_length(text, lower_alphabet, upper_alphabet, len_alphabet, action):
    text_crypt = []
    for k in text.split():           
        crypt = []
        step = 0
        for i in k:   
            if i.lower() in lower_alphabet:
                step += 1
        if action == 'шифровать':
            for i in k:
                if i in lower_alphabet:  
                    crypt += lower_alphabet[(lower_alphabet.find(i) + step) \
                            % len_alphabet]
                elif i in upper_alphabet: 
                    crypt += upper_alphabet[(upper_alphabet.find(i) + step) \
                            % len_alphabet]
                else: crypt += i
            text_crypt.append(''.join(crypt))
        elif action == 'расшифровывать':            
            for i in k:
                if i in lower_alphabet:  
                    crypt += lower_alphabet[(lower_alphabet.find(i) - step) \
                            % len_alphabet]
                elif i in upper_alphabet: 
                    crypt += upper_alphabet[(upper_alphabet.find(i) - step) \
                            % len_alphabet]
                else: crypt += i
            text_crypt.append(''.join(crypt))
    return ' '.join(text_crypt)    

def decryption_no_step(text, lower_alphabet, upper_alphabet, len_alphabet): 
    result_list = {}
    for j in range(len_alphabet):
        text_crypt = ''
        for i in text:    
            if i in lower_alphabet:     
                text_crypt += lower_alphabet[(lower_alphabet.find(i) - j) \
                        % len_alphabet]
            elif i in upper_alphabet: 
                text_crypt += upper_alphabet[(upper_alphabet.find(i) - j) \
                        % len_alphabet]
            else: text_crypt += i
        result_list[j] = result_list. setdefault(j, text_crypt)
    return '\n'.join("{}: {}".format(k, v) for k, v in result_list.items())

def en_decryption(text, lower_alphabet, upper_alphabet, step, len_alphabet):   
    text_crypt = ''
    for i in text:    
        if i in lower_alphabet:     
            text_crypt += lower_alphabet[(lower_alphabet.find(i) + step) \
                    % len_alphabet]
        elif i in upper_alphabet: 
            text_crypt += upper_alphabet[(upper_alphabet.find(i) + step) \
                    % len_alphabet]
        else: text_crypt += i
    return text_crypt

text = input('Введите текст для обработки: ')
action = input('Что будем делать: шифровать, расшифровывать или \
дешифрововывать? ').lower()
while True:  
    if action in ('шифровать', 'расшифровывать'):
        step = input('Укажите шаг сдвига(целое число или "l" - длина каждого слова: ')
        if step.isdigit():            
            if action == 'шифровать':
                step = step
                break
            elif action == 'расшифровывать':
                step = -1 * int(step)
                break
        elif step in ('длина слова', 'l'):
            break
        else:
            print('Введен неверный шаг! Побробуйте еще раз. ')
    elif action == 'дешифрововывать':
        break        
    else:
        action = input('Введена неверная операция! Побробуйте еще раз: ')
language = input('Какой язык будем использовать: английский или русский? \
(en/ru): ').lower()
while True:
    if language == 'en':
        if action in ('шифровать', 'расшифровывать'):
            if step in ('длина слова', 'l'):
                print('Ваш текст: ', step_word_length(text, eng_lower_alphabet, \
                        eng_upper_alphabet, 26, action), 'До новых встреч!', sep='\n')
                break                 
            else:
                print('Ваш текст: ', en_decryption(text, eng_lower_alphabet, \
                        eng_upper_alphabet, int(step), 26), 'До новых встреч!', \
                        sep='\n')
                break 
        elif action == 'дешифрововывать':
            print('Ваш текст: ', decryption_no_step(text, eng_lower_alphabet,\
                    eng_upper_alphabet, 26), 'До новых встреч!', sep='\n')
            break
    elif language == 'ru':
        if action in ('шифровать', 'расшифровывать'):
            if step in ('длина слова', 'l'):
                print('Ваш текст: ', step_word_length(text, rus_lower_alphabet, \
                        rus_upper_alphabet, 26), 'До новых встреч!', sep='\n')
                break                 
            else:
                print('Ваш текст: ', en_decryption(text, rus_lower_alphabet, \
                        rus_upper_alphabet, int(step), 32), 'До новых встреч!', \
                        sep='\n')
                break 
        elif action == 'дешифрововывать':        
            print('Ваш текст: ', decryption_no_step(text, rus_lower_alphabet, \
                    rus_upper_alphabet, 32), 'До новых встреч!', sep='\n')
            break
    else:
        language = input('Введен неверный язык! Побробуйте еще раз: ')