from os import system

zodiacSign = ["Capricornio", "Acuario", "Picis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
days = [21, 20, 19, 20, 20, 20, 21, 21, 22, 22, 22, 22]       # Comenzamos por capicornio, es decir, Mes de diciembre

def isNum(myNum):
    try:
        int(myNum)
        return True
    except ValueError:
        return False

def mainMenu():
    print("*****MENU*****")
    print("1.- Calcular Signo.")
    print("q.- Salir")

def errorNum():
    print("No se detecta numero valido.")
    print("Intente de nuevo.")
    input("Presione Enter para continuar...")

def getSign(myM, myD):
    if myM == 12:
        myM = 0    
    if myD <= days[myM]:
        myM -= 1
        mySign = zodiacSign[myM]
    else:
        mySign = zodiacSign[myM]
    print("Tu signo zodiacal es: ", mySign)

if __name__ == "__main__":

    while(True):
        system("cls")
        mainMenu()
        num = input("\tEleccion: ") 
        if num == "1":
            myNum = "s" 
            while(isNum(myNum) == False):
                myNum = input("Mes de Nacimiento: ")
                if(isNum(myNum) == False):
                    errorNum()
        
            myMonth = myNum
            myNum = "s"
            while(isNum(myNum) == False):
                myNum = input("Dia de Nacimiento: ")
                if(isNum(myNum) == False):
                    errorNum()
            myDay = myNum
            getSign(int(myMonth),int(myDay))
            input("Presione Enter para continuar...\n")
        
        if num == "q" or num == "Q":
            print("Saliendo del sistema...")
            print("Hasta la proxima. ")
            
            exit()