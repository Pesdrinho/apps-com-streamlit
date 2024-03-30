import pyodbc

DRIVER = 'SQL Server'
SERVER = 'Pepson'
DATABASE = 'Plataforma Hub'
USERNAME = 'sa'
PASSWORD = '060820'

connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
print(connectionString)
conn = pyodbc.connect(connectionString)

