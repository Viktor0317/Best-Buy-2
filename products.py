from abc import ABC, abstractmethod
from typing import Optional  # Used to indicate that a variable can be of a specified type or None

class Product:

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name can't be empty")
        if price < 0:
            raise ValueError("Price can't be negative")
        if quantity < 0:
            raise ValueError("Quantity can't be negative")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True
        self._promotion: Optional[Promotion] = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        """
        Sets the quantity of the product. Deactivates the product if quantity reaches 0.

        Args:
            value (int): The new quantity.

        Raises:
            ValueError: If the quantity is negative.
        """
        if value < 0:
            raise ValueError("Quantity can't be negative")
        self._quantity = value
        if self._quantity == 0:
            self.deactivate()

    @property
    def is_active(self) -> bool:
        return self._active

    def activate(self):
        """Activates the product."""
        self._active = True

    def deactivate(self):
        """Deactivates the product."""
        self._active = False

    @property
    def promotion(self) -> Optional["Promotion"]:
        return self._promotion

    @promotion.setter
    def promotion(self, promotion: "Promotion"):
        self._promotion = promotion

    def show(self) -> str:
        """Displays product details, including promotion if applicable."""
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.

        Args:
            quantity (int): The number of items to purchase.

        Returns:
            float: The total price for the purchase.

        Raises:
            ValueError: If quantity is invalid or exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available for purchase.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity
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
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    @property
    def quantity(self):
        raise ValueError("Quantity cannot be set for non-stocked products.")

    def show(self) -> str:
        return f"{self.name} (Non-Stocked), Price: {self.price}"

class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} of {self.name} in one order.")
        return super().buy(quantity)

    def show(self) -> str:
        return f"{self.name} (Limited to {self.maximum} per order), Price: {self.price}, Quantity: {self.quantity}"
