from fastapi import FastAPI
from .database import Base, engine
from .routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(items.router)


# Código que se añaden a continuación para comprobar que la aplicación funciona correctamente
@app.get("/status")
def version():
    return {"status": "Robles Vidal, Diego - v.Xxx"}
