# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# entrada
b = float(input())

# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x1 = modelo.addVar(vtype="C", name="x_1", lb=0)
x2 = modelo.addVar(vtype="I", name="x_2", lb=0)
# funcao objetivo
modelo.setObjective(x1 - x2, sense="minimize")
# restricoes
modelo.addCons(x1 + x2 <= b)
modelo.addCons(x1 <= 10)
modelo.addCons(x2 <= 10)
# resolver problema
modelo.optimize()
# mostrar resultado
if modelo.getStatus() == "unbounded":
    print("ILIMITADO")
else:
    print(round(modelo.getObjVal(), 2))
    print(round(modelo.getVal(x1), 2))
    print(modelo.getVal(x2))
