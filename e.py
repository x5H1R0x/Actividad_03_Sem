from os import system

def factorial(myN):
    myF = 1
    myL = 1
    while(myN >= myL):
        myF = myF * myL
        myL += 1
    return myF

def isNum(myNum):
    try:
        int(myNum)
        return True
    except ValueError:
        return False

def mainMenu():
    print("*****MENU*****")
    print("1.- Numero e.")
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
            limit = "s" 
            n = 0
            e = 0
            while(isNum(limit) == False or limit < 0):
                limit = int(input("Ingrese el limite: "))
                if(isNum(limit) == False or limit < 0):
                    errorNum()
    
            while(n < limit):
                e += 1 / factorial(n)
                n +=1
            print("El numero e: ", e)
            input("Presione Enter para continuar...\n")
        
        if num == "q" or num == "Q":
            print("Saliendo del sistema...")
            print("Hasta la proxima. ")
            
            exit()
        