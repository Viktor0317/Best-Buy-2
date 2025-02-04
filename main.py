import products
import store
from products import SecondItemHalfPrice, BuyTwoGetOneFree, PercentageDiscount

def start(best_buy):
    while True:
        print("\n-------- Store Menu --------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            # List all products
            print("\nAvailable Products:")
            for idx, product in enumerate(best_buy.get_all_products(), 1):
                print(f"{idx}. {product.show()}")
        elif choice == "2":
            # Show total amount in store
            print(f"\nTotal of {best_buy.get_total_quantity()} items in store")
        elif choice == "3":
            # Make an order
            shopping_list = []
            print("\nAvailable Products:")
            for idx, product in enumerate(best_buy.get_all_products(), 1):
                print(f"{idx}. {product.show()}")

            print("\nWhen you want to finish your order, enter an empty text.")
            while True:
                try:
                    product_idx = input("Which product # do you want? ")
                    if not product_idx:  # Empty input means user finished the order
                        break
                    product_idx = int(product_idx) - 1
                    if product_idx < 0 or product_idx >= len(best_buy.get_all_products()):
                        print("Invalid product number. Please try again.")
                        continue

                    quantity = int(input("What amount do you want? "))
                    product = best_buy.get_all_products()[product_idx]
                    shopping_list.append((product, quantity))
                    print("Product added to your list!")
                except (ValueError, IndexError):
                    print("Invalid input. Please try again.")

            try:
                total_price = best_buy.order(shopping_list)
                print(f"\nOrder completed! Total cost: ${total_price:.2f}")
            except ValueError as e:
                print(f"Error processing your order: {e}")
        elif choice == "4":
            # Quit
            print("Thank you for visiting Best Buy!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = SecondItemHalfPrice("Second Half Price!")
    third_one_free = BuyTwoGetOneFree("Third One Free!")
    thirty_percent = PercentageDiscount("30% Off!", discount_percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    # Start the user interface
    start(best_buy)

if __name__ == "__main__":
    main()
