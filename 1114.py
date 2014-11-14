# -*- coding: utf-8 -*-

# can use Korean(unicode charset) for arguments

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pyExcelerator import *

SourceFilePath = './'
SourceFileName = 'data3.xls'

encoding='utf-8' if sys.stdin.encoding in (None, 'ascii') else sys.stdin.encoding

w = Workbook()
ws = w.add_sheet('Copied Cell')

def bubbleSort(a):
    for i in range(0, len(a)-1):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                swap = a[j]
                a[j]=a[j-1]
                a[j-1]=swap
    return a;

print "What do you want to search?",  " 1. ", '서명', " 2. ", '저자', " 3. ", '출판사', " 4. ", '출판년',  " 5. ", '비고'

label = int(raw_input()).decode(encoding)

row = 0
col = 0
input_row = 0
input_col = 0
yes = 0
year = []
remark = []

if (label==1):
	col = 0
elif (label==2):
	col = 1
elif (label==3):
	col = 2
elif (label==4):
	col = 3
	for sheet_name, values in parse_xls(SourceFilePath+SourceFileName, 'utf-8'):
		for row_idx, col_idx in sorted(values.keys()):
			v = values[(row_idx, col_idx)]
			if (type(v) is unicode):
				tmp = str(v)
				if row_idx != 0 and col_idx == 3:
					for i in year:
						if str(v) == str(i):
							yes = 1
					if yes == 0:
						year.append(str(v))
				yes = 0
elif (label==5):
	col = 4
	for sheet_name, values in parse_xls(SourceFilePath+SourceFileName, 'utf-8'):
		for row_idx, col_idx in sorted(values.keys()):
			v = values[(row_idx, col_idx)]
			if (type(v) is unicode):
				tmp = str(v)
				if row_idx != 0 and col_idx == 4:
					for i in remark:
						if str(v) == str(i):
							yes = 1
					if yes == 0:
						remark.append(tmp)
				yes = 0

if label == 1 or label == 2 or label == 3:
	print "input word for searching"
elif label == 4:
	print "input year for searching"
	print "possible searching year showing under the line:"
	print bubbleSort(year)
elif label == 5:
	print "input word which showed under the line:"
	for word in remark:
		print unicode(word)

s = str(raw_input()).decode(encoding)


for sheet_name, values in parse_xls(SourceFilePath+SourceFileName, 'utf-8'):
    for row_idx, col_idx in sorted(values.keys()):
        v = values[(row_idx, col_idx)]
        if (type(v) is unicode):
            tmp = str(v)
            if col == col_idx:
            	if tmp.find(s) >= 0:
					ws.write(input_row, 0, values[(row_idx, 0)])
					ws.write(input_row, 1, values[(row_idx, 1)])
					ws.write(input_row, 2, values[(row_idx, 2)])
					ws.write(input_row, 3, values[(row_idx, 3)])
					ws.write(input_row, 4, values[(row_idx, 4)])
					input_row = input_row + 1


w.save('savedata.xls')