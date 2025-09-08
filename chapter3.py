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




