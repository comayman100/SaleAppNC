def load_categories():
    return [
        {
            "id" : 1,
            "name" : "Mobile"
        },
        {
            "id": 2,
            "name": "Tablet"
        },
        {
            "id": 3,
            "name": "LapTop"
        }
    ]

def load_products(kw = None):
    products = [
        {
            "id" : 1,
            "name": "iphone 15 pro max",
            "price" : 20000000,
            "img" : "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg"
        },
        {
            "id": 1,
            "name": "iphone 15 pro max",
            "price": 20000000,
            "img": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg"
        },
        {
            "id": 1,
            "name": "iphone 15 pro max",
            "price": 20000000,
            "img": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg"
        },
        {
            "id": 1,
            "name": "iphone 15 pro max",
            "price": 20000000,
            "img": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg"
        },
        {
            "id": 1,
            "name": "iphone 15 pro max",
            "price": 20000000,
            "img": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg"
        },
        {
            "id": 1,
            "name": "ipad pro 2023",
            "price": 20000000,
            "img": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg"
        },
        {
            "id": 1,
            "name": "iphone 15 pro max",
            "price": 20000000,
            "img": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg"
        },
        {
            "id": 1,
            "name": "iphone 15 pro max",
            "price": 20000000,
            "img": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg"
        }
    ]
    if kw:
        products = [p for p in products if p["name"].find(kw) >= 0]

    return products