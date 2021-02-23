#記帳程式
stocks = []
while True :
    name = input("Please input what your stock name is : ")
    if name == 'q' :
        break
    amount = input('Please input hom many stock you bought : ')
    price = input('Please input what is your stock price when you brought it : ')
    p = []
    p.append(name)
    p.append(amount)
    p.append(price)
#   p = [name, price] 上兩行也可以寫成這樣
    stocks.append(p)
print(stocks)

for p in stocks:
    print(p[0],"共買", p[1], "張而一張為", p[2], "元")
    
with open('stock.csv','w') as f :
    f.write('股票,買進數量,買進價格\n')
    for p in stocks :
        f.write(p[0]+","+p[1]+","+p[2]+'\n')


