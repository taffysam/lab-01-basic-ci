def calculate_shipping(weight):
    if weight <= 5:
        return 50
    elif weight <= 10:
        return 100
    else:
        return 150


if __name__ == "__main__":
    print("Shipping Calculator")
    print(calculate_shipping(7))