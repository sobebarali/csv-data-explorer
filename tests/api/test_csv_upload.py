from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_upload_csv_success():
    headers = {"x-api-key": "segwise-sobebar"}
    response = client.post(
        "/csv/upload-csv",
        json={"csv_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSCtraqtnsdYd4FgEfqKsHMR2kiwqX1H9uewvAbuqBmOMSZqTAkSEXwPxWK_8uYQap5omtMrUF1UJAY/pub?gid=1439814054&single=true&output=csv"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json() == {"message": "CSV data uploaded successfully"}

def test_upload_csv_invalid_url():  
    headers = {"x-api-key": "segwise-sobebar"}
    response = client.post("/csv/upload-csv", json={"csv_url": "http://invalid-url.com/csv"}, headers=headers)
    assert response.status_code == 400
    assert "Error fetching CSV" in response.json()["detail"]
