import pandas as pd

df_transacciones = pd.read_csv("transacciones.csv", sep=";")

print(df_transacciones.head())

print(df_transacciones.isnull().sum())

print(f"Filas duplicadas: {df_transacciones.duplicated().sum()}")
#6 filas duplicadas

df_transacciones.drop_duplicates(inplace=True)
print(f"Filas duplicadas despues de la limpieza: {df_transacciones.duplicated().sum()}")

#-------------- Estandarizacion de datos -----------------------

# df_transacciones["tipo_producto"] = df_transacciones["tipo_producto"].str.lower()

# print("--- Limpieza tipo producto ---")
# print(df_transacciones["tipo_producto"].unique())
# #Limpieza tipo producto
# df_transacciones["tipo_producto"] = df_transacciones["tipo_producto"].replace({
#     "ahorros": "Cuenta de Ahorros",
#     "cuenta de ahorros" : "Cuenta de Ahorros",
#     "cuenta ahorros" : "Cuenta de Ahorros",
#     "cta_ahorros":"Cuenta de Ahorros",
#     "cdt " : "CDT",
#     "cdt" : "CDT",
#     "certificado de deposito" : "CDT",
#     "crédito" : "Crédito",
#     "credito" : "Crédito",
#     "cuenta corriente" : "Cuenta Corriente",
#     "corriente" : "Cuenta Corriente",
#     "cta corriente" : "Cuenta Corriente"
# })
# print("----------------------------------------")
# print(df_transacciones["tipo_producto"].unique())

#Limpieza columna moneda
# print(df_transacciones["moneda"].unique())

# df_transacciones["moneda"] = df_transacciones["moneda"].replace({
#     "Pesos" : "COP",
#     "Dolares" : "USD",
#     "cop" : "COP",
#     "pesos" : "COP",
#     "usd" : "USD",
#     "$" : "COP" 
# })

# df_transacciones["moneda"] = df_transacciones["moneda"].fillna("Sin categoría")
# print(df_transacciones["moneda"].unique())

#------ Limpieza fechas

# df_transacciones["fecha"] = pd.to_datetime(
#     df_transacciones["fecha"],
#     format="mixed",
#     dayfirst=True,
#     errors="coerce"
# )
# print(df_transacciones["fecha"].head())

#Limpieza de la columna monto
print(df_transacciones["monto"].info())
print(df_transacciones["monto"].isna().sum())

df_transacciones["monto"] = df_transacciones["monto"].str.replace("$","",regex=False)
df_transacciones["monto"] = df_transacciones["monto"].str.replace("COP","",regex=False)

print(df_transacciones["monto"])

