# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# entrada
arr = input()
a = list(map(float, arr.split(' ')))


# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x1 = modelo.addVar(vtype="C", name="x_1", lb=0)
x2 = modelo.addVar(vtype="C", name="x_2", lb=0)
x3 = modelo.addVar(vtype="I", name="x_3", lb=0)
# funcao objetivo
modelo.setObjective(1.1*x1 + 1.2*x2 + 1.3*x3, sense="maximize")
# restricoes
modelo.addCons(a[0]*x1 + a[1]*x2 + a[2]*x3 <= 12)
modelo.addCons(x1 <= 10)
modelo.addCons(x2 <= 10)
modelo.addCons(x3 <= 10)

# resolver problema
modelo.optimize()
# mostrar resultado
if modelo.getStatus() == "infeasible":
    print("INFACTÍVEL")
else:
    print(round(modelo.getObjVal(), 2))
