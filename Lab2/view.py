from datetime import datetime

class View:

    def show_menu(self):
        self.show_message("\nМеню:")
        self.show_message("1. Додати рядок")
        self.show_message('2. Генерувати рандомізовані дані(тільки для таблиці "Customer")')
        self.show_message("3. Показати таблицю")
        self.show_message("4. Редагувати рядок")
        self.show_message("5. Видалити рядок")
        self.show_message("6. Пошук")
        self.show_message("7. Вихід")
        return input("Виберіть пункт: ")

    def show_tables(self):
        self.show_message("\nТаблиці:")
        self.show_message("1. Customer (клієнт)")
        self.show_message("2. Product (продукт)")
        self.show_message("3. Order (замовлення)")
        self.show_message("4. Delivery (доставка)")
        self.show_message("5. Product_Order (продукт-замовлення)")
        self.show_message("6. Повернутися до меню")
        return input("Оберіть потрібну таблицю: ")

    def show_customers(self, customers):
        print("\nCustomers:")
        for customer in customers:
            print(f"ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}, Phone: {customer[3]}")

    def show_products(self, products):
        print("\nProducts:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")

    def show_orders(self, orders):
        print("\nOrders:")
        for order in orders:
            print(f"ID: {order[0]}, Date: {order[1]}, Customer ID: {order[2]}")

    def show_deliveries(self, deliveries):
        print("\nDeliveries:")
        for delivery in deliveries:
            print(f"ID: {delivery[0]}, Address: {delivery[1]}, Status: {delivery[2]}, Order ID: {delivery[3]}")

    def show_product_orders(self, product_orders):
        print("\nProduct Orders:")
        for product_order in product_orders:
            print(f"Product ID: {product_order[0]}, Order ID: {product_order[1]}")

    def show_orders_with_status(self, orders):
        print("\nЗамовлення клієнта за проміжок часу:")
        for order in orders:
            order_id, order_date, customer_name, delivery_status = order
            print(f"ID замовлення: {order_id}, Дата: {order_date}, Клієнт: {customer_name}, Статус: {delivery_status}")

    def show_popular_product(self, product):
        product_name, times_ordered = product
        print("\nНайпопулярніший продукт у клієнта:")
        print(f"Назва продукту: {product_name}, Замовлено разів: {times_ordered}")

    def show_orders_count_by_date(self, orders_count):
        print("\nКількість замовлень за датами та статусом:")
        for order_date, delivery_status, order_count in orders_count:
            print(f"Дата: {order_date}, Статус: {delivery_status}, Кількість замовлень: {order_count}")

    def show_search(self):
        self.show_message("\nПошук:")
        self.show_message("1. Замовлення клієнта за проміжок часу")
        self.show_message("2. Найпопулярніший продукт у клієнта")
        self.show_message("3. Кількість замовлень за датами та статусом")
        self.show_message("4. Повернутися до меню")
        choice = input("Оберіть щось: ")
        return choice

    def get_customer_input(self,include_id=True):
        if include_id:
            customer_id = input("Enter Сustomer ID: ")
        else:
            customer_id = None
        while True:
            name = input("Enter Customer name: ")
            if name.strip():
                break
            else:
                print("Name cannot be empty.")
        while True:
            email = input("Enter Customer email: ")
            if email.strip():
                break
            else:
                print("Email cannot be empty.")
        while True:
            phone = input("Enter Customer phone: ")
            if phone.strip():
                break
            else:
                print("Phone cannot be empty.")
        return (customer_id, name, email, phone) if include_id else (name, email, phone)

    def get_product_input(self,include_id=True):
        if include_id:
            product_id = input("Enter Product ID: ")
        else:
            product_id = None
        while True:
            name = input("Enter Product name: ")
            if name.strip():
                break
            else:
                print("Name cannot be empty.")
        while True:
            try:
                price = float(input("Enter Product price: "))
                break
            except ValueError:
                print("Price must be a number.")

        return (product_id, name, price) if include_id else (name, price)

    def get_order_input(self,include_id=True):
        if include_id:
            order_id = input("Enter Order ID: ")
        else:
            order_id = None
        while True:
            try:
                date = input("Enter date (YYYY-MM-DD): ")
                date = datetime.strptime(date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        while True:
            try:
                customer_id = int(input("Enter Customer ID: "))
                break
            except ValueError:
                print("Customer ID must be a number.")
        return  (order_id, date, customer_id) if include_id else (date, customer_id)

    def get_delivery_input(self,include_id=True):
        if include_id:
            delivery_id = input("Enter Delivery ID: ")
        else:
            delivery_id = None
        while True:
            address = input("Enter address: ")
            if address.strip():
                break
            else:
                print("Address cannot be empty.")
        while True:
            status = input("Enter status (Pending, Shipped, Delivered, Cancelled): ")
            if status.strip():
                break
            else:
                print("Status cannot be empty.")
        while True:
            try:
                order_id = int(input("Enter Order ID: "))
                break
            except ValueError:
                print("Order ID must be a number.")
        return  (delivery_id, address, status, order_id) if include_id else (address, status, order_id)

    def get_product_order_input(self,include_id=True):
        if include_id:
            tab_id = input("Enter Tab ID: ")
        else:
            tab_id = None
        while True:
            try:
                product_id = int(input("Enter Product ID: "))
                break
            except ValueError:
                print("Product ID must be a number.")
        while True:
            try:
                order_id = int(input("Enter Order ID: "))
                break
            except ValueError:
                print("Order ID must be a number.")
        return (tab_id,product_id, order_id) if include_id else (product_id, order_id)

    def get_customer_search_input(self):
        customer_id = int(input("Введіть ID клієнта: "))
        start_date = input("Введіть початкову дату (YYYY-MM-DD): ")
        end_date = input("Введіть кінцеву дату (YYYY-MM-DD): ")
        return customer_id, start_date, end_date

    def get_status_and_date_input(self):
        delivery_status = input("Введіть статус доставки (наприклад, 'Shipped', 'Pending'): ")
        start_date = input("Введіть початкову дату (YYYY-MM-DD): ")
        end_date = input("Введіть кінцеву дату (YYYY-MM-DD): ")
        return delivery_status, start_date, end_date

    def get_id(self):
        while True:
            try:
                id = int(input("Enter ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_message(self, message):
        print(message)


    def get_number(self):
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("It must be a number.")
        return number


