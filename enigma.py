# '''
#     Энигма v0.3
#     Реализуйте функцию enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3) с поворачивающимися и двигающимися роторами, как они описаны на предыдущем шаге.
#
#     text - исходный текст, который необходимо зашифровать
#     ref - номер отражателя (согласно задаче https://stepik.org/lesson/283487/step/3)
#     rot1, rot2, rot3 - номера роторов (согласно задаче https://stepik.org/lesson/283487/step/2)
#     shift1, shift2, shift3 - сдвиги роторов (1, 2 и 3, соответственно)
#     Не забывайте, что правый ротор смещается на 1 ДО того как начнёт кодироватсья каждый новый символ. А так же, что в определённых ситуациях Роторы сдвигают соседей слева от себя.
# '''
# def rotor(symbol, n, reverse=False):
#     rtrs = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#             1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
#             2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
#             3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
#             4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
#             5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
#             6: 'JPGVOUMFYQBENHZRDKASXLICTW',
#             7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
#             8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
#             'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
#             'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
#             }
#     ans = str()
#     for i in symbol.upper():
#         w = rtrs[0]
#         v = rtrs[n]
#         if reverse == False:
#             if i in w:
#                 ans += v[w.find(i)]
#         else:
#             if i in v:
#                 ans += w[v.find(i)]
#
#     return ans
#
#
# def reflector(symbol, n):
#     rtrs = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#             1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
#             2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
#             3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
#             4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
#             }
#     ans = str()
#     for i in symbol.upper():
#         w = rtrs[0]
#         v = rtrs[n]
#         if i in w:
#             ans += v[w.find(i)]
#     return ans
#
#
# def caesar(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     cri_alpha = {}
#     l = len(alphabet)
#     encripted = []
#     key %= l
#     if key != 0 and key / abs(key) == -1:  # проверяю ключ-сдвиг на отрицательное значение
#         key = l + key
#     for i in range(l - key):
#         cri_alpha[alphabet[i]] = alphabet[i + key]
#     for i in range(key):
#         cri_alpha[alphabet[l - key + i]] = alphabet[i]
#     for item in text.upper():
#         if item in cri_alpha:
#             encripted.append(cri_alpha[item])
#
#     return ("".join(encripted)).upper()
#
#
#
#
# def enigma(text, ref, rot1=0, shift1=0, rot2=0, shift2=0, rot3=0, shift3=0):
#     text = [i for i in text.upper() if i != ' ']
#     text = "".join(text)
#     rot = (rot3, rot2, rot1, ref, rot1, rot2, rot3)
#     sh = (shift3, shift2, shift1, 0, shift1, shift2, shift3)
#     z = 1 % 26
#     z2 = 0%26
#     z3 = 0%26
#     ans = str()
#
#     for i in text:
#         sh = ((shift3 + z)%26, (shift2 + z2)%26, (shift1 + z3)%26, 0, (shift1 + z3)%26,(shift2 + z2)%26,
#             (shift3 + z)%26)
#
#         p = 0
#         if rot[0] == 1 and sh[0] == 16:
#             z2 += 1
#             if rot[1] == 1 and sh[1] == 16 or sh[1] == 17:
#                 z3 += 1
#             if rot[1] == 2 and sh[1] == 4 or sh[0] == 5:
#                 z3 += 1
#             if rot[1] == 3 and sh[1] == 21 or sh[1] == 22:
#                 z3 += 1
#
#         if rot[0] == 2 and sh[0] == 4 :
#             z2 += 1
#             if rot[1] == 1 and sh[1] == 16 or sh[1] == 17:
#                 z3 += 1
#             if rot[1] == 2 and sh[1] == 4 or sh[1]==5:
#                 z3 += 1
#             if rot[1] == 3 and sh[1] == 21 or sh[1] == 22:
#
#                 z3 += 1
#         if rot[0] == 2 and sh[0] == 5:
#             z2 += 1
#             if rot[1] == 1 and sh[1] == 16 or sh[1] == 17:
#                 z3 += 1
#             if rot[1] == 2 and sh[1] == 4 :
#                 z3 += 1
#             if rot[1] == 3 and sh[1] == 21 or sh[1] == 22:
#                 z3 += 1
#
#
#         if rot[0] == 3 and sh[0] == 21 :
#             z2 += 1
#             if rot[1] == 1 and sh[1] == 16 or sh[1] == 17:
#                 z3 += 1
#             if rot[1] == 2 and sh[1] == 4 or sh[1] == 5:
#                 z3 += 1
#             if rot[1] == 3 and sh[1] == 21 or sh[1] == 22:
#                 z3 += 1
#
#
#
#
#
#         if rot[0] == 1 and sh[0] == 17:
#             z2 += 1
#             if rot[1] == 1 and sh[1] == 16 or sh[1] == 17:
#                 z3 += 1
#             if rot[1] == 2 and sh[1] == 4 or sh[0] == 5:
#                 z3 += 1
#             if rot[1] == 3 and sh[1] == 21 or sh[1] == 22:
#                 z3 += 1
#
#
#
#         if rot[0] == 3 and sh[0] == 22:
#             z2 += 1
#             if rot[1] == 1 and sh[1] == 16 or sh[1] == 17:
#                 z3 += 1
#             if rot[1] == 2 and sh[1] == 4 or sh[1] == 5:
#                 z3 += 1
#             if rot[1] == 3 and sh[1] == 21 or sh[1] == 22:
#                 z3 += 1
#
#
#         for y in rot:
#             if p < 3:
#                 if sh[p] != 0:
#                     i = caesar(i, sh[p])
#                 i = rotor(i, y)
#                 if sh[p] != 0:
#                     i = caesar(i, sh[p] * -1)
#                 p += 1
#             elif p == 3:
#                 p += 1
#                 i = reflector(i, y)
#             elif p > 3:
#                 if sh[p] != 0:
#                     i = caesar(i, sh[p])
#                 i = rotor(i, y, reverse=True)
#                 if sh[p] != 0:
#                     i = caesar(i, sh[p] * -1)
#                 p += 1
#         # print("sh--->",sh)
#         # print(ans)
#         # print("\n")
#         ans += i
#         z += 1
#
#     return ans
#
#
# #--------------------------------------------------
# '''
#      Функция Энигма v0.2(text, ref, rot1, shift1, rot2, shift2, rot3, shift3) с поворачивающимися роторами, как они описаны на предыдущем шаге.
#
#     text - исходный текст, который необходимо зашифровать
#     ref - номер отражателя (согласно задаче https://stepik.org/lesson/283487/step/3)
#     rot1, rot2, rot3 - номера роторов (согласно задаче https://stepik.org/lesson/283487/step/2)
#     shift1, shift2, shift3 - сдвиги роторов (1, 2 и 3, соответственно)
#
#
#     Первые тестовые сценарии соответствуют примерам 3-6 с предыдущего шага
#
#
#
#     P.S. Не забудьте, что вам надо реализовать (или взять из предыдущего урока) функцию для шифрования Цезаря, использующуюся в сдвигах.
# '''
# def rotor(symbol, n, reverse=False):
#     rtrs = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#             1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
#             2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
#             3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
#             4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
#             5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
#             6: 'JPGVOUMFYQBENHZRDKASXLICTW',
#             7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
#             8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
#             'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
#             'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
#             }
#     ans = str()
#     for i in symbol.upper():
#         w = rtrs[0]
#         v = rtrs[n]
#         if reverse == False:
#             if i in w:
#                 ans += v[w.find(i)]
#         else:
#             if i in v:
#                 ans += w[v.find(i)]
#
#     return ans
#
#
# def reflector(symbol, n):
#     rtrs = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#             1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
#             2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
#             3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
#             4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
#             }
#     ans = str()
#     for i in symbol.upper():
#         w = rtrs[0]
#         v = rtrs[n]
#         if i in w:
#             ans += v[w.find(i)]
#     return ans
#
#
# def caesar(text, key,alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     cri_alpha = {}
#     l = len(alphabet)
#     encripted = []
#     key%=l
#     if key!=0 and key / abs(key) == -1:  # проверяю ключ-сдвиг на отрицательное значение
#         key = l + key
#     for i in range(l - key):
#         cri_alpha[alphabet[i]] = alphabet[i + key]
#     for i in range(key):
#         cri_alpha[alphabet[l - key + i]] = alphabet[i]
#     for item in text.upper():
#         if item in cri_alpha:
#             encripted.append(cri_alpha[item])
#
#     return ("".join(encripted)).upper()
#
#
# def enigma(text, ref, rot1=0, shift1=0, rot2=0, shift2=0, rot3=0, shift3=0):
#     rot = (rot3, rot2, rot1, ref, rot1, rot2, rot3)
#     sh = (shift3,shift2,shift1,0,shift1,shift2,shift3)
#     ans = str()
#     for i in text.upper():
#         p = 0
#         for y in rot:
#             if p <3:
#                 if sh[p]!=0:
#                     i = caesar(i,sh[p])
#                 i = rotor(i, y)
#                 if sh[p] != 0:
#                     i = caesar(i,sh[p]*-1)
#                 p+=1
#             elif p == 3:
#                 p +=1
#                 i = reflector(i, y)
#             elif p >3:
#                 if sh[p] != 0:
#                     i =caesar(i,sh[p])
#                 i = rotor(i, y, reverse=True)
#                 if sh[p] != 0:
#                     i = caesar(i,sh[p]*-1)
#                 p+=1
#         ans += i
#     return ans
#
#
# #print(enigma('A ',1,1,1,2,2,3,1))
#
#
# #--------------------------------------------
# '''
#      Энигма  3 ротора и 1 отражатель.
#
#     Спецификации роторов и отражателем используются из предыдущих задач.
#
#     Смещения и движение роторов/отражателей отсутствуют. Фактически мы реализуем примеры 1 и 2 с предыдущего шага.
#
#     Для проверки алгоритма и одного из алфавитов можно использовать пример http://www.codesandciphers.org.uk/enigma/example1.htm
#
#
#
#     Реализуйте функцию enigma(text, ref, rot1, rot2, rot3), где:
#
#     text - исходный текст, который необходимо зашифровать
#     ref - номер отражателя (согласно задаче https://stepik.org/lesson/283487/step/3)
#     rot1, rot2, rot3 - номера роторов (согласно задаче https://stepik.org/lesson/283487/step/2)
#     Функция возвращает зашифрованный текст.
#
#     Сигнал распространяется по машине справа налево (и после отражения обратно)
# '''
#
# def rotor(symbol, n, reverse=False):
#     rtrs = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#             1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
#             2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
#             3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
#             4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
#             5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
#             6: 'JPGVOUMFYQBENHZRDKASXLICTW',
#             7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
#             8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
#             'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
#             'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
#             }
#     ans = str()
#     for i in symbol.upper():
#         w = rtrs[0]
#         v = rtrs[n]
#         if reverse == False:
#             if i in w:
#                 ans += v[w.find(i)]
#         else:
#             if i in v:
#                 ans += w[v.find(i)]
#
#     return ans
#
#
# def reflector(symbol, n):
#     rtrs = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#             1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
#             2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
#             3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
#             4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
#             }
#     ans = str()
#     for i in symbol.upper():
#         w = rtrs[0]
#         v = rtrs[n]
#         if i in w:
#             ans += v[w.find(i)]
#     return ans
#
#
# def enigma(text, ref=0, rot1=0, rot2=0, rot3=0):
#     rot = (rot3, rot2, rot1, ref, rot1, rot2, rot3)
#     ans = str()
#     for i in text.upper():
#         p = 0
#         for y in rot:
#
#             if p <3:
#                 p +=1
#                 i = rotor(i, y)
#             elif p == 3:
#                 p +=1
#                 i = reflector(i, y)
#             elif p >3:
#                 p += 1
#                 i = rotor(i, y, reverse=True)
#         ans += i
#     return ans
#
#
# #--------------------------------------------
# '''
#     Функция "отражатель". Пока для нас она аналогична ротору, за 2 исключениями:
#
#     Имеет только 1 направление
#     Отражатель с функцией шифрования всегда соединяет символы парами
#     Реализуйте 2 отражателя:
#
#     0 - без шифрования
#     1 - отражатель вида "B"
#     Спецификация на Отражатели (и таблица соответствия символов) - http://www.codesandciphers.org.uk/enigma/rotorspec.htm
#
#     Реализуйте функцию reflector(symbol, n):
#
#     symbol - символ, поступающий для шифрования
#     n - номер отражателя
# '''
# def reflector(symbol, n):
#     rtrs = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#            1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
#            2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
#            3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
#            4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
#            }
#     ans = str()
#     for i in symbol.upper():
#         w = rtrs[0]
#         v = rtrs[n]
#         if i in w:
#             ans += v[w.find(i)]
#     return ans
#
# #-----------------------------------------------------
# '''
#     Функция Ротора шифрования
#     Фактически это простая замена символа по словарю.
#
#    Учитывайте, что ротор имеет "прямое" и "обратное" направления.
#
#    Т.е. если сигнал идёт напрямую и символ "A" соответствует "E", то при обратном движении сигнала символу "E" будет соответствовать символ "А"
#
#    Реализуйте функцию с 4 роторами:
#
#    0 - "не шифрованный ротор" - возвращает всегда тот же символ, что и принимает (в любом направлении)
#    1-3 - роторы номер 1, 2 и 3 соответственно.
#    Спецификация на роторы (и таблица соответствия символов) - http://www.codesandciphers.org.uk/enigma/rotorspec.htm
#
#     ymbol - символ, поступающий для шифрования
#     n - номер ротора
#     reverse - признак обратного направления, если находится в значении True, это значит, что функцию надо использовать в обратном направлении. (по умолчанию False)
#
#     Возвращает строку с зашифрованным символом
# '''
# def rotor(symbol, n, reverse=False):
#     rtrs = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#               1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
#               2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
#               3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
#               4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
#               5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
#               6: 'JPGVOUMFYQBENHZRDKASXLICTW',
#               7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
#               8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
#               'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
#               'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
#               }
#     ans = str()
#     for i in symbol.upper():
#         w = rtrs[0]
#         v = rtrs[n]
#         if reverse == False:
#             if i in w:
#                 ans += v[w.find(i)]
#         else:
#             if i in v:
#                 ans += w[v.find(i)]
#
#
#     return ans
