print(2 + 2)
print(18 / 5)
print(18 // 5) #小数点以下切り捨て
print(17 % 5) #余り
print(5 ** 2) #5の2乗

print('dosen\'t') # \を使用してシングルフォート(')をエスケープする

s = 'First line. \nSecond line.' # \n で改行
print(s)

print('C:\some\name') # \n で改行
print(r'C:\some\name') # r(raw strings)を引用符の前につけることで \ の後の文字が特殊文字として解釈されなくなる

print("""\
aiueo           kakikukeko
      sasisuseso
      tachituteto
""") #三連引用符を使うことで文字列リテラルを複数行にまたがって記述可能

print(3 * 'un' + 'ium') # 文字列は+演算子で連結、*演算子で反復可能

print('連続して並んでいる複数の文字列リテラルは'
      '自動的に連結される') #変数や式には働かない
prefix = 'Py'
print(prefix + 'thon') #変数同士や変数とリテラルを連結させる場合は+を使用

# 文字の取得
word = "Python"
print(word[0]) #0番目
print(word[5]) #5番目
print(word[-2]) #後ろから2番目
print(word[-4]) #後ろから4番目
print(word[0:2]) #0番目(含む)~2番目(含まない)
print(word[:2]) #0番目(含む)~2番目(含まない)
print(word[4:]) #4番目(含む)~最後
print(word[-2:]) #後ろから2番目(含む)~最後
print(word[:2] + word[2:])

s = 'aaaaaaaaaaaaaaaaaaa'
print(len(s)) #文字列の長さ
