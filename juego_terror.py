print ("====================================================")
print ("======Bienvenido al juego de terror de python=======")
print ("====================================================")

print ("En este juego, te encontrarás en una casa embrujada y tendrás que tomar decisiones para sobrevivir.")
print ("pero ten cuidado, cada decisión que tomes tendrá consecuencias diferentes.")
print ("asi que piensa bien antes de elegir tu camino.")
print ("pero antes de comenzar, ¿Cuál es tu nombre y edad? ")

nombre_usuario = str(input ("Ingrese su nombre: "))
edad_usuario = int(input ("Ingrese su edad: "))

if edad_usuario <= 17 or edad_usuario >= 50:
    print ("Lo siento, este juego es para personas entre 18 y 49 años.")
    print ("Gracias por tu interés, " + nombre_usuario + ". ¡Hasta la próxima!")

elif edad_usuario >= 18 and edad_usuario <= 49:
    print ("¡Bienvenido al juego, " + nombre_usuario + "! ¡Prepárate para una aventura aterradora!")
    print ("Te encuentras en la entrada de una casa embrujada. ¿Qué quieres hacer?")
    print ("1. Entrar a la casa")
    print ("2. Salir corriendo")
    print ("3. Quedarte afuera y observar la casa")
    opcion = int(input("Ingrese el número de su elección (1-2): "))

    if opcion == 1:
        print ("Has entrado a la casa y te encuentras con un pasillo oscuro. ¿Qué quieres hacer?")
        print ("1. Ir hacia la izquierda")
        print ("2. Ir hacia la derecha")
        print ("3. Ir hacia adelante")
        opcion2= int(input("Ingrese el número de su elección (1-3): "))

        if opcion2 == 1:
            print ("Has ido hacia la izquierda y te encuentras con una habitación llena de telarañas. ¿Qué quieres hacer?")
            print ("1. Explorar la habitación")
            print ("2. buscar una salida")
            print ("3. Quedarte en la habitación y esperar a que algo suceda")
            opcion3 = int(input("Ingrese el número de su elección (1-3): "))

            if opcion3 == 1:
                print ("Mientras exploras la habitación, encuentras un objeto misterioso que te da poderes especiales para enfrentar a los fantasmas. ¡Felicidades, has ganado el juego!")
            elif opcion3 == 2:
                print ("Mientras buscas una salida, te encuentras con un fantasma que te asusta tanto que pierdes el juego. ¡Game Over!")
            elif opcion3 == 3:
                print ("Mientras esperas en la habitación, un fantasma aparece y te asusta tanto que pierdes el juego. ¡Game Over!")

    elif opcion == 2:
        print ("Has salido corriendo de la casa, pero te encuentras con un grupo de fantasmas que te persiguen. ¿Qué quieres hacer?")
        print ("1. Esconderte detrás de un árbol")
        print ("2. Correr más rápido")
        print ("3. Enfrentar a los fantasmas")
        opcion4 = int(input("Ingrese el número de su elección (1-3): "))

        if opcion4 == 1:
            print ("Te escondes detrás de un árbol, pero los fantasmas te encuentran y te asustan tanto que pierdes el juego. ¡Game Over!")
        elif opcion4 == 2:
            print ("Corres más rápido, pero los fantasmas te alcanzan y te asustan tanto que pierdes el juego. ¡Game Over!")
        elif opcion4 == 3:
            print ("Enfrentas a los fantasmas con valentía y logras asustarlos tanto que huyen de ti. ¡Felicidades, has ganado el juego!")

    elif opcion == 3:
        print ("Decides quedarte afuera y observar la casa, pero te encuentras con un objeto misterioso ¿Qué quieres hacer?")
        print ("1. Acercarte al objeto")
        print ("2. Ignorar el objeto y seguir observando")
        print ("3. Salir de la zona")
        opcion5 = int(input("Ingrese el número de su elección (1-3): "))

        if opcion5 == 1:
            print ("Te acercas al objeto y descubres que es un tesoro oculto. ¡Felicidades, has ganado el juego!")
        elif opcion5 == 2:
            print ("Ignoras el objeto y continúas observando, pero de repente un fantasma aparece y te asusta tanto que pierdes el juego. ¡Game Over!")
        elif opcion5 == 3:
            print ("Sales de la zona y te terminas encontrando con un policia al que le cuentas lo sucedido pero el policia no habla y esta quieto ¿Qué quieres hacer?")
            print ("1. Hablar con el policia")
            print ("2. Ignorar al policia y seguir caminando")
            print ("3. Enfrentar al policia")
            opcion6 = int(input("Ingrese el número de su elección (1-3): "))


            if opcion6 == 1:
                print ("Hablas con el policia, pero de repente el policia se transforma en un fantasma y te asusta tanto que pierdes el juego. ¡Game Over!")
            elif opcion6 == 2:
                print ("Ignoras al policia y sigues caminando, pero de repente un fantasma aparece y te asusta tanto que pierdes el juego. ¡Game Over!")
            elif opcion6 == 3:
                print ("Enfrentas al policia con valentía y logras asustarlo tanto que huyen de ti. ¡Felicidades, has ganado el juego!")
            
            else:
                print ("Opción no válida. Por favor, ingrese una opción del 1 al 3.")

        else: 
            print ("Opción no válida. Por favor, ingrese una opción del 1 al 3.")

    else: 
        print ("Opción no válida. Por favor, ingrese una opción del 1 al 3.")
        
else:    print ("Opción no válida. Por favor, ingrese una edad entre 18 y 49 años.")
 



    
    












    




