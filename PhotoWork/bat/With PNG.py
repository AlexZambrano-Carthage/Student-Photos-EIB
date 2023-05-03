import base64
import os
import csv

input_dir = 'C:\PhotoWork\PhotoConv'
output_file = 'C:\PhotoWork\Finish\Todaysss.csv'

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='|')
    writer.writerow(['Image Name', 'Base64 Data'])
    
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.gif')):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, 'rb') as img_file:
                img_data = img_file.read()
                base64_data = base64.b64encode(img_data).decode('utf-8')
                writer.writerow([os.path.splitext(filename)[0], base64_data])
    
print('Done!')
