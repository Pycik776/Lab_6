import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

try:
    # Таблиця Ліки
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Medicines (
        medicine_registration_number integer PRIMARY KEY,
        medicine_name varchar(255),
        manufacture_date DATE,
        shelf_life_days integer,
        medicine_group varchar(20),
        price decimal,
        prescription_required boolean
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Medicines: {e}")

try:
    # Таблиця Постачальники
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Suppliers (
        supplier_code integer PRIMARY KEY,
        supplier_name varchar(255),
        supplier_address varchar(255),
        supplier_phone varchar(20),
        contact_person varchar(255),
        location varchar(50)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Suppliers: {e}")

try:
    # Таблиця Поставки
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Supplies (
        supply_code integer PRIMARY KEY,
        supply_date DATE,
        medicine_registration_number integer,
        quantity_supplied integer,
        supplier_code integer,
        FOREIGN KEY (medicine_registration_number) REFERENCES Medicines(medicine_registration_number),
        FOREIGN KEY (supplier_code) REFERENCES Suppliers(supplier_code)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Supplies: {e}")

cursor.close()
connection.close()