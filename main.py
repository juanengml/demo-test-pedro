pessoas = homens = mulheres = 0
while True:
    print("=" * 20)
    print("CADASTRE UMA PESSOA")
    print("=" * 20)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    print("=" * 20)
    if idade >= 18:
        pessoas += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        print("Finalizado!!")
        break
print(f"Temos um total de {pessoas} pessoa(s) maior(es) de 18 anos!!")
print(f"Temos um total de {homens} Homens cadastrados no sistema!!")
print(f"Temos um total de {mulheres} Mulheres menores de 20 anos!!")