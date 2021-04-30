# Desafio pokemon aniversário:
mes = input("Informe o mês de aniversário: ")
dia = int(input("Informe o dia: "))
# Mês:
if mes == "janeiro" or mes == "agosto":
  tipo = "ground"
elif mes == "fevereiro" or mes == "novembro":
  tipo = "fighting"
elif mes == "março" or mes == "julho":
  tipo = "normal"
elif mes == "abril" or mes == "dezembro":
  tipo = "steel"
elif mes == "maio" or mes == "setembro":
  tipo = "flying"
elif mes == "junho" or mes == "outubro":
  tipo = "psychic"
# Dia:
if dia == 1 or dia == 17 or dia == 9:
  tipo = tipo + " eletric"
if dia == 4 or dia == 12 or dia == 23:
  tipo = tipo + " dark"
if dia == 7 or dia == 18:
  tipo = tipo + " bug"
if dia == 2 or dia == 10 or dia == 21:
  tipo = tipo + " fairy"
if dia == 13 or dia == 26:
  tipo = tipo + " fire"
if dia == 6 or dia == 16 or dia == 29 :
  tipo = tipo + " ice"
if dia == 8 or dia == 19 or dia == 30:
  tipo = tipo + " poison"
if dia == 11 or dia == 22:
  tipo = tipo + " ghost"
if dia == 14 or dia == 25 :
  tipo = tipo +" grass"
if dia == 15 or dia == 28:
  tipo = tipo + " water"
if dia == 20 or dia == 31 :
  tipo = tipo + " rock"
if dia == 3 or dia == 24 :
  tipo = tipo +" normal"
if dia == 5 or dia == 27:
  tipo = tipo + " dragon"
print(tipo)