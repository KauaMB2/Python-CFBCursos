r = lambda x, func:x + func(x)
res = r(3, lambda x:x*x)
print(res)
res = r(3, lambda x:x+x)
print(res)