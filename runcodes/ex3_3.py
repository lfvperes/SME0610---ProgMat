# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# entrada
c = float(input())

# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x1 = modelo.addVar(vtype="C", name="x_1", lb=0)
x2 = modelo.addVar(vtype="I", name="x_2", lb=0)
# funcao objetivo
modelo.setObjective((c**2)*x1 + c*x2, sense="minimize")
# restricoes
modelo.addCons(5*x1 + 1*x2 >= 100)
modelo.addCons(1*x1 - 1*x2 <= 15)
# resolver problema
modelo.optimize()
# mostrar resultado
if modelo.getStatus() == "unbounded":
    print("ILIMITADO")
else:
    print(round(modelo.getObjVal(), 2))
    print(round(modelo.getVal(x1), 2))
    print(modelo.getVal(x2))
