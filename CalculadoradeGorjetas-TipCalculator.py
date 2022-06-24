print("Essa é a calculadora de gorjetas, seja bem vindo.")

bill = float(input("Qual foi o valor da conta? $"))
tip = int(input("Qual porcentagem de gorjeta você gostaria de dar? (Só coloque o número): "))
split = int(input("Quantas pessoas vão dividir a conta? "))

pay = tip / 100 * bill
pay = (pay + bill) / split

billPay = round(pay, 2)
billPay = "{:.2f}".format(pay)
print(f"Cada pessoa deve pagar: ${billPay}.")