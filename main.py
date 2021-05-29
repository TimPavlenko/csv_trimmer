import csv
import pandas as pd
import numpy
import os
from os import listdir
import shutil
from numpy import genfromtxt

new_file = "file0" #без первых 6и строк и 2х столбцов
new_files_index = 0 # глобальный счетчик для называния выходных файлов
new_file2 = 'tempfile0'
new_files_index2 = 0
tempfiles = [] # список файлов в директории temple_files

def toutf8(X,nc): # X = файл которому мы меняем кодировку; nc = название кодировки файла X
  data = []
  with open(X, 'r', encoding=nc, newline='') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
  # write
  with open('tempfile.csv', 'w+', encoding = 'utf-8', newline='') as f:
    writer = csv.writer(f)
    for i in range(int(len(data))):
        writer.writerow(data[i])
    
  
# удаляем первые 6 строк и 2 столбца, не нужные нам в новом файле
def nf(X, Y): # X = old file ; Y = new file
  in_file = open(X, "r")
  out_file = open(Y, "w", newline="")
  in_csv = csv.reader(in_file)
  out_csv = csv.writer(out_file)
  for row_number, row in enumerate(in_csv):
    if row_number >= 6:
        out_csv.writerow(row[:2])
  in_file.close()
  out_file.close()

  
# кастыль, удаляет лишние два столбца(КоТоРыЕ ПоЧеМуТо Не УдАлЯюТсЯ в функции nf):
def nffix(X, I): # X = путь к файлу который надо обработать; I = индкс для имени выходного файла
  # порядковые номера столбцов, которые нужно удалить (нумерация столбцов начинается с 0)
  cols2drop = [0,1]
  name = 'temp_files/res' + str(I) +'.csv'
  # список столбцов, которые нужно прочитать    
  cols = [i for i in range(6) if i not in cols2drop]
  # чтение нужных столбцов и запись в CSV
  (pd.read_csv(X, usecols=cols, delim_whitespace=True)
     .to_csv(name, index=False, sep=','))
    #.to_csv(r'/temp_files/result.csv', index=False, sep=','))

def expo(X):
  arr = numpy.loadtxt(X, delimiter=',')
  num = arr[0,3]
  #print(num)
  if(row_count > row_count):
    print ("{:.16f}".format(float("1.70000043572e-05")))
  x = float(arr[0,3])
  print ("%.2f" % (x))

def test(X):
  with open(X, newline='') as f:
    reader = csv.reader(f)
    row1 = next(reader)  # gets the first line
    print('>')
    rr = []
    for value in row1:
      value.strip()
      value = str(value)
      value.lower()
      print(value)
      rr.append(value)
      for i in rr:
        i.strip()
    print(rr)
    print('<')
    # now do something here 
    # if first row is the header, then you can do one more next() to get the next row:
    row2 = next(f)
    print(row1)
    print(row2)
  
def expo2():
  df=pd.read_csv('output/file0.csv', sep=',',header=None)
  print(df)

#--------------
print(' ')
print('beginning...')
print(' ')
files = next(os.walk("input"))
file_count = len(files)
if(file_count == 0):
    print('папка input пуста!')
files_csv = []
files = listdir("input")
for filename in files:
  if('csv' in filename):
    files_csv.append(filename)
#print(files_csv)
for fl in files_csv:
  nc = 'utf-16'
  p = "input/" + fl
  toutf8(p,nc)
  p = 'temp_files/' + new_file2 + '.csv'
  shutil.move('tempfile.csv', p)
  u = new_file2 + '.csv'
  tempfiles.append(u)
  new_files_index2 += 1
  new_file2 = 'tempfile' + str(new_files_index2)
  
numfiles = len(tempfiles)
nm = 0

for wd in tempfiles:
  o = "temp_files/" + wd
  outway = "output/" + new_file + '.csv'
  shutil.move(o, 'temp_files/t1.csv')
  nf('temp_files/t1.csv','t2.csv')
  nm += 1
  print(str(nm) + '/' + str(numfiles) + '   complited')
  with open('t2.csv', 'r') as f:
    lines = f.readlines()
    lines = lines[:-1]
  with open('t2.csv', 'w') as f:
    f.writelines(lines)
  shutil.move('t2.csv',outway)
  nffix(outway, new_files_index)
  new_files_index += 1
  new_file = "file" + str(new_files_index)


#test(outway) # debug функция
print(' ')
print("DONE")
