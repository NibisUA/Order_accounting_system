class Client:
    def __init__(self, name,contact_info,client_id):
        self.name = name
        self.contact_info = contact_info
        self.client_id = client_id

    def update_contact_info(self, new_contact_info):
        self.contact_info = new_contact_info
    def __str__(self):
        return f"Client ID: {self.client_id}\nName: {self.name}\nContact Info: {self.contact_info}"
#-------------------------------------------------------------------------------------------------------
class Product:
    def __init__(self, name, description, price, quantity, product_id ):
        self.name = name
        self.descriptoin = description
        self.price = price
        self.quantity = quantity
        self.product_id = product_id

    def update_price(self,new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def __str__(self):
        return f"Product: {self.name}\nDescription: {self.descriptoin}\nPrice: {self.price}$\nQuantity: {self.quantity}"
#--------------------------------------------------------------------------------------------------------
class Order:
    def __init__(self, order_id,client, products):
        self.order_id = order_id
        self.client = client
        self.products = products
        self.total_price = self.sum_price()

    def sum_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def add_product(self,product):
        self.products.append(product)
        self.total_price = self.sum_price()

    def __str__(self):
        return f"Order ID: {self.order_id}\nClient: {self.client}\nTotal Price: {self.total_price}$\n"
#-------------------------------------------------------------------------------------------------------
class AccountingSystem:
    def __init__(self):
        self.clients = []
        self.products = []
        self.orders = []

    def add_client(self, client):
        self.clients.append(client)

    def add_product(self,product):
        self.products.append(product)

    def create_order(self, order_id, client_id, product_ids):
        client = self.find_client(client_id)
        if client is None:
            return "Такого кліенту немає"
        products = []
        for product_id in product_ids:
            product = self.find_product(product_id)
            if product is not None:
                products.append(product)
        if len(products) == 0:
            return "Такаго продукту немає"
        order = Order(order_id, client, products)
        self.orders.append(order)
        return "Заказ прийнятий"

    def find_client(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        if found_client is not None:
            print("Найден клиент:")
            print(found_client)
            return None
        else:
            return f"Клиент не найден"

    def find_product(self,producr_id):
        for product in self.products:
            if product.product_id == producr_id:
                return product
        return None
        if found_product is not None:
            print("Найден продукт:")
            print(found_product)
        else:
            return f"Продукт не найден"

    def __str__(self):
        client_info = "\n--- Clients ---\n"
        for client in self.clients:
            client_info += str(client) + "\n"
        product_info = "\n--- Products ---\n"
        for product in self.products:
            product_info += str(product) + "\n"
        order_info = "\n--- Orders ---\n"
        for order in self.orders:
            order_info += str(order) + "\n"
        return client_info + product_info + order_info

    def remove_product(self, product_id):
        product = self.find_product(product_id)
        if product is not None:
            self.products.remove(product)
            return f"Продукт \"{product.name}\"успішно видалений"
        else:
            return f"Продукт\"{product.name}\" не знайден"

    def remove_client(self, client_id):
        client = self.find_client(client_id)
        if client is not None3:
            self.clients.remove(client)
            return f"Клієнт \"{client.name}\" успішно видалений"
        else:
            return f"Клієнт \"{client.name}\" знайден"
#-------------------------------------------------------------------------------------------------
def main_menu():
    accounting_system = AccountingSystem()

    while True:
        print("--- Меню ---")
        print("1. Додати клієнта")
        print("2. Додати продукт")
        print("3. Додати заказ")
        print("4. Видалити клієнта")
        print("5. Видалити продукт")
        print("6. Подивитись всю інофрмацію")
        print("7. Вихід")
        choice = input("Виберіть дію (1-7): ")

        if choice == "1":
            name = input("Введіть ім'я клієнта: ")
            contact_info = input("Введіть контактну інформацію клієнта: ")
            client_id = input("Введіть ідентифікатор клієнта: ")
            client = Client(name, contact_info, client_id)
            accounting_system.add_client(client)
            print("Клієнт успішно додан.")
        elif choice == "2":
            name = input("Введіть назву продукта: ")
            description = input("Введіть опис продукта: ")
            price = float(input("Введіть ціну продукта: "))
            quantity = int(input("Введіть кількісь продукта: "))
            product_id = input("Введіть ідентифікатор продукта: ")
            product = Product(name, description, price, quantity, product_id)
            accounting_system.add_product(product)
            print("Продукт успішно додан.")
        elif choice == "3":
            order_id = input("Введіть ідентифікатор заказа: ")
            client_id = input("Введіть ідентифікатор клієнта: ")
            product_ids = input("Введіть ідентифікатори продуктов через кому: ").split(",")
            result = accounting_system.create_order(order_id, client_id, product_ids)
            print(result)
        elif choice == "4":
            client_id = input("Введіть ідентифікатор клієнта для видалення: ")
            result = accounting_system.remove_client(client_id)
            print(result)
        elif choice == "5":
            product_id = input("Введіть ідентифікатор продукта для видалення: ")
            result = accounting_system.remove_product(product_id)
            print(result)
        elif choice == "6":
            print(accounting_system)
        elif choice == "7":
            print("Вихід з програми.")
            break
        else:
            print("Не правильний вибір. Будь ласка введіть інформвцію ще раз.")


# Запуск
main_menu()