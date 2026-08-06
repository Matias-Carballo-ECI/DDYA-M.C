def prueba():

    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
    num = float(input("\nPor favor ingresa un numero: "))
    
    if num > 0:
        print("\nEl numero",num,"es positivo.")

        if num in fibonacci:
            print("\nEl numero",num,"pertenece a la secuencia de Fibonacci.")
        
        
    elif num < 0:
        print("\nEl numero",num," es negativo.")
        
        
    else:
        print("\nEl numero",num,"es cero y pertenece a la secuencia de Fibonacci.")
        

# El tercer punto de los primos no tengo muy claro como hacerlo, el profesor me dijo que podia usar la funcion modulo %, lo que haria es usar ese residuo que da el modulo y compararlo con los residuos de otros numeros. 

#El cuarto punto tampoco tengo claro como hacerlo, pediria los dos nuemros, pero no sabria de que forma sumar los intermedios, tal vez metiendo los numeros a una lista y averiguar cual es mayor o menor, o si son iguales, y ya con esaa informacioon averiguar los numeros intermedios. Lo mismoo coon el punto 5.

    if num %2 == 0:
        result = num ** 3
        print("\nEl numero",num,"es par, elevado al cubo es:",result)
        
    else:
        result = num ** 2
        
        print("\nEl numero",num,"es impar, elevado al cuadrado es:",result)
        
#Para el punto 7, cuando se solicite el numero se debe coolocar : 1000113707

#No termino de coomprender el punto 8, lo que intentaria es poner un input para meter la fecha de nacimiento y juntarlo con el coodigo estudiantil, para despues filtrarlo y obtener el resultado deseado

#Para el punto 9 usaria dos listas, uno que contenga las vocales y otra las consonantes, y recorreria cada letra del mes para averigur consonanntes y vocales, despues imprimiria los resultados.

#Para el punto 10 recorreria cada letra del mes y la meteria en una lista, despues averiguaria su pocision con base a la lista.         
        
prueba()
