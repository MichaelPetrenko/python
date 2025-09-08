import time

import asyncio

async def get_all_pages(sitename):
    await asyncio.sleep(2)
    return range(0, 10)

async def get_page_date(site_name, page):
    await asyncio.sleep(1)
    return "assfsd"

async def parser(site_name):
    pages = await get_all_pages(site_name)
    for page in pages:
        data = await get_page_date(site_name, page)

    return site_name

if __name__ == '__main__':
    start_time = time.time()
    parsers = [
        asyncio.ensure_future(parser(site))
        for site in ["site1", "site2", "site3"]
    ]
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.gather(*parsers))
    event_loop.close()

    print("--- %s seconds ---" % (time.time() - start_time))
