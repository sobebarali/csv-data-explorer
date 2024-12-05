import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from modules.csv_module.router import router as csv
from src.config import SEGWISE_API_KEY

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = FastAPI()

# Include the CSV router
app.include_router(csv, prefix="/csv", tags=["csv"])

@app.get("/api-key")
async def get_api_key():
    try:
        if not SEGWISE_API_KEY:
            raise ValueError("API key is not set")
        
        print(SEGWISE_API_KEY)
        
        key = SEGWISE_API_KEY
        return {"api_key": key}
    except Exception as e:
        logging.error(f"Error retrieving API key: {e}")
        return {"error": "Failed to retrieve API key"}
    

# Serve static files
app.mount("/", StaticFiles(directory="public", html=True), name="public")


if __name__ == "__main__":
    import uvicorn
    import os
    
    port = int(os.getenv("PORT", default=8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

