# Luís Filipe Vasconcelos Peres
# 10310641

from pyscipopt import Model

# modelo
modelo = Model()
# configura logs
modelo.hideOutput(True)
# variaveis de decisao
x1 = modelo.addVar(vtype="C", lb=0)
x2 = modelo.addVar(vtype="C", lb=0)
x3 = modelo.addVar(vtype="C", lb=0)
# funcao objetivo
modelo.setObjective(0.56*x1+0.81*x2+0.46*x3, sense="minimize")
# restricoes
modelo.addCons(0.2*x1 + 0.5*x2 + 0.4*x3 >= 0.3)
modelo.addCons(0.6*x1 + 0.4*x2 + 0.4*x3 >= 0.5)
modelo.addCons(x1 + x2 + x3 == 1)
# resolver problema
modelo.optimize()
# mostrar resultado
print(modelo.getObjVal())
