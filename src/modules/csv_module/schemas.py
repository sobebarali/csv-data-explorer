from pydantic import BaseModel, Field, HttpUrl, field_validator, ConfigDict
from typing import Optional, List
from datetime import date

class CSVUploadRequest(BaseModel):
    csv_url: HttpUrl = Field(..., description="URL of the CSV file to upload")

    @field_validator('csv_url', mode='before')
    @classmethod
    def ensure_https(cls, v):
        if v.startswith('http://'):
            return v.replace('http://', 'https://', 1)
        return v

class QueryDataRequest(BaseModel):
    appid: Optional[int] = Field(None, ge=0, description="App ID must be a non-negative integer")
    name: Optional[str] = Field(None, max_length=100, description="Name must be at most 100 characters")
    release_date: Optional[date] = Field(None, description="Release date in the format YYYY-MM-DD")
    release_date_start: Optional[date] = Field(None, description="Release date greater than in the format YYYY-MM-DD")
    release_date_end: Optional[date] = Field(None, description="Release date less than in the format YYYY-MM-DD")
    required_age: Optional[int] = Field(None, ge=0, le=100, description="Required age must be between 0 and 100")
    price: Optional[float] = Field(None, ge=0.0, description="Price must be a non-negative float")
    dlc_count: Optional[int] = Field(None, ge=0, description="DLC count must be a non-negative integer")
    windows: Optional[bool] = Field(None, description="Indicates if Windows is supported")
    mac: Optional[bool] = Field(None, description="Indicates if Mac is supported")
    linux: Optional[bool] = Field(None, description="Indicates if Linux is supported")        

class CSVDataResponse(BaseModel):
    appid: int
    name: str
    release_date: date
    required_age: int
    price: float
    dlc_count: int
    about_the_game: str
    supported_languages: str
    windows: bool
    mac: bool
    linux: bool
    positive: int
    negative: int
    score_rank: int
    developers: str
    publishers: str
    categories: str
    genres: str
    tags: str

    model_config = ConfigDict(from_attributes=True)

class PaginatedResponse(BaseModel):
    total: int
    limit: int
    offset: int
    data: List[CSVDataResponse]
    



    
    
    