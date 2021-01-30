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
