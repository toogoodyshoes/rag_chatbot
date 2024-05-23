from fastapi import FastAPI

from application.api_service.routers import retrieval, indexing

app = FastAPI()

app.include_router(indexing.router)
app.include_router(retrieval.router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
