from os import system
import math

def squareArea(s_height):
    mySquare =  (s_height) * (s_height)
    print("El area es:", mySquare)

def circleArea(c_r):
    myCircle =  (c_r) * (c_r)*math.pi
    print("El area es:", myCircle)

def triangleArea(s_width, s_height):
    myTriangle =  (s_width * s_height)/2 
    print("El area es:", myTriangle)

def isNum(myNum):
    try:
        int(myNum)
        return True
    except ValueError:
        return False

def mainMenu():
    print("*****MENU*****")
    print("1.- Area de cuadro.")
    print("2.- Area de circulo")
    print("3.- Area de triangulo.")
    print("q.- Salir")

def errorNum():
    print("No se detecta numero valido.")
    print("Intente de nuevo.")
    input("Presione Enter para continuar...")

if __name__ == "__main__":

    while(True):
        system("cls")
        mainMenu()
        num = input("\tEleccion: ") 
        if num == "1":
            myNum = "s" 
            while(isNum(myNum) == False):
                myNum = float(input("Altura del cuadrado: "))
                if(isNum(myNum) == False):
                    errorNum()
            squareArea(myNum)
            input("Presione Enter para continuar...\n")
            
        if num == "2":
           
            myNum = "s" 
            while(isNum(myNum) == False):
                myNum = float(input("Radio del circulo: "))
                if(isNum(myNum) == False):
                    errorNum()
            circleArea(myNum)
            input("Presione Enter para continuar...\n")

        if num == "3":
            myH = "s"
            myW = "s"
            while(isNum(myW) == False):
                myW = float(input("Base del triangulo: "))
                if(isNum(myW) == False):
                    errorNum()
        
            while(isNum(myH) == False):
                myH = float(input("Altura del triangulo: "))
                if(isNum(myH) == False):
                    errorNum()

            triangleArea(myW, myH)
            input("Presione Enter para continuar...\n")
        
        if num == "q" or num == "Q":
            print("Saliendo del sistema...")
            print("Hasta la proxima. ")
            
            exit()
        