estudante = [{'ra': 123, 'curso': 'PP', 'nota': 8.5} ,
             {'ra': 456, 'curso': 'ADS', 'nota': 9.5} ,
             {'ra': 789, 'curso': 'SI', 'nota': 7.5} ,]

notasmenores = list(filter(lambda x: x['nota'] < 8.0, estudante))