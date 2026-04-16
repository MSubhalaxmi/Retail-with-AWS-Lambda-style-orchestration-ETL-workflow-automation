def calculate_price(base_price, stock, demand):
    if stock < 10:
        surge = 1.2
    elif demand > 50:
        surge = 1.1
    else:
        surge = 1.0

    return round(base_price * surge, 2)