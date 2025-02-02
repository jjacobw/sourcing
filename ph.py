from producthunt import ProductHunt
api_key = 'YOUR_API_KEY_HERE'
ph = ProductHunt(api_key)



daily_products = ph.get_daily()
for product in daily_products:
    print(f"ID: {product['ID']}")
    print(f"Name: {product['Name']}")
    print(f"Tagline: {product['Tagline']}")