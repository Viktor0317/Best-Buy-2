
# Best Buy 2 Store Management System

## Overview
This is a project created as part of the Masterschool curriculum.

The Best Buy 2 Store Management System is a Python-based application for managing store inventory, processing customer orders, and applying promotional discounts. Designed with object-oriented principles, it provides a flexible and extensible structure for handling various types of products and promotions.

---

## Features

### Product Management
- Add, remove, and manage product inventory.
- Automatically deactivate products when inventory reaches zero.
- Support for various product types:
  - **Basic Products**: Standard products with price and inventory.
  - **Non-Stocked Products**: Products like software licenses that do not require inventory tracking.
  - **Limited Products**: Products with maximum purchase limits per order.

### Promotions
- Support for single promotions per product:
  - **Second Item Half Price**: Provides a 50% discount on every second item purchased.
  - **Buy Two, Get One Free**: Offers one free item for every two purchased.
  - **Percentage Discount**: Applies a percentage-based discount on the product's price.

### Store Management
- View all active products with their current inventory and promotions.
- Display total inventory across all products.
- Process customer orders with automatic application of promotions.

### User Interface
- Command-line interface with options to:
  - List all products.
  - Display total inventory.
  - Place orders.
  - Exit the program.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
Execute the `main.py` file to start the program:
```bash
python main.py
```

---

## Project Structure

```plaintext
Best Buy/
├── main.py          # Entry point for the application and user interface
├── products.py      # Product class and its variations
├── store.py         # Store class for managing inventory and orders
├── test_product.py  # Unit tests for product functionalities
```

---

## Usage

1. **Run the program**:
   ```bash
   python main.py
   ```
2. Follow the on-screen menu to:
   - List all products with promotions (if applied).
   - Show total inventory.
   - Place an order by selecting products and quantities.
   - Quit the program.

---

## Example

### Initial Inventory Setup:
```python
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    NonStockedProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Create promotion catalog
second_half_price = SecondItemHalfPrice("Second Half Price!")
third_one_free = BuyTwoGetOneFree("Third One Free!")
thirty_percent = PercentageDiscount("30% Off!", discount_percent=30)

# Assign promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)
```

### Sample Menu:
```plaintext
-------- Store Menu --------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number: 3
```

### Placing an Order:
```plaintext
Available Products:
1. MacBook Air M2, Price: $1450, Quantity: 100 (Promotion: Second Half Price!)
2. Bose QuietComfort Earbuds, Price: $250, Quantity: 500 (Promotion: Third One Free!)
3. Google Pixel 7, Price: $500, Quantity: 250

Which product # do you want? 1
What amount do you want? 2
Product added to your list!

Order completed! Total cost: $2175.00
```

---

## Testing

Unit tests are included to validate product functionality. To run the tests, use:
```bash
pytest test_product.py
```

---

## Author
**Nikola Brajkovic** - Initial development

---

## 🙏 Acknowledgments

Special thanks to Masterschool for providing the guidance and resources for this project.

