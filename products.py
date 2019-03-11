import os
def readfile(filename): # 讀取檔案
	products = []
	#讀取檔案
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
	return (products)
	

def userinput(products): #輸入
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = int(input('請輸入此商品金額:'))
		products.append([name, price])
	print(products)
	return(products)

def printpro(products): #印出
	for p in products:
		print(p[0] + '的價格是' + str(p[1]))

def writefile(filename, products): #寫入
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #相對路徑/絕對路徑
		print('有找到檔案')
		products = readfile(filename)
	else:
		print('無清單檔案')

	products = userinput(products)
	printpro(products)
	writefile('products.csv', products)

main()