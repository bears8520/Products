products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入此商品金額:')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

for p in products:
	print(p[0] + '的價格是' + p[1])