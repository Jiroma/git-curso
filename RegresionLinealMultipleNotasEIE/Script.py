try:
	import pandas as pd
	import numpy as np
	import statsmodels.formula.api as smf
except:
        import subprocess, sys, pip
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade','pip'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas','statsmodels'])
        import pandas as pd
        import numpy as np
        import statsmodels.formula.api as smf
        print("----------------------------------------------------------------")
                
def Nota_Final_Prediccion(Nota_1=1,Asistencia=0):
	Nota_Final_Prediccion=lm.params.Intercept+lm.params.Nota_1*Nota_1+lm.params.Asistencia*Asistencia
	return Nota_Final_Prediccion

dataBase=pd.read_csv("dataBase.csv")
lm=smf.ols(formula="Nota_Final~Nota_1+Asistencia",data=dataBase).fit()

print("""Bienvenido Estudiante
Puedes predecir cuál será tu nota a final de semestre en base a:
	La primera nota del ramo:	valor entre [1.0 y 7.0]
	La asistencia esperada:		valor entre [0 y 100]
----------------------------------------------------------------""")
while True:
	Nota_1=float(input("Ingrese primera nota: "))
	Asistencia=float(input("Ingrese asistencia esperada: "))
	print("----------------------------------------------------------------")
	print("Esta IA predice que su nota a final de semestre será: ",round(Nota_Final_Prediccion(Nota_1,Asistencia),1))
	print("----------------------------------------------------------------")
