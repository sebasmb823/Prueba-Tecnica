import pandas as pd

# df_transacciones = pd.read_csv("transacciones.csv", sep=";")

# print(df_transacciones.head())

# print(df_transacciones.isnull().sum())

# print(f"Filas duplicadas: {df_transacciones.duplicated().sum()}")
# #6 filas duplicadas

# df_transacciones.drop_duplicates(inplace=True)
# print(f"Filas duplicadas despues de la limpieza: {df_transacciones.duplicated().sum()}")

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
# print(df_transacciones["fecha"].head(10))

#Limpieza de la columna monto
# print(df_transacciones["monto"].head(10))
# print(df_transacciones["monto"].isna().sum())

# df_transacciones["monto"] = df_transacciones["monto"].str.replace("$","",regex=False)
# df_transacciones["monto"] = df_transacciones["monto"].str.replace("COP","",regex=False)
# df_transacciones["monto"] = df_transacciones["monto"].str.replace(".","",regex=False)
# df_transacciones["monto"] = df_transacciones["monto"].str.replace(",","",regex=False)
# df_transacciones["monto"] = df_transacciones["monto"].replace("-", pd.NA)
# df_transacciones["monto"] = df_transacciones["monto"].replace("sin dato", "")
# df_transacciones["monto"] = df_transacciones["monto"].fillna(0)


# df_transacciones["monto"] = pd.to_numeric(df_transacciones["monto"])

# print(df_transacciones["monto"].head(10))
# print(df_transacciones["monto"].dtype)

#Limpieza de la columna tasa interes

# print(df_transacciones["tasa_interes"].isna().sum())

# df_transacciones["tasa_interes"] = df_transacciones["tasa_interes"].str.replace("%","", regex=False)
# df_transacciones["tasa_interes"] = df_transacciones["tasa_interes"].fillna(0)
# print(df_transacciones["tasa_interes"].isna().sum())

# print(df_transacciones["tasa_interes"])

# #Limpieza de la columna plazo dias
# print(df_transacciones["plazo_dias"].isna().sum())
# df_transacciones["plazo_dias"] = df_transacciones["plazo_dias"].str.replace("dias","",regex=False)
# df_transacciones["plazo_dias"] = df_transacciones["plazo_dias"].fillna(0)
# print(df_transacciones["plazo_dias"].isna().sum())
# print(df_transacciones["plazo_dias"])

#limpieza columna canal
# print(df_transacciones["canal"].isna().sum())
# print(df_transacciones["canal"].unique())

# df_transacciones["canal"] = df_transacciones["canal"].replace({
#     "web" : "Web",
#     "ATM" : "Cajero",
#     "oficina" : "Oficina",
#     "OFICINA" : "Oficina",
#     "cajero automatico" : "Cajero",
#     "app movil" : "App",
#     "APP" : "App"
# })
# print(df_transacciones["canal"].unique())

#limpieza columna estado
# print(df_transacciones["estado"].isna().sum())
# print(df_transacciones["estado"].unique())

# df_transacciones["estado"] = df_transacciones["estado"].replace({
#     "pend" : "Pendiente",
#     "aprobado" : "Aprobada",
#     "rechazada" : "Rechazada",
#     "APROBADA" : "Aprobada",
#     "PENDIENTE" : "Pendiente"
# })

# print(df_transacciones["estado"].unique())

#Limpieza columna sucursal 
# print(df_transacciones["sucursal"].isna().sum())
# print(df_transacciones["sucursal"].unique())

# df_transacciones["sucursal"] = df_transacciones["sucursal"].replace({
#     "cali" : "Cali",
#     "Bogota" : "Bogotá",
#     "b/quilla" : "Barranquilla",
#     "Medellin" : "Medellín",
#     "medellín" : "Medellín",
#     "BOGOTA" : "Bogotá",
#     "  Bogotá ": "Bogotá"
# })

# df_transacciones["sucursal"] = df_transacciones["sucursal"].fillna("Sin sucursal")
# print(df_transacciones["sucursal"].isna().sum())
# print(df_transacciones["sucursal"].unique())


#Columna monto COP
# dolar = 4000
# df_transacciones["monto_COP"] = df_transacciones["monto"]

# df_transacciones.loc[df_transacciones["moneda"] == "USD", "monto_COP"] = df_transacciones["monto"] * dolar

# print(df_transacciones["monto_COP"])


#Limpieza dataset clientes
df_clientes = pd.read_json("clientes.json")

print(df_clientes.columns)
#'id_cliente', 'nombre', 'tipo_documento', 'numero_documento',
#'segmento', 'ciudad', 'fecha_alta', 'contacto', 'productos', 'activo']


# print(df_clientes["id_cliente"].duplicated().sum())
# print(df_clientes["id_cliente"].value_counts())

#id_cliente duplicado 1011, 1004

# print(df_clientes[df_clientes["id_cliente"] == 1011].T)
# print(df_clientes[df_clientes["id_cliente"] == 1004].T)

df_clientes = df_clientes.drop_duplicates(subset="id_cliente", keep="first")
#print(df_clientes["id_cliente"].value_counts())

print(df_clientes["tipo_documento"].unique())

df_clientes["tipo_documento"] = df_clientes["tipo_documento"].replace({
    "cc" : "C.C.",
    "nit" : "NIT",
    "CC" : "C.C."
})
df_clientes["tipo_documento"] = df_clientes["tipo_documento"].fillna("Sin tipo documento")
print(df_clientes["tipo_documento"].unique())

#----Limpieza columna numero_documento
df_clientes["numero_documento"] = df_clientes["numero_documento"].str.replace(".","", regex= False)

#Limpieza segmento
print(df_clientes["segmento"].unique())

df_clientes["segmento"] = df_clientes["segmento"].replace({
    "personal" : "Personal",
    "premium": "Premium",
    "EMPRESARIAL" : "Empresarial",
    "Pyme" : "PYME",
    "pyme" : "PYME"
})
df_clientes["segmento"] = df_clientes["segmento"].fillna("Sin segmento")
print(df_clientes["segmento"].unique())

#Limpieza columna ciudad
df_clientes["ciudad"] = df_clientes["ciudad"].str.capitalize()
print(df_clientes["ciudad"].unique())

df_clientes["ciudad"] = df_clientes["ciudad"].replace({
    "  bogotá " : "Bogotá",
    "B/quilla" : "Barranquilla",
    "Bogota" : "Bogotá",
    " cúcuta" : "Cúcuta",
    "Medellin" : "Medellín"
})

print(df_clientes["ciudad"].unique())

#Limpieza columna activo
print(df_clientes["activo"].unique())
print(df_clientes["activo"].dtype)

df_clientes["activo"] = df_clientes["activo"].replace({
    "SI" : True,
    "Si" : True,
    "NO" : False,
    "No" : False
})
print(df_clientes["activo"].unique())



#Limpieza columna fecha

print(df_clientes["fecha_alta"].head(10))
#Valores a cambiar jul,ago,sep,oct,may,mar,ene,jun

df_clientes["fecha_alta"] = df_clientes["fecha_alta"].str.replace("jul", "07", regex=False)
df_clientes["fecha_alta"] = df_clientes["fecha_alta"].str.replace("ago", "08", regex=False)
df_clientes["fecha_alta"] = df_clientes["fecha_alta"].str.replace("sep", "09", regex=False)
df_clientes["fecha_alta"] = df_clientes["fecha_alta"].str.replace("oct", "10", regex=False)
df_clientes["fecha_alta"] = df_clientes["fecha_alta"].str.replace("may", "05", regex=False)
df_clientes["fecha_alta"] = df_clientes["fecha_alta"].str.replace("mar", "03", regex=False)
df_clientes["fecha_alta"] = df_clientes["fecha_alta"].str.replace("ene", "01", regex=False)
df_clientes["fecha_alta"] = df_clientes["fecha_alta"].str.replace("jun", "06", regex=False)

df_clientes["fecha_alta"] = pd.to_datetime(
    df_clientes["fecha_alta"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)
print(df_clientes["fecha_alta"].head(10))



# df_clientes = df_clientes.explode("productos")