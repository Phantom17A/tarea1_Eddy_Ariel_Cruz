# ejercicio con try y except
#ejercicio 3.11_2


horas_trabajadas = (input("Introdusca las horas trabajadas: "))
tarifa_hora = (input("Introdusca la tarifa por hora: "))

try:

    if horas_trabajadas>40:
        salario_base = 40 * tarifa_hora 
        horas_extra = horas_trabajadas - 40
        salario_extra = horas_extra * (tarifa_hora * 1.5)
        salario_total = salario_base + salario_extra
     
    else:
        salario_total = horas_trabajadas * tarifa_hora
    
      
    print("salario", salario_total)    

except:
    print("Error, por favor introdusca un numero")    