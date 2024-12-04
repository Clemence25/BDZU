import time
from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '7':
                break
            if choice == '6':
                self.process_search_option()
            elif choice in ['1', '2', '3', '4', '5']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()
            if table == '6':
                break
            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_add_random_option(table)
            elif choice == '3':
                self.process_view_option(table)
            elif choice == '4':
                self.process_update_option(table)
            elif choice == '5':
                self.process_delete_option(table)

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding customer:")
            self.add_customer()
        elif table == '2':
            self.view.show_message("\nAdding product:")
            self.add_product()
        elif table == '3':
            self.view.show_message("\nAdding order:")
            self.add_order()
        elif table == '4':
            self.view.show_message("\nAdding delivery:")
            self.add_delivery()
        elif table == '5':
            self.view.show_message("\nAdding product-order association:")
            self.add_product_order()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_add_random_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding random customers:")
            self.add_random_fields()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_view_option(self, table):
        if table == '1':
            self.view_customers()
        elif table == '2':
            self.view_products()
        elif table == '3':
            self.view_orders()
        elif table == '4':
            self.view_deliveries()
        elif table == '5':
            self.view_product_orders()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating customer:")
            self.update_customer()
        elif table == '2':
            self.view.show_message("\nUpdating product:")
            self.update_product()
        elif table == '3':
            self.view.show_message("\nUpdating order:")
            self.update_order()
        elif table == '4':
            self.view.show_message("\nUpdating delivery:")
            self.update_delivery()
        elif table == '5':
            self.view.show_message("\nUpdating product-order association:")
            self.update_product_order()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting customer:")
            self.delete_customer()
        elif table == '2':
            self.view.show_message("\nDeleting product:")
            self.delete_product()
        elif table == '3':
            self.view.show_message("\nDeleting order:")
            self.delete_order()
        elif table == '4':
            self.view.show_message("\nDeleting delivery:")
            self.delete_delivery()
        elif table == '5':
            self.view.show_message("\nDeleting product-order association:")
            self.delete_product_order()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def add_customer(self):
      try:
        customer_id, name, email, phone = self.view.get_customer_input()
        self.model.add_customer(customer_id, name, email, phone)
        self.view.show_message("Customer added successfully!")
      except Exception as e:
        self.view.show_message(f"Something went wrong: {e}")

    def add_product(self):
     try:
        product_id, name, price = self.view.get_product_input()
        self.model.add_product(product_id, name, price)
        self.view.show_message("Product added successfully!")
     except Exception as e:
        self.view.show_message(f"Something went wrong: {e}")

    def add_order(self):
     try:
        order_id, date, customer_id = self.view.get_order_input()
        self.model.add_order(order_id, date, customer_id)
        self.view.show_message("Order added successfully!")
     except Exception as e:
        self.view.show_message(f"Something went wrong: {e}")

    def add_delivery(self):
     try:
        delivery_id, address, status, order_id = self.view.get_delivery_input()
        self.model.add_delivery(delivery_id, address, status, order_id)
        self.view.show_message("Delivery added successfully!")
     except Exception as e:
        self.view.show_message(f"Something went wrong: {e}")

    def add_product_order(self):
     try:
        tab_id, product_id, order_id = self.view.get_product_order_input()
        self.model.add_product_order(tab_id, product_id, order_id)
        self.view.show_message("Product-Order association added successfully!")
     except Exception as e:
        self.view.show_message(f"Something went wrong: {e}")


    def view_customers(self):
        customers = self.model.get_all_customers()
        self.view.show_customers(customers)

    def view_products(self):
        products = self.model.get_all_products()
        self.view.show_products(products)

    def view_orders(self):
        orders = self.model.get_all_orders()
        self.view.show_orders(orders)

    def view_deliveries(self):
        deliveries = self.model.get_all_deliveries()
        self.view.show_deliveries(deliveries)

    def view_product_orders(self):
        product_orders = self.model.get_all_product_orders()
        self.view.show_product_orders(product_orders)


    def update_customer(self):
            try:
                customer_id = self.view.get_id()
                name, email, phone = self.view.get_customer_input(include_id=False)
                self.model.update_customer(name, email, phone, customer_id)
                self.view.show_message("Customer updated successfully!")
            except Exception as e:
                self.view.show_message(f"Something went wrong: {e}")

    def update_product(self):
        try:
            product_id = self.view.get_id()
            name, price = self.view.get_product_input(include_id=False)
            self.model.update_product(name, price,product_id)
            self.view.show_message("Product updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def update_order(self):
        try:
            order_id = self.view.get_id()
            date, customer_id = self.view.get_order_input(include_id=False)
            self.model.update_order(date, customer_id,order_id)
            self.view.show_message("Order updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def update_delivery(self):
        try:
            delivery_id = self.view.get_id()
            address, status, order_id = self.view.get_delivery_input(include_id=False)
            self.model.update_delivery(address, status, order_id, delivery_id)
            self.view.show_message("Delivery updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_product_order(self):
        try:
            tab_id = self.view.get_id()
            product_id, order_id = self.view.get_product_order_input(include_id=False)
            self.model.update_product_order(product_id, order_id,tab_id)
            self.view.show_message("Product-Order association updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def delete_customer(self):
        try:
            customer_id = self.view.get_id()
            self.model.delete_customer(customer_id)
            self.view.show_message("Customer deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_product(self):
        try:
            product_id = self.view.get_id()
            self.model.delete_product(product_id)
            self.view.show_message("Product deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_order(self):
        try:
            order_id = self.view.get_id()
            self.model.delete_order(order_id)
            self.view.show_message("Order deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_delivery(self):
        try:
            delivery_id = self.view.get_id()
            self.model.delete_delivery(delivery_id)
            self.view.show_message("Delivery deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_product_order(self):
        try:
            tab_id = self.view.get_id()
            self.model.delete_product_order(tab_id)
            self.view.show_message("Product-Order association deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def process_search_option(self):
        option = self.view.show_search()
        if option == '1':
            self.show_customer_orders()
        elif option == '2':
            self.show_most_popular_product_for_customer()
        elif option == '3':
            self.show_orders_count_by_date_and_status()
        else:
            self.view.show_message("Invalid choice, back to menu")
            return

    def show_customer_orders(self):
        try:
            customer_id = self.view.get_id()
            start_date = input("Введіть початкову дату (YYYY-MM-DD): ")
            end_date = input("Введіть кінцеву дату (YYYY-MM-DD): ")
            start_time = time.time()
            orders = self.model.get_orders_by_customer(customer_id, start_date, end_date)
            if orders:
                self.view.show_orders_with_status(orders)
                elapsed_time = (time.time() - start_time) * 1000
                print(f"Час виконання запиту: {elapsed_time:.2f} мс")
            else:
                self.view.show_message("Не знайдено замовлень для цього клієнта у вказаний період.")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_most_popular_product_for_customer(self):
        try:
            customer_id = self.view.get_id()
            start_time = time.time()
            popular_product = self.model.get_most_popular_product_for_customer(customer_id)
            if popular_product:
                self.view.show_popular_product(popular_product)
                elapsed_time = (time.time() - start_time) * 1000
                print(f"Час виконання запиту: {elapsed_time:.2f} мс")
            else:
                self.view.show_message("У цього клієнта немає замовлень.")
        except Exception as e:
            self.view.show_message(f"Щось пішло не так: {e}")

    def show_orders_count_by_date_and_status(self):
        try:
            delivery_status, start_date, end_date = self.view.get_status_and_date_input()
            start_time = time.time()
            orders_count = self.model.get_orders_count_by_date_and_status(delivery_status, start_date, end_date)
            if orders_count:
                self.view.show_orders_count_by_date(orders_count)
                elapsed_time = (time.time() - start_time) * 1000
                print(f"Час виконання запиту: {elapsed_time:.2f} мс")
            else:
                self.view.show_message("Не знайдено замовлень з таким статусом у вказаний період.")
        except Exception as e:
            self.view.show_message(f"Помилка: {e}")

    def add_random_fields(self):
        try:
            number = self.view.get_number()
            self.model.add_random_fields(number)
            self.view.show_message("Random fields added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")