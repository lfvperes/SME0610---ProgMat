# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x1 = modelo.addVar(vtype="C", name="x_1", lb=0)
x2 = modelo.addVar(vtype="I", name="x_2", lb=0)
# funcao objetivo
modelo.setObjective(10*x1 + 6*x2, sense="maximize")
# restricoes
modelo.addCons(9*x1 + 5*x2 <= 45)
modelo.addCons(-4*x1 + 5*x2 <= 5)
# resolver problema
modelo.optimize()
# mostrar resultado
print(round(modelo.getObjVal(), 2))
print(round(modelo.getVal(x1), 2))
print(modelo.getVal(x2))
