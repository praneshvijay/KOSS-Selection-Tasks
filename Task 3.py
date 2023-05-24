import aiohttp
import asyncio
import time


async def download_file(session, comic_id):
    url = f"https://xkcd.com/{comic_id}/info.0.json"
    async with session.get(url) as response:
        if response.status == 200:
            file_name = f"comic_{comic_id}.json"
            content = await response.text()
            with open(file_name, "w") as file:
                file.write(content)
            print(f"Downloaded and saved JSON for comic {comic_id} to {file_name}")
        else:
            print(f"Failed to download JSON for comic {comic_id}")


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for comic_id in range(1, 201):
            tasks.append(download_file(session, comic_id))
        
        start_time = time.time()

        await asyncio.gather(*tasks)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")


asyncio.run(main())
