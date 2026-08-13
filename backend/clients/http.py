import asyncio

from httpx import AsyncClient



# 如果同步， http_client = httpx.client()
http_client:AsyncClient |None = None


def init_http_client():
    global http_client
    http_client = AsyncClient()

async def close_http_client():
    global http_client
    if http_client:
        await http_client.aclose()


if __name__ == '__main__':
    init_http_client()
    async def main():
        response = await http_client.get('https://app04.hycdc.top/login')
        print(response.text)

        await close_http_client()
    asyncio.run(main())
