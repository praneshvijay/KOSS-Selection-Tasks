import requests
import time

start_time = time.time()

for comic_id in range(1, 201):
    url = f"https://xkcd.com/{comic_id}/info.0.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        file_name = f"comic_{comic_id}.json"
        
        with open(file_name, "w") as file:
            file.write(response.text)
        
        print(f"Downloaded and saved JSON for comic {comic_id} to {file_name}")
    else:
        print(f"Failed to download JSON for comic {comic_id}")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")
