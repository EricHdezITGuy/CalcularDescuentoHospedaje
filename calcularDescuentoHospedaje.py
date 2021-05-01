dias=int(input("Ingrese el numero de dias de hospedaje"))
precioDia=int(input("Precio del dia"))
if dias >=5 and dias <= 10:
    porDescuento=0.10
elif dias >= 10:
    porDescuento=0.15
else:
    porDescuento=0
subTotal= precioDia*dias
descuento= subTotal*porDescuento
totalPagar= subTotal-descuento
print("El total es ", totalPagar)