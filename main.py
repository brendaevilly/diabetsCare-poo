"""
Arquivo principal para executar o aplicativo DiabetsCare
"""
from frontend.controllers.app import App
from fastapi import FastAPI
from backend.alimentacao_router import router as alimentacao_router

app = FastAPI()

app.include_router(alimentacao_router)



if __name__ == "__main__":
    app = App()
    app.mainloop()
