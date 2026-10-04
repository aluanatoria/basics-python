def paridade(num : int):
    if num%2==0:
        return "par"
    else:
        return "impar"

while True:
    num = int(input("Digite um número: "))
    print(paridade(num))
    print("Deseja verificar a paridade de outro número? ")
    loop = input("1- Sim | 2- Não: ")

    if loop == "2":
        break