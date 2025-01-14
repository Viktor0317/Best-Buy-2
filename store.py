from products import Product

class Store:

    def __init__(self, products):
        """Initializes the store with a list of products."""
        self.products = products

    def add_product(self, product):
        """Adds a new product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Returns the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """Returns a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """Processes an order from the shopping list and returns the total price."""
        total_price = 0.0

        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"Product {product.name} is not available in the store.")
            total_price += product.buy(quantity)

        return total_price


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))



if __name__ == "__main__":
    main()