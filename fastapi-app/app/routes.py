from fastapi import APIRouter, HTTPException
from app.models import Person, Mission
from app.db import people_db, mission_db

router = APIRouter()

# People endpoints
@router.get("/people")
async def get_people():
    return await people_db.get_all()

@router.post("/people/{id}")
async def create_or_update_person(id: str, person: Person):
    return await people_db.upsert(id, person)

@router.get("/people/{id}")
async def get_person(id: str):
    return await people_db.get(id)

@router.delete("/people/{id}")
async def delete_person(id: str):
    return await people_db.delete(id)

# Mission endpoints
@router.get("/mission")
async def get_missions():
    return await mission_db.get_all()

@router.post("/mission/{region}/{name}")
async def create_or_update_mission(region: str, name: str, mission: Mission):
    return await mission_db.upsert(region, name, mission)

@router.get("/mission/{region}/{name}")
async def get_mission(region: str, name: str):
    return await mission_db.get(region, name)

@router.delete("/mission/{region}/{name}")
async def delete_mission(region: str, name: str):
    return await mission_db.delete(region, name)
