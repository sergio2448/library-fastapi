from fastapi import FastAPI, Request
from app.v1.router.user_router import router as user_router
from app.v1.router.book_router import router as book_router
from app.v1.router.lending_router import router as lending_router
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


app = FastAPI()

@app.exception_handler(500)
async def internal_exception_handler(request: Request, exc: Exception):
  return JSONResponse(status_code=500, content=jsonable_encoder({"code": 500, "msg": "Internal Server Error"}))

app.include_router(user_router)
app.include_router(book_router)
app.include_router(lending_router)

