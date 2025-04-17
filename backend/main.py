from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

ALLOWED_CONTENT_TYPES = [
    "application/pdf",
    "text/plain"
]

app = FastAPI(
    title="TOS Analyser",
    description="A tool for analyzing Terms of Service documents.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "Welcome to the TOS Analyser API!"}

@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF and TXT files are allowed.")
    
    contents = await file.read()

    return {"filename": file.filename, "content_type": file.content_type, "size": len(contents)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)