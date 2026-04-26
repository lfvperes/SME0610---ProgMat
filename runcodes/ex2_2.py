# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x1 = modelo.addVar(vtype="B", name="x_1")
x2 = modelo.addVar(vtype="B", name="x_2")
# funcao objetivo
modelo.setObjective(2*x1 + 3*x2, sense="maximize")
# restricoes
modelo.addCons(6*x1 + 8*x2 <= 10)
# resolver problema
modelo.optimize()
# mostrar resultado
print(modelo.getObjVal())
print(modelo.getVal(x1))
print(modelo.getVal(x2))
