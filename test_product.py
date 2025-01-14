import pytest
from products import Product


def test_create_normal_product():
    """Test that creating a product with valid details works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()


def test_create_product_invalid_details():
    """Test that creating a product with invalid details raises exceptions."""
    with pytest.raises(ValueError, match="Product name can't be empty"):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError, match="Price can't be negative"):
        Product("MacBook Air M2", price=-10, quantity=100)

    with pytest.raises(ValueError, match="Quantity can't be negative"):
        Product("MacBook Air M2", price=1450, quantity=-5)


def test_product_reaches_zero_quantity():
    """Test that when a product quantity reaches 0, it becomes inactive."""
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_correct_output():
    """Test that buying a product modifies its quantity and returns the correct price."""
    product = Product("MacBook Air M2", price=1450, quantity=10)
    total_price = product.buy(2)
    assert total_price == 2900  # 1450 * 2
    assert product.get_quantity() == 8


def test_buying_larger_quantity_than_exists():
    """Test that buying a larger quantity than exists raises an exception."""
    product = Product("MacBook Air M2", price=1450, quantity=5)

    with pytest.raises(ValueError, match="Not enough quantity available for purchase."):
        product.buy(10)
