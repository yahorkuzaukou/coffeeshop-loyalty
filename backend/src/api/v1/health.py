from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from core.db.db import get_session

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/db")
async def db(session: AsyncSession = Depends(get_session)):
    result = await session.execute(text("SELECT 1"))
    return {"status": "ok", "result": result.scalar()}