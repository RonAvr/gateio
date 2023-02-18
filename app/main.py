import uvicorn
from fastapi import FastAPI
from app.controllers.routes import api_router
from fastapi.middleware.cors import CORSMiddleware
from managers.Extractor import Extractor
from time import sleep

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
        last_announcement: str = Extractor.get_last_announcement()
        while True:
            new_announcement = Extractor.get_last_announcement()
            if new_announcement != last_announcement:
                symbol = Extractor.get_symbol(new_announcement)
                if not not symbol:
                    pass
            sleep(10)
    except Exception as ex:
        print(ex)