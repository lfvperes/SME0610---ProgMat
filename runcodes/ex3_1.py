# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# entrada
c = int(input())

# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x1 = modelo.addVar(vtype="C", name="x_1", lb=0)
x2 = modelo.addVar(vtype="I", name="x_2", lb=0)
# funcao objetivo
modelo.setObjective(c*x1 + (c + 4)*x2, sense="maximize")
# restricoes
modelo.addCons(10*x1 + 18*x2 <= 52)
modelo.addCons(-1*x1 + 1*x2 <= 2)
# resolver problema
modelo.optimize()
# mostrar resultado
print(round(modelo.getObjVal(), 2))
print(round(modelo.getVal(x1), 2))
print(modelo.getVal(x2))
