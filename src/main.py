from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import debugpy
from typing import List
from .basic_chain import chain
from .rag import rag_main


app = FastAPI()
# Allow all origins for CORS (you can customize this based on your requirements)
origins = ["*"]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
debugpy.listen(("0.0.0.0", 5678))

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Read the content of your HTML file
    with open("./src/index.html", "r") as file:
        html_content = file.read()

    return HTMLResponse(content=html_content)


@app.get("/basic_chain/")
async def read_item(topic: str = "weather"):
    return chain.run(topic)


@app.get("/test_rag/")
async def test_rag(url: str = "https://python.langchain.com/docs/get_started/introduction"):
    return rag_main(url)




