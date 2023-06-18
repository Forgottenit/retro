import json
import os

# Load JSON data from file
with open('album_fixtures.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Filter and remove the "available_markets" field from each object
filtered_data = []
for item in data:
    # Remove "available_markets" from the album object
    item['fields'].pop('available_markets', None)

    # Remove "available_markets" from each track object
    for track in item['fields']['tracks']['items']:
        track.pop('available_markets', None)

    filtered_data.append(item)

# Create the filtered_albums folder
folder_path = 'filtered_albums'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Save the filtered data to a new JSON file
output_file = os.path.join(folder_path, 'filtered_album_fixtures.json')
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, ensure_ascii=False)

print("Filtered data saved to:", output_file)