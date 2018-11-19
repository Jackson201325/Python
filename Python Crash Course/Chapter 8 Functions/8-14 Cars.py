def make_car(brand, model, **car_info):
    car = {}
    car['Brand'] = brand
    car['Model'] = model

    for key, value in car_info.items():
        car[key] = value

    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
