from app import app

# Configurar conexión a SQL Server
class Config:
    SQLALCHEMY_DATABASE_URI = ("mssql+pyodbc://sa:2025@FELICIDAD/EscuelaOficios?driver=ODBC+Driver+17+for+SQL+Server")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
