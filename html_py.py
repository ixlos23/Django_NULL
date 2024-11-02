with open('data.txt', 'r') as file:
    base64_image = file.read()

html_content = f'''
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Base64 Image</title>
</head>
<body>
    <h1>Base64 Rasm</h1>
    <img src="data:image/png;base64,{base64_image}" alt="Python Logo">
</body>
</html>
'''

# HTML faylini saqlash
with open('index.html', 'w') as html_file:
    html_file.write(html_content)
