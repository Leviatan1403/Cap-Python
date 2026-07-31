import asyncio

from motor.motor_asyncio import AsyncIOMotorClient


async def main():
    client = AsyncIOMotorClient("mongodb://localhost:27017")

    db = client.store

    await db.users.insert_one({"name": "Juan", "email": "juan@mail.com"})

    user = await db.users.find_one({"name": "Juan"})

    print(user)

    client.close()


if __name__ == "__main__":
    asyncio.run(main())
