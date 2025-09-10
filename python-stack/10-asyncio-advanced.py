import asyncio

async def my_task():
    print("Асинхронная задача выполняется")

# get_event_loop позволяет проверить наличие event_loop в текущем потоке:
if asyncio.get_event_loop() is None:
    asyncio.set_event_loop(asyncio.new_event_loop())

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(my_task())
    event_loop.close()
