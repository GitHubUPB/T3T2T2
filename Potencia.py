def a_power_b (a,b):
    prod=1
    for A in range (1,b):
        prod=prod*b
    return prod


while True:
    
    bas=int(input("ingrese Valor Para La Base"))
    if bas ==0:
        print("El Valor Es Cero")
        break
    exp=int(input("Ingrese Valor Para La Exponente"))
    result=a_power_b(bas,exp)
    print("El Resultado Es: ",result)
    if bas ==0:
        break

