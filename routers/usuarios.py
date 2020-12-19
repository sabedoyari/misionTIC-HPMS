from typing import Optional
from fastapi import APIRouter, HTTPException
from db import db_hoteles

router = APIRouter(
    tags = ["Hoteles"],
    prefix = "/Hoteles"
)

