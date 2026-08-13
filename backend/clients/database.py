import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession, create_async_engine
from config.config import settings
from sqlalchemy import text

engine: AsyncEngine | None = None
session_factory: async_sessionmaker[AsyncSession] | None = None

def init_db_engine():
    global engine, session_factory
    engine = create_async_engine(settings.database_url)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)

async def close_db_engine():
    global engine, session_factory
    if engine is not None:
        await engine.dispose()
    engine = None
    session_factory = None

if __name__ == '__main__':
    init_db_engine()

    async def main():
        async with session_factory() as session:
            result = await session.execute(text("select 1"))
            print(result.fetchall())

    asyncio.run(main())
