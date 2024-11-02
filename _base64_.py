from base64 import b64encode

import psycopg2

with open('unnamed.png', 'rb') as f:
    base64_image = b64encode(f.read()).decode('utf-8')
#
conn = psycopg2.connect(
    dbname="django_null_db",
    user="postgres",
    password="1",
    host="localhost"
)
cursor = conn.cursor()

query = """
INSERT INTO apps_product (image)
VALUES (%s)
"""
cursor.execute(query, (base64_image,))

conn.commit()
cursor.close()
conn.close()
