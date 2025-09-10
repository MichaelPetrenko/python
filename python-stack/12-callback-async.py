import time
import asyncio
import functools

def upper(future):
    print(future.result().upper())

def save_to_db(site, future):
    print("db", site, future.result())

def print_space(site, future):
    print("\n")

def save_to_minio(site, future):
    print("minio", site, future.result())

# И вызываем callback в функции
async def parser(site_name, future):
    await asyncio.sleep(2)
    print(site_name)
    future.set_result("data from " + site_name)

# Создаем Callback из функций save_to_db, save_to_minio,print_space
def get_callback(site):
    future = asyncio.Future()
    for callback in [save_to_db, save_to_minio, print_space]:
        future.add_done_callback(functools.partial(callback, site))
    return future

if __name__ == '__main__':
    start_time = time.time()

    # Далее создаем задачи, которые будут
    # выполняться асинхронно и передаем callback
    jobs = []
    for site in ["site1", "site2", "site3"]:
        jobs.append(asyncio.ensure_future(parser(site, get_callback(site))))
        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(asyncio.gather(*jobs))
        event_loop.close()

        print("--- %s seconds ---" % (time.time() - start_time))