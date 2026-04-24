from datetime import datetime

def validate_name(name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Nome invalido")
    
def validate_date(date):
    if not isinstance(date, str):
        raise ValueError("Data invalida")
    
    try:
        datetime.strptime(date, "%d-%m-%Y")
    
    except ValueError:
        raise ValueError("Data invalida. Formato correto (DD-MM-YYYY)")
    
def validate_number(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Dados invalidos")