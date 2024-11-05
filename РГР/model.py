import time
import psycopg2
import random


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='2535',
            host='localhost',
            port=5432
        )


    def add_customer(self, customer_id, name, email, phone):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Customer" ("customer_id", "name", "email", "phone") VALUES (%s, %s, %s, %s)',
                  (customer_id, name, email, phone))
        self.conn.commit()

    def get_all_customers(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "Customer" ORDER BY customer_id ASC')
            return cursor.fetchall()

    def update_customer(self, name, email, phone, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Customer" SET "name"=%s, "email"=%s, "phone"=%s WHERE "customer_id"=%s',
                  (name, email, phone, id))
        self.conn.commit()

    def delete_customer(self, customer_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Customer" WHERE "customer_id"=%s', (customer_id,))
        self.conn.commit()


    def add_product(self, product_id, name, price):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Product" ("product_id", "name", "price") VALUES (%s, %s, %s)',
                  (product_id, name, price))
        self.conn.commit()

    def get_all_products(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "Product" ORDER BY product_id ASC')
            return cursor.fetchall()

    def update_product(self, name, price, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Product" SET "name"=%s, "price"=%s WHERE "product_id"=%s',
                  (name, price, id))
        self.conn.commit()

    def delete_product(self, product_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Product" WHERE "product_id"=%s', (product_id,))
        self.conn.commit()



    def add_order(self, order_id, date, customer_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Order" ("order_id", "date", "customer_id") VALUES (%s, %s, %s)',
                  (order_id, date, customer_id))
        self.conn.commit()

    def get_all_orders(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "Order" ORDER BY order_id ASC')
            return cursor.fetchall()

    def update_order(self, date, customer_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Order" SET "date"=%s, "customer_id"=%s WHERE "order_id"=%s',
                  (date,customer_id, id))
        self.conn.commit()

    def delete_order(self, order_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Order" WHERE "order_id"=%s', (order_id,))
        self.conn.commit()


    def add_delivery(self, delivery_id, address, status, order_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Delivery" ("delivery_id", "address", "status", "order_id") VALUES (%s, %s, %s, %s)',
                  (delivery_id, address, status, order_id))
        self.conn.commit()

    def get_all_deliveries(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "Delivery" ORDER BY delivery_id ASC')
            return cursor.fetchall()

    def update_delivery(self, address, status,order_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Delivery" SET "address"=%s, "status"=%s,"order_id"=%s WHERE "delivery_id"=%s',
                  (address,status,order_id, id))
        self.conn.commit()

    def delete_delivery(self, delivery_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Delivery" WHERE "delivery_id"=%s', (delivery_id,))
        self.conn.commit()


    def add_product_order(self, tab_id,product_id, order_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Product_Order" ("tab_id","product_id", "order_id") VALUES (%s, %s,%s)' ,
                  (tab_id, product_id, order_id))
        self.conn.commit()

    def get_all_product_orders(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "Product_Order" ORDER BY tab_id ASC')
            return cursor.fetchall()

    def update_product_order(self, product_id, order_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE "Product_Order" SET "product_id"=%s,"order_id"=%s WHERE "tab_id"=%s',
                  (product_id,order_id, id))
        self.conn.commit()

    def delete_product_order(self, tab_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Product_Order" WHERE "tab_id"=%s', (tab_id,))
        self.conn.commit()

    def get_orders_by_customer(self, customer_id, start_date, end_date):
        with self.conn.cursor() as cursor:
            query = '''
                SELECT o.order_id, o.date, c.name AS customer_name, d.status
                FROM "Order" o
                JOIN "Customer" c ON o.customer_id = c.customer_id
                LEFT JOIN "Delivery" d ON o.order_id = d.order_id
                WHERE o.customer_id = %s AND o.date BETWEEN %s AND %s
                ORDER BY o.date;
            '''
            cursor.execute(query, (customer_id, start_date, end_date))
            result = cursor.fetchall()
            return result

    def get_most_popular_product_for_customer(self, customer_id):
        with self.conn.cursor() as cursor:
            query = '''
                SELECT p.name AS product_name, COUNT(po.product_id) AS times_ordered
                FROM "Customer" c
                JOIN "Order" o ON c.customer_id = o.customer_id
                JOIN "Product_Order" po ON o.order_id = po.order_id
                JOIN "Product" p ON po.product_id = p.product_id
                WHERE c.customer_id = %s
                GROUP BY p.name
                ORDER BY times_ordered DESC
                LIMIT 1;
            '''
            cursor.execute(query, (customer_id,))
            result = cursor.fetchone()
            return result

    def get_orders_count_by_date_and_status(self, delivery_status, start_date, end_date):
      with self.conn.cursor() as cursor:
        query = """
            SELECT o.date, d.status, COUNT(*) AS order_count
            FROM "Order" o
            JOIN "Delivery" d ON o.order_id = d.order_id
            WHERE d.status = %s AND o.date BETWEEN %s AND %s
            GROUP BY o.date, d.status
            ORDER BY o.date;
          """
        cursor.execute(query, (delivery_status, start_date, end_date))
        result = cursor.fetchall()
        return result

    def add_random_fields(self, number):
                c = self.conn.cursor()
                first_names = ['John', 'Ann', 'Bob', 'Joel', 'Jannet', 'Ria','Mia','Sophie','Jennie','Stella','Jules',
                               'Ava','Bridget','Juliet','Rhys','Alex','Cardan','Jude','Vivien','Seth','Christian',
                               'Sylus','Tarin','Rhysand','Feyre','Emilia','Carissa','Oraya','Raihn','Suren','Oak',
                               'Lauren','Kai','Paedyn','Stephanie','Evangeline','Karen','Kerri','Daniel','Ashley',
                               'Aaryan','Isabel','Selena','Shawn','Avrora','James','Zoe','Belle','Zane','Xavier',
                               'Rafayel','Zack','Mei'

                               ]
                last_names = ['Smith', 'Nelson', 'Wilson', 'Parker', 'Garber', 'Roberts','Black','Chen','Harper',
                              'Ambrose','Alonso','Greenbriar','Larsen','Angelo','Grey','Laross','Martinez','Gomez',
                              'Skye','Atlantic','Cameron','Regas','Grande','Huang','Muarte','Floranse','Nevil','Cabello',
                              'Mendes','Olives','Monroe','Monroe','Jordan','Del','Rey','Clark','Spilberg','Han','Duarte',
                              'Douglas','Maas','Bridgerton','Feather','Benson','Raiden'
                              ]

                query = '''
                      WITH max_id AS (SELECT COALESCE(MAX("customer_id"), 0) FROM public."Customer")
            INSERT INTO public."Customer" ("customer_id", "name", "email", "phone")
            SELECT 
                (SELECT * FROM max_id) + row_number() OVER () AS "customer_id",
                CONCAT_WS(' ', first_name, last_name) AS "name",
                LOWER(first_name || '.' || last_name) || '@' ||
                (CASE (random() * 10)::integer
                    WHEN 0 THEN 'gmail'
                    WHEN 1 THEN 'hotmail'
                    WHEN 2 THEN 'yahoo'
                    WHEN 3 THEN 'gov'
                    WHEN 4 THEN 'ukr'
                    WHEN 5 THEN 'wers'
                    WHEN 6 THEN 'sitit'
                    WHEN 7 THEN 'mmska'
                    WHEN 8 THEN 'hotline'
                    WHEN 9 THEN 'olx'
                    WHEN 10 THEN 'lllkpi'
                END) || '.com' AS "email",
                CONCAT('+1', (1000000000 + floor(random() * 9000000000)::bigint)::text) AS "phone"
            FROM (SELECT unnest(ARRAY[%s]) AS first_name, unnest(ARRAY[%s]) AS last_name
                  FROM generate_series(1, %s * 1000)) AS names;
                '''
                first_names_sample = [random.choice(first_names) for _ in range(number)]
                last_names_sample = [random.choice(last_names) for _ in range(number)]
                c.execute(query, (first_names_sample, last_names_sample, number))
                self.conn.commit()














