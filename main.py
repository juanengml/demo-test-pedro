from console_logging.console import Console
console = Console()

console.log("APP iniciando...")

total = totalmil = menor = produtos = 0
barato = ""
while True:
    produto = str(input("Produto: ")).strip()
    valor = float(input("Valor: R$"))
    produtos += 1
    total += valor
    if valor > 1000:
        totalmil += 1
    if produtos == 1 or valor < menor:
        menor = valor
        barato = produto
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        print("{:-^40}".format("FIM DO PROGRAMA"))
        break
console.info(f"O total gasto na compra foi de R${total:.2f}")
console.info(f"O total de produtos acima de R$1000.00 é de: {totalmil}")
console.info(f"O produto mais barato é o/a {barato} que custa R${menor:.2f}")

console.success("DONE ! ")