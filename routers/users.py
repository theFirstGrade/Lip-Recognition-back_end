from io import BytesIO
from starlette.responses import StreamingResponse
from fastapi import Response
from fastapi import APIRouter, Form, Depends, HTTPException, File
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
# import glob
# import os
# import cv2
import algorithms.code.Gabor_feature_extraction.Main as dog
import sys
import os

import zipfile

from fastapi.responses import StreamingResponse

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


class Data(BaseModel):
    filename: str


# @router.post("/uploadVideo",tags=["video"])
# async def upload(filename: Data):
#     print(filename)
#     return {"code": 200, "filename": filename}

imgCount = 1


def zipImage(i):
    zip_io = BytesIO()
    if i < 10:
        i = '0' + str(i)
    else:
        i = str(i)

    # z = zipfile.ZipFile("routers/test.zip", "w")
    # if os.path.exists('algorithms/code/store/2Features/czh/' + i + '.png'):
    #     z.write('algorithms/code/store/2Features/czh/' + i + '.png', i + '.png')
    #     z.write('algorithms/code/store/2Gabor/czh/' + i + '.jpg', i + '.jpg')
    #     z.write('algorithms/code/store/2mouth/czh/' + i + '.jpg', i + '.jpg')
    #     z.write('algorithms/code/store/2Sheet/czh/' + i + '.xls', i + '.xls')
    #
    # z.close()
    #
    # fileName = "routers/test.zip"
    # response = StreamingResponse(get_file_byte("xxx.jpg"), media_type="application/octet-stream")
    # response = response.headers["Content-Disposition"] = "attachment; filename=%s" % fileName
    # return response

    with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as z:
        if os.path.exists('algorithms/code/store/2Features/czh/' + str(i) + '.png'):
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            z.write('algorithms/code/store/2Features/czh/' + i + '.png', 'feature')
            z.write('algorithms/code/store/2Gabor/czh/' + i + '.jpg', 'gabor')
            z.write('algorithms/code/store/2mouth/czh/' + i + '.jpg', 'mouth')
            # z.write('algorithms/code/store/2Sheet/czh/' + i + '.xls', i + '.xls')
    return StreamingResponse(
        iter([zip_io.getvalue()]),
        media_type="application/x-zip-compressed",

        headers={"Content-Disposition": f"inline; filename=images.zip"}
    )


# for fpath in filenames:
#     # Calculate path for file in zip
#     fdir, fname = os.path.split(fpath)
#     zip_path = os.path.join(zip_subdir, fname)
#     # Add file, at correct path
#     temp_zip.write((fpath, zip_path))

# return StreamingResponse(
#     iter([zip_io.getvalue()]),
#     media_type="application/x-zip-compressed",
#     headers={"Content-Disposition": f"attachment; filename=images.zip"}
# )


def get_file_byte(filename, chunk_size=512):  # filename可以是文件，也可以是压缩包
    with open(filename, "rb") as f:
        while True:
            content = f.read(chunk_size)
            if content:
                yield content
            else:
                break


@router.post("/liveRecord")
async def liveRecord(file: bytes = File(...)):
    global imgCount
    # print(file)
    path = 'algorithms/code/store/2Picture/czh/' + str(imgCount) + '.jpg'
    with open(path, 'wb') as f:
        f.write(file)
    dog.aa(imgCount)
    # index = 0
    # if imgCount < 10:
    #     index = '0' + str(imgCount)
    # else:
    #     index = str(imgCount)
    imgCount = imgCount + 1
    #
    # file_like = open('algorithms/code/store/2mouth/czh/' + str(index) + '.jpg', mode="rb")
    # return StreamingResponse(file_like, media_type="image/jpg")

    return zipImage(imgCount - 1)
    # if file:
    #     return {'code': 200, 'data': zipImage(imgCount - 1)}
    # else:
    #     return {'code': 400}


@router.post("/uploadVideo")
async def uploadVideo(file: bytes = File(...)):
    print('Receiving')
    content = file
    path = 'a.mp4'
    with open(path, 'wb') as f:
        f.write(content)
    # dict = {
    #     'filesize': len(content)
    # }
    return {'code': 200}


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
        return {'code': 401, 'detail': 'wrong username or password'}
        # )

    if not user.password == password:
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="wrong username or password",
        return {'code': 401, 'detail': 'wrong username or password'}

    # )

    return {'user': user, 'code': 200}


if __name__ == '__main__':
    sys.path.append(os.path.dirname(sys.path[0]))
