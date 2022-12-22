def criaConta(titular, numero, saldo, limite):
    conta = {"titular": titular, "numero": numero,
             "saldo": saldo, "limite": limite}
    return conta


conta = criaConta(123, "Nico", 50, 100)


def depositar(conta, valor):
    conta["saldo"] += valor


def sacar(conta, valor):
    conta["saldo"] = conta["saldo"] - valor


def extrato(conta):
    print("saldo é {}".format(conta["saldo"]))


depositar(conta, 100)
print(sacar(conta, 100))
print(extrato(conta))
