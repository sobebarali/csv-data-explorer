from fastapi.testclient import TestClient
from src.main import app

import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

SEGWISE_API_KEY = os.getenv("SEGWISE_API_KEY")

client = TestClient(app)

def test_query_data_success():
    headers = {"x-api-key": SEGWISE_API_KEY}
    response = client.get("/csv/query-data", headers=headers)
    assert response.status_code == 200
    assert "data" in response.json()

def test_query_data_no_results():
    headers = {"x-api-key": SEGWISE_API_KEY}
    response = client.get("/csv/query-data", params={"appid": 9999}, headers=headers)
    assert response.status_code == 200
    assert response.json()["data"] == []

def test_query_data_by_appid():
    headers = {"x-api-key": SEGWISE_API_KEY}
    response = client.get("/csv/query-data", params={"appid": 20200}, headers=headers)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data[0]["name"] == "Galactic Bowling"

def test_query_data_by_name():
    headers = {"x-api-key": SEGWISE_API_KEY}
    response = client.get("/csv/query-data", params={"name": "Train Bandit"}, headers=headers)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data[0]["appid"] == 655370

def test_query_data_by_release_date():
    headers = {"x-api-key": SEGWISE_API_KEY}
    response = client.get("/csv/query-data", params={"release_date": "2020-07-23"}, headers=headers)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data[0]["name"] == "Henosisâ¢"

def test_query_data_by_release_date_range():
    headers = {"x-api-key": SEGWISE_API_KEY}
    start_date = "2017-10-12"
    end_date = "2021-11-17"
    
    response = client.get(
        "/csv/query-data", 
        params={"release_date_start": start_date, "release_date_end": end_date}, 
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()["data"]
    
    # Convert string dates to datetime objects for comparison
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    for item in data:
        item_date = datetime.strptime(item["release_date"], "%Y-%m-%d")
        assert start_date <= item_date <= end_date

def test_query_data_by_price():
    headers = {"x-api-key": SEGWISE_API_KEY}
    response = client.get("/csv/query-data", params={"price": 19.99}, headers=headers)
    assert response.status_code == 200
    data = response.json()["data"]
    for item in data:
        assert item["price"] == 19.99

def test_query_data_by_multiple_filters():
    headers = {"x-api-key": SEGWISE_API_KEY}
    response = client.get("/csv/query-data", params={"appid": 1362670, "name": "KHIO"}, headers=headers)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data[0]["release_date"] == "2020-07-24"
