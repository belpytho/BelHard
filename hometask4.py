x=input('Введите первое число: ')
b=input('Введите операцию: ')
y=input('Введите второе число: ')
a=float(x)
c=float(y)
plus=a+c
minus=a-c
mult=a*c
div=a/c
list_results=[plus,minus,mult,div]
list_operation=['+','-','*','/']
index=list_operation.index(b)
result=list_results[index]
d='='
print("Результат: {}{}{}{}{}".format(a,b,c,d,result))