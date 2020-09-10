
def main():
    print("Digite Palabra/frase ")
    a=input("Palabra: ")
    isPalindroma(a)



def isPalindroma(palabra):

    tamaño=len(palabra)
    print(tamaño)
    y=palabra.lower()
    z=y.replace(" ", "")
    w=palabra.replace(" ", "")
    zz=w.lower()


    if  zz==z[::-1]:
        print("Es palidroma")
    else:
        print("No es palidroma")
        print(palabra.replace(" ", ""))
        print(z[::-1])




if __name__ == '__main__':
        main()