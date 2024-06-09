import Connection
from prettytable import PrettyTable

# Словник з відповідностями англійських та українських заголовків
ukrainian_headers = {
    "medicine_registration_number": "Реєстраційний номер ліки",
    "medicine_name": "Назва ліки",
    "manufacture_date": "Дата виготовлення",
    "shelf_life_days": "Термін зберігання (дні)",
    "medicine_group": "Група",
    "price": "Ціна",
    "prescription_required": "Відпускається за рецептом лікаря",
    "supplier_code": "Код постачальника",
    "supplier_name": "Назва постачальника",
    "supplier_address": "Адреса",
    "supplier_phone": "Телефон",
    "contact_person": "Контактна особа",
    "location": "Розташування",
    "supply_code": "Код поставки",
    "supply_date": "Дата поставки",
    "medicine_registration_number": "Номер ліки",
    "quantity_supplied": "Кількість ліків",
    "supplier_code": "Код постачальника"
}

try:
    # Підключення до бази даних
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()

    def print_table(name_table, table_label):
        cursor.execute(f"SELECT * FROM {name_table}")
        data = cursor.fetchall()
        table = PrettyTable()
        table.title = table_label
        table.field_names = [ukrainian_headers[description[0]] for description in cursor.description if description[0] in ukrainian_headers]
        for row in data:
            table.add_row(row)
        print(table)

    print_table("Medicines", "Ліки")
    print_table("Suppliers", "Постачальники")
    print_table("Supplies", "Поставки")

except Exception as e:
    print(f"Помилка при виводі таблиць в консоль: {e}")

finally:
    cursor.close()
    connection.close()