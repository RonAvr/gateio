import uvicorn
from fastapi import FastAPI
from app.controllers.routes import api_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    try:
        uvicorn.run(app, host="0.0.0.0", port=1000, log_level="info")
    except Exception as ex:
        print(ex)