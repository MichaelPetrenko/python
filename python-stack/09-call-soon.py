import asyncio

async def my_task():
    await asyncio.sleep(3)
    print("Асинхронная задача выполняется")

def callback():
    print("Callback function completed")

# Пример использования call_soon()
loop = asyncio.get_event_loop()
loop.call_soon(callback)
loop.call_soon(callback)
loop.call_soon(callback)
loop.run_until_complete(my_task())

# Пример использования call_later()
print("-----------------------")
loop = asyncio.get_event_loop()
loop.call_later(1, callback)
loop.run_until_complete(my_task())