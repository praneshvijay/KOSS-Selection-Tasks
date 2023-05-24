import aiohttp
import asyncio
import time


async def download_page(page):
    url = f"https://reqres.in/api/users?page={page}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.text()


async def main():
    arr = [1, 2, 3]
    tasks = [download_page(el) for el in arr]

    start = time.time()

    await asyncio.gather(*tasks)

    time_taken = time.time() - start
    print(f"Time Taken: {time_taken}")


asyncio.run(main())
