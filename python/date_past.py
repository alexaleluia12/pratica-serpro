import datetime

hoje = datetime.datetime.now()

tres_dias_atras = hoje - datetime.timedelta(days=3)
format_br = "%d/%m/%Y"
print(tres_dias_atras.strftime(format_br))