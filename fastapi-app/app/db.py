from motor.motor_asyncio import AsyncIOMotorClient
import os
from app.models import Person, Mission

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["crew_scheduler"]

class PeopleDB:
    def __init__(self):
        self.collection = db["people"]

    async def get_all(self):
        return await self.collection.find().to_list(100)

    async def upsert(self, id: str, person: Person):
        await self.collection.update_one({"_id": id}, {"$set": person.dict()}, upsert=True)
        return {"message": "Upserted"}

    async def get(self, id: str):
        return await self.collection.find_one({"_id": id})

    async def delete(self, id: str):
        result = await self.collection.delete_one({"_id": id})
        return {"deleted": result.deleted_count}

class MissionDB:
    def __init__(self):
        self.collection = db["missions"]

    async def get_all(self):
        return await self.collection.find().to_list(100)

    async def upsert(self, region: str, name: str, mission: Mission):
        key = f"{region}:{name}"
        await self.collection.update_one({"_id": key}, {"$set": mission.dict()}, upsert=True)
        return {"message": "Upserted"}

    async def get(self, region: str, name: str):
        key = f"{region}:{name}"
        return await self.collection.find_one({"_id": key})

    async def delete(self, region: str, name: str):
        key = f"{region}:{name}"
        result = await self.collection.delete_one({"_id": key})
        return {"deleted": result.deleted_count}

people_db = PeopleDB()
mission_db = MissionDB()