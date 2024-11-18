from bs4 import BeautifulSoup
import csv

html = """
<tr>
<td data-id="product-0">1</td>
<td data-id="name-1">Малина</td>
<td data-id="price-2">7694</td>
<td data-id="quantity-3">839</td>
<td data-id="category-4">Фрукты</td>
<td data-id="description-5">Является источником незаменимых аминокислот, необходимых для построения мышц.</td>
<td data-id="production-date-6">2022-01-22</td>
<td data-id="expiration-date-7">2030-03-21</td>
<td data-id="rating-8">1.93:</td>
<td data-id="status-9">Pending</td>
</tr>
"""

columns = ['product_id','name','price','quantity','category','description','production_date','expiration_date','rating','status']

to_float = ['price', 'rating']
to_int = ['product_id', 'quantity']

with open("./data/fifth_task.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

data = []

for row in soup.find_all("tr"):
    cols = row.find_all("td")
    item = {}

    column_index = 0
    for col in cols:
        val = col.get_text(strip=True)
        curr_column = columns[column_index]
        column_index += 1
        item[curr_column] = val

        if curr_column in to_float:
            item[curr_column] = float(val.replace(":", ""))
        elif curr_column in to_int:
            item[curr_column] = int(val)
    
    if len(item) > 0:
        data.append(item)

with open("./results/fifth_task_result.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, data[0].keys())
    writer.writeheader()
    for row in data:
        writer.writerow(row)