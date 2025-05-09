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

async def worker(url: str):
    print(type(requests.get(url)))

async def main():
    print("Hello from concurrent-downloader!")
    result = await worker("https://edu.anarcho-copy.org/Programming%20Languages/Python/using-asyncio-python-understanding-asynchronous.pdf")
    print(read_url_file("README.md"))

if __name__ == "__main__":
    asyncio.run(main())
