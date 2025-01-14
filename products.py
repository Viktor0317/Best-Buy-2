from abc import ABC, abstractmethod

class Product:

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name can't be empty")
        if price < 0:
            raise ValueError("Price can't be negative")
        if quantity < 0:
            raise ValueError("Quantity can't be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> float:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Sets the quantity of the product.
        Deactivates the product if the quantity reaches 0."""
        if quantity < 0:
            raise ValueError("Quantity can't be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product"""
        self.active = False

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self) -> str:
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product.
        Updates the quantity and returns the total price."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available for purchase.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        pass

class PercentageDiscount(Promotion):
    def __init__(self, name: str, discount_percent: float):
        super().__init__(name)
        self.discount_percent = discount_percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        discount = product.price * (self.discount_percent / 100)
        return (product.price - discount) * quantity

class SecondItemHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)

class BuyTwoGetOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        paid_items = (quantity // 3) * 2 + (quantity % 3)
        return paid_items * product.price

class NonStockedProduct(Product):
    """A product that is not physical and does not track quantity."""

    def __init__(self, name: str, price: float):
        # Initialize with quantity set to zero
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        """Override to ensure quantity cannot be changed."""
        raise ValueError("Quantity cannot be set for non-stocked products.")

    def show(self) -> str:
        """Return a string representation of the non-stocked product."""
        return f"{self.name} (Non-Stocked), Price: {self.price}"


class LimitedProduct(Product):
    """A product that has a maximum purchase limit per order."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """Override to enforce maximum purchase limit."""
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} of {self.name} in one order.")
        return super().buy(quantity)

    def show(self) -> str:
        """Return a string representation of the limited product."""
        return f"{self.name} (Limited to {self.maximum} per order), Price: {self.price}, Quantity: {self.quantity}"


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    windows = NonStockedProduct("Windows License", price=125)
    shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())
    print(windows.show())
    print(shipping.show())

    bose.set_quantity(1000)
    print(bose.show())

if __name__ == "__main__":
    main()
