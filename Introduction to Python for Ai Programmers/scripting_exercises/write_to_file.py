with open('./text.txt', 'w') as f:
  file_data = f.write('Hello World!')


with open('./text.txt', 'r') as f:
  file_data = f.read()
  print(file_data)
