import Connection
import psycopg2
from prettytable import PrettyTable

def outputTable(data):
    table = PrettyTable()
    table.field_names = [description[0] for description in cursor.description]
    for row in data:
        table.add_row(row)
    print(table)

try:
    # Підключення до бази даних
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()
    print("Підключення до бази даних PostgreSQL пройшло успішно")

    # Запит 1: Відобразити всі ліки, які відпускаються за рецептом лікаря. Відсортувати за назвою ліків.
    query1 = """
    SELECT 
        medicine_name AS "Назва ліків"
    FROM 
        Medicines
    WHERE 
        prescription_required = TRUE
    ORDER BY 
        medicine_name;
    """
    cursor.execute(query1)
    outputTable(cursor.fetchall())

    # Запит 2: Відобразити всі ліки за обраною групою (запит з параметром)
    medicine_group = input("Введіть групу ліків: ")
    query2 = """
    SELECT 
        medicine_name AS "Назва ліків", 
        medicine_group AS "Група ліків"
    FROM 
        Medicines
    WHERE 
        medicine_group = %s;
    """
    cursor.execute(query2, (medicine_group,))
    outputTable(cursor.fetchall())

    # Запит 3: Порахувати вартість кожної поставки (запит з обчислювальним полем)
    query3 = """
    SELECT 
        supply_code AS "ID поставки",
        SUM(price * quantity_supplied) AS "Загальна вартість"
    FROM 
        Supplies
    JOIN 
        Medicines ON Supplies.medicine_registration_number = Medicines.medicine_registration_number
    GROUP BY 
        supply_code;
    """
    cursor.execute(query3)
    outputTable(cursor.fetchall())

    # Запит 4: Порахувати загальну суму грошей, яку сплатила аптека кожному постачальнику (підсумковий запит)
    query4 = """
    SELECT 
        supplier_name AS "Назва постачальника",
        SUM(price * quantity_supplied) AS "Загальна сума"
    FROM 
        Supplies
    JOIN 
        Suppliers ON Supplies.supplier_code = Suppliers.supplier_code
    JOIN 
        Medicines ON Supplies.medicine_registration_number = Medicines.medicine_registration_number
    GROUP BY 
        supplier_name;
    """
    cursor.execute(query4)
    outputTable(cursor.fetchall())

    # Запит 5: Порахувати кількість поставок для кожної групи ліків від вітчизняних та закордонних постачальників (перехресний запит)
    query5 = """
    SELECT 
        medicine_group AS "Група ліків",
        location AS "Країна постачальника",
        COUNT(supply_code) AS "Кількість поставок"
    FROM 
        Supplies
    JOIN 
        Medicines ON Supplies.medicine_registration_number = Medicines.medicine_registration_number
    JOIN 
        Suppliers ON Supplies.supplier_code = Suppliers.supplier_code
    GROUP BY 
        medicine_group, location;
    """
    cursor.execute(query5)
    outputTable(cursor.fetchall())

    # Запит 6: Порахувати останню дату придатності для кожної ліки (запит з обчислювальним полем)
    query6 = """
    SELECT 
        medicine_name AS "Назва ліків",
        MAX(supply_date + shelf_life_days * interval '1 day') AS "Остання дата придатності"
    FROM 
        Supplies
    JOIN 
        Medicines ON Supplies.medicine_registration_number = Medicines.medicine_registration_number
    GROUP BY 
        medicine_name;
    """
    cursor.execute(query6)
    outputTable(cursor.fetchall())

except (Exception, psycopg2.Error) as error:
    print("Помилка при роботі з PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Підключення до PostgreSQL закрито")
