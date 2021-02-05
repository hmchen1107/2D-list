#記帳程式
stocks = []
while True :
    name = input("PLS input what your stock name is : ")
    if name == 'q' :
        break
    price = input('PLS input what your stock price when you bought : ')
    p = []
    p.append(name)
    p.append(price)
#   p = [name, price] 上兩行也可以寫成這樣
    stocks.append(p)
print(stocks)

for p in stocks:
    print(p[0], "的價格是", p[1])

with open('stock.csv','w') as f :
    for p in stocks :
        f.write(p[0]+","+p[1]+'\n')
