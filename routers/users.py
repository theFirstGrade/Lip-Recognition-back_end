from fastapi import APIRouter, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

import sys
import os

from sql_app.database import SessionLocal
from sql_app.models import User
from sql_app import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users/", tags=["users"])
async def read_user():
    return [{"username": "zhangsan"}, {"username": "lisi"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "zhangsan"}


@router.post("/login")
async def login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    # 首先校验用户信息
    print(email)
    print(password)
    # user = db.get(username)
    user = crud.get_user_by_email(db, email)
    if not user:
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="wrong username or password",
        return {'code': 401}
        # )

    if not user.password == password:
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="wrong username or password",
        return {'code': 401}

    # )

    return {'user': user, 'code': 200}


if __name__ == '__main__':
    sys.path.append(os.path.dirname(sys.path[0]))
