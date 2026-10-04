# Este programa calcula o número de dias até o próximo aniversário, ou emite uma mensagem de parabéns, caso seja seu aniversário
from datetime import date

diaAtual = date.today().day
meseAtual = date.today().month
anoAtual = date.today().year

nasc = input("Digite a data do seu nascimento: ")
vetor_nasc = nasc.split("-") #supondo que o aniversário seja dado em formato de string 12-12-2000

diaNasc = int(vetor_nasc[0])
meseNasc = int(vetor_nasc[1])
anoNasc = int(vetor_nasc[2])

aniversario = date(anoAtual, meseNasc, diaNasc)
idade = anoAtual - anoNasc

if diaNasc == diaAtual and meseNasc == meseAtual:
    print(f"Hoje é seu aniversário de {idade} anos! Parabénsssss")
else:
    if aniversario < date.today():
        aniversario = date(anoAtual+1, meseNasc, diaNasc)
        idade +=1

    diasFaltantes = (aniversario - date.today()).days
    print(f"Faltam {diasFaltantes} dias para o seu aniversário de {idade} anos!")

