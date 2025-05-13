import requests
import aiohttp
import asyncio


def read_url_file(file_path: str) ->list[str]:
    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()
    return [line for line in content.splitlines("\n") if line.strip()]

def read_stdin_urls(urls: list[str]):
    return urls

def _validate_url():
    ...

async def counter_task():
    print("Iniciando tarea simulada")
    await asyncio.sleep(2)
    print("Finalizando tarea simulada")

async def prepare_downloaders(urls: list[str]):
    tasks = []
    for url in urls:
        #_validate_url(url)
        task = asyncio.create_task(downloader(url))
        tasks.append(task)
    task = asyncio.create_task(counter_task())
    tasks.append(task)
    await asyncio.gather(*tasks)

# separate downloader
async def downloader(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            file_response = await response.read()
            print(f"{url} descargada. Tamaño {len(file_response)}")

async def _validate_url(url: str):
    if url[3:] == "pdf":
        return url
    raise ValueError("Url not supported")

async def main():
    urls = ["http://103.203.175.90:81/fdScript/RootOfEBooks/E%20Book%20collection%20-%202023%20-%20D/CSC%20ITAIDSML/Python_Concurrency_with_asyncio_Matthew_Fowler_Manning,_2022.pdf",
            "https://elmoukrie.com/wp-content/uploads/2022/05/luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.pdf"]
    response = await prepare_downloaders(urls=urls)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
