import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

try:
    # Додавання ліків
    medicines_data = [
        (1, "Парацетамол", "2023-01-01", 365, "протизапальне", 50.00, True),
        (2, "Ібупрофен", "2023-02-01", 365, "протизапальне", 45.00, True),
        (3, "Аспірин", "2023-03-01", 365, "протизапальне", 30.00, True),
        (4, "Анальгін", "2023-04-01", 365, "знеболююче", 25.00, False),
        (5, "Но-шпа", "2023-05-01", 365, "знеболююче", 40.00, False),
        (6, "Вітамін С", "2023-06-01", 365, "вітаміни", 20.00, False),
        (7, "Вітамін D", "2023-07-01", 365, "вітаміни", 35.00, False),
        (8, "Ампіцилін", "2023-08-01", 365, "протизапальне", 55.00, True),
        (9, "Цефтріаксон", "2023-09-01", 365, "протизапальне", 65.00, True),
        (10, "Нурофен", "2023-10-01", 365, "знеболююче", 50.00, True),
        (11, "Комплівіт", "2023-11-01", 365, "вітаміни", 30.00, False),
        (12, "Панкреатин", "2023-12-01", 365, "вітаміни", 25.00, False),
        (13, "Магне B6", "2024-01-01", 365, "вітаміни", 45.00, False)
    ]

    insert_query = """
    INSERT INTO Medicines (medicine_registration_number, medicine_name, manufacture_date, shelf_life_days, medicine_group, price, prescription_required)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (medicine_registration_number) DO NOTHING
    """

    for record in medicines_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Medicines: {e}")

try:
    # Додавання постачальників
    suppliers_data = [
        (1, "Фармація Україна", "м. Київ, вул. Богдана Хмельницького, 10", "+380671234567", "Олександр Коваль", "Україна"),
        (2, "Медікал Груп", "м. Львів, пр. Свободи, 20", "+380682345678", "Ірина Петренко", "Україна"),
        (3, "Здоров'я та Життя", "м. Одеса, вул. Дерибасівська, 30", "+380633456789", "Володимир Сидоренко", "Україна"),
        (4, "Фарма Плюс", "м. Харків, вул. Сумська, 45", "+380684567890", "Наталія Іванова", "Україна"),
        (5, "Глобал Фарм", "г. Варшава, ул. Маршала Пілсудського, 50", "+48221234567", "Ян Ковальський", "інша країна")
    ]

    insert_query = """
    INSERT INTO Suppliers (supplier_code, supplier_name, supplier_address, supplier_phone, contact_person, location)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (supplier_code) DO NOTHING
    """

    for record in suppliers_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Suppliers: {e}")

try:
    # Додавання поставок
    supplies_data = [
        (1, "2024-01-01", 1, 100, 1),
        (2, "2024-02-01", 2, 150, 1),
        (3, "2024-03-01", 3, 200, 2),
        (4, "2024-04-01", 4, 250, 2),
        (5, "2024-05-01", 5, 300, 3),
        (6, "2024-06-01", 6, 350, 3),
        (7, "2024-07-01", 7, 400, 4),
        (8, "2024-08-01", 8, 450, 4),
        (9, "2024-09-01", 9, 500, 5),
        (10, "2024-10-01", 10, 550, 5),
        (11, "2024-11-01", 11, 600, 1)
    ]

    insert_query = """
    INSERT INTO Supplies (supply_code, supply_date, medicine_registration_number, quantity_supplied, supplier_code)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (supply_code) DO NOTHING
    """

    for record in supplies_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Supplies: {e}")

cursor.close()
connection.close()
