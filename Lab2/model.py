from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Таблиці
class Customer(Base):
    __tablename__ = 'Customer'
    customer_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    orders = relationship('Order', back_populates='customer', cascade="all, delete-orphan")


class Order(Base):
    __tablename__ = 'Order'
    order_id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    customer_id = Column(Integer, ForeignKey('Customer.customer_id', ondelete='CASCADE'))
    customer = relationship('Customer', back_populates='orders')
    deliveries = relationship('Delivery', back_populates='order', cascade="all, delete-orphan")
    product_orders = relationship('ProductOrder', back_populates='order', cascade="all, delete-orphan")


class Delivery(Base):
    __tablename__ = 'Delivery'
    delivery_id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    status = Column(String, nullable=False)
    order_id = Column(Integer, ForeignKey('Order.order_id', ondelete='CASCADE'))
    order = relationship('Order', back_populates='deliveries')


class Product(Base):
    __tablename__ = 'Product'
    product_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    product_orders = relationship('ProductOrder', back_populates='product', cascade="all, delete-orphan")


class ProductOrder(Base):
    __tablename__ = 'Product_Order'
    tab_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('Product.product_id', ondelete='CASCADE'))
    order_id = Column(Integer, ForeignKey('Order.order_id', ondelete='CASCADE'))
    product = relationship('Product', back_populates='product_orders')
    order = relationship('Order', back_populates='product_orders')

# Взаємодія з базою даних
class Model:
    def __init__(self):
        engine_url = 'postgresql+psycopg2://postgres:2535@localhost:5432/postgres'
        self.engine = create_engine(engine_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_customer(self, customer_id, name, email, phone):
         with self.Session() as session:
            customer = Customer(customer_id=customer_id, name=name, email=email, phone=phone)
            session.add(customer)
            session.commit()

    def add_product(self, product_id, name, price):
        with self.Session() as session:
            product = Product(product_id=product_id, name=name, price=price)
            session.add(product)
            session.commit()

    def add_order(self, order_id, date, customer_id):
        with self.Session() as session:
            order = Order(order_id=order_id, date=date, customer_id=customer_id)
            session.add(order)
            session.commit()

    def add_delivery(self, delivery_id, address, status, order_id):
        with self.Session() as session:
            delivery = Delivery(delivery_id=delivery_id, address=address, status=status, order_id=order_id)
            session.add(delivery)
            session.commit()

    def add_product_order(self, tab_id, product_id, order_id):
        with self.Session() as session:
            product_order = ProductOrder(tab_id=tab_id, product_id=product_id, order_id=order_id)
            session.add(product_order)
            session.commit()

    def update_customer(self, name, email, phone, id):
        with self.Session() as session:
            customer = session.query(Customer).filter_by(customer_id=id).first()
            if customer:
                customer.name = name
                customer.email = email
                customer.phone = phone
                session.commit()

    def update_product(self, name, price, id):
        with self.Session() as session:
            product = session.query(Product).filter_by(product_id=id).first()
            if product:
                product.name = name
                product.price = price
                session.commit()

    def update_order(self, date, customer_id, id):
        with self.Session() as session:
            order = session.query(Order).filter_by(order_id=id).first()
            if order:
                order.date = date
                order.customer_id = customer_id
                session.commit()

    def update_delivery(self, address, status, order_id, id):
        with self.Session() as session:
            delivery = session.query(Delivery).filter_by(delivery_id=id).first()
            if delivery:
                delivery.address = address
                delivery.status = status
                delivery.order_id = order_id
                session.commit()

    def update_product_order(self, product_id, order_id, tab_id):
        with self.Session() as session:
            product_order = session.query(ProductOrder).filter_by(tab_id=tab_id).first()
            if product_order:
                product_order.product_id = product_id
                product_order.order_id = order_id
                session.commit()

    def delete_customer(self, customer_id):
        with self.Session() as session:
            customer = session.query(Customer).filter_by(customer_id=customer_id).first()
            if customer:
                session.delete(customer)
                session.commit()

    def delete_order(self, order_id):
        with self.Session() as session:
            order = session.query(Order).filter_by(order_id=order_id).first()
            if order:
                session.delete(order)
                session.commit()

    def delete_delivery(self, delivery_id):
        with self.Session() as session:
            delivery = session.query(Delivery).filter_by(delivery_id=delivery_id).first()
            if delivery:
                session.delete(delivery)
                session.commit()

    def delete_product(self, product_id):
        with self.Session() as session:
            product = session.query(Product).filter_by(product_id=product_id).first()
            if product:
                session.delete(product)
                session.commit()

    def delete_product_order(self, tab_id):
        with self.Session() as session:
            product_order = session.query(ProductOrder).filter_by(tab_id=tab_id).first()
            if product_order:
                session.delete(product_order)
                session.commit()
