class Coffee:
    def __init__(self, name):
        self.name = name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list(set([order.customer for order in self.orders()])
                    )

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        price_list = [order.price for order in self.orders()]
        average = (sum(price_list)/len(price_list))
        return average

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            print("Attribute cannot be changed")
        elif isinstance(name, str) and len(name) >= 3:
            self._name = name


class Customer:
    def __init__(self, name):
        self.name = name

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) < 15:
            self._name = name

    # @classmethod
    # def most_aficionado(cls, coffee):
    #     # list of all the customers who bought coffee
    #     # see how much each customer spent on the coffee
    #     customers = coffee.customers()
    #     prices = [float(order.price)
    #               for order in Order.all if order.customer in customers]
    #     print(prices)


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if hasattr(self, "price"):
            print("Price cannot be changed")
        elif isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee

    def __repr__(self):
        return f'<Order belongs to {self.customer.name} of {self.coffee.name}>'
