import requests

import asyncio


def read_url_file(file_path: str) ->list[str]:
    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()
    return [line for line in content.splitlines("\n") if line.strip()]

def read_stdin_urls(urls: list[str]):
    return urls

def _validate_url():
    ...

async def prepare_downloaders(urls: list[str]):
    # create tasks 
    for url in urls:
        _validate_url(url)
        async def downloader(process_url: str):
            file = requests.get(process_url)
        
        asyncio.create_task(downloader(url))
            
async def _validate_url(url: str):
    if url[3:] == "pdf":
        return url
    raise ValueError("Url not supported")

async def main():
    # print("Hello from concurrent-downloader!")
    # result = await worker("https://edu.anarcho-copy.org/Programming%20Languages/Python/using-asyncio-python-understanding-asynchronous.pdf")
    # print(read_url_file("README.md"))
    task = asyncio.create_task(worker("https://edu.anarcho-copy.org/Programming%20Languages/Python/using-asyncio-python-understanding-asynchronous.pdf"))
    await task

    await worker("https://edu.anarcho-copy.org/Programming%20Languages/Python/using-asyncio-python-understanding-asynchronous.pdf")

if __name__ == "__main__":
    asyncio.run(main())
