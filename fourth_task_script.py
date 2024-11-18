import csv

def read_csv(path):
    data = []

    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'product_id': int(row['product_id']),
                'name': row['name'],
                'price': int(row['price']),
                'quantity': int(row['quantity']),
                'category': row['category'],
#                'description': row['description'],
                'production_date': row['production_date'],
                'expiration_date': row['expiration_date'],
                'rating': float(row['rating']),
                'status': row['status'],
            })
    
    return data

data = read_csv('./data/fourth_task.txt')

size = len(data)
avg_rating = 0
max_price = data[0]['price']
min_price = data[0]['price']

filtered_data = []

for item in data:
    avg_rating += item['rating']
    if max_price < item['price']:
        max_price = item['price']
    if min_price > item['price']:
        min_price = item['price']
    
    if item['price'] > 7910:
        filtered_data.append(item)

avg_rating /= size

with open("./results/fourth_task_result.txt", "w", encoding="utf-8") as file:
    file.write(f"{avg_rating}\n")
    file.write(f"{max_price}\n")
    file.write(f"{min_price}\n")

with open("./results/fourth_task_result.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, filtered_data[0].keys())
    writer.writeheader()
    for row in filtered_data:
        writer.writerow(row)