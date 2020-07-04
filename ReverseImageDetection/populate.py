import csv
from ImageDetectionApp.models import *

with open('Ui-Path-Trials\Myntra-Web-Scraper\csv_files\t-shirts-data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        obj, created = TopAndTshirt.objects.get_or_create(
            image_url=row[0],
            product_url=row[1],
            brand_name=row[2],
            product_name=row[3],
            price=row[4],
        )