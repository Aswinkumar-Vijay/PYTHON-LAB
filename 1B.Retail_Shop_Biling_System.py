#1B.Retail_Shop_Biling_System.py
a=0
b=0
c=0
while True:
    item=input('Item:')
    quan=input('Quantity:')
    a=int(quan)
    price=input('Price:')
    b=int(price)
    c+=a*b
    next_item=input('Is there another item?')
    if next_item=='N':
        print('Total:',c)
        break
    if next_item!='Y':
        print('Please choose between Yes or No')
    print('Total:',c)
