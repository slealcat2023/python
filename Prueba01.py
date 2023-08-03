print ("hola mundo de cevicuela")
print ("Soy Sergio Leal y estoy aprendiendo")
print ("Python")
print("")
print("")

numbers = [2,4, 6, 8]
product = 1

for number in numbers:
    product = product * number
    
print ("The product is: ", product)

print("")
print("") #Este es un comentario

vuelta = 1
while vuelta <= 10:
    #print("Vuelta "+str(vuelta))
    match vuelta:
        case 1:
            print("Sergio")
        case 2:
            print("Kike") 
        case 3:
            print("Marquitos")
        case other:
            print ("No match")

    vuelta = vuelta + 1


          
