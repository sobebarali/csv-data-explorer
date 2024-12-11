import logging
from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
import requests
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import case


from src.modules.csv_module.models import CSVData
from src.database import get_db
from src.modules.auth_module.dependencies import get_api_key

from src.modules.csv_module.schemas import CSVUploadRequest, QueryDataRequest, PaginatedResponse

from src.modules.csv_module.service import process_csv_upload

router = APIRouter()

logger = logging.getLogger(__name__)

@router.post("/upload-csv")
async def upload_csv(request: CSVUploadRequest, db: Session = Depends(get_db), api_key: str = Depends(get_api_key)):
    try:
        logger.info(f"Received request to upload CSV from {request.csv_url}")

        errors = process_csv_upload(request.csv_url, db)

        if errors:
            raise HTTPException(status_code=400, detail={"message": "CSV data uploaded with some errors", "errors": errors})
        else:
            return {"message": "CSV data uploaded successfully"}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error fetching CSV: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/query-data", response_model=PaginatedResponse)
async def query_data(
    request: QueryDataRequest = Depends(),
    db: Session = Depends(get_db),
    api_key: str = Depends(get_api_key),
    limit: int = 10,
    offset: int = 0
):
    try:
        query = db.query(CSVData)

        # Apply filters
        if request.appid is not None:
            query = query.filter(CSVData.appid == request.appid)
        if request.name is not None:
            query = query.filter(CSVData.name.ilike(f"%{request.name}%"))
        if request.release_date is not None:
            query = query.filter(CSVData.release_date == request.release_date)
        if request.release_date_start is not None:
            query = query.filter(CSVData.release_date >= request.release_date_start)
            query = query.order_by(CSVData.release_date)
        if request.release_date_end is not None:
            query = query.filter(CSVData.release_date <= request.release_date_end)
            query = query.order_by(CSVData.release_date)
        if request.release_date_start is not None and request.release_date_end is not None:
            query = query.filter(CSVData.release_date >= request.release_date_start, 
                                 CSVData.release_date <= request.release_date_end)
            query = query.order_by(CSVData.release_date)
        if request.price is not None:
            query = query.filter(CSVData.price == request.price)
        if request.windows is not None:
            query = query.filter(CSVData.windows == request.windows)
        if request.mac is not None:
            query = query.filter(CSVData.mac == request.mac)
        if request.linux is not None:
            query = query.filter(CSVData.linux == request.linux)

        total = query.count()
        data = query.offset(offset).limit(limit).all()

        return PaginatedResponse(total=total, limit=limit, offset=offset, data=data)

    except Exception as e:
        logger.error(f"Error in query_data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

