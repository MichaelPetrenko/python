import time
from turtle import pen

import asyncio

async def parser(sitename):
    for page in range(0, 10):
        print(sitename, page)
        await asyncio.sleep(2)

if __name__ == '__main__':
    start_time = time.time()
    parsers = [
        asyncio.ensure_future(parser(site))
        for site in ["site1", "site2", "site3"]
    ]
    print(parsers)
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.gather(*parsers))
    event_loop.close()

    print("--- %s seconds ---" % (time.time() - start_time))
