# csv-data-explorer

## Live Demo
[https://csv-data-explorer.onrender.com](https://csv-data-explorer.onrender.com)

## Project Description
The `csv-data-explorer` is a web application designed to explore and query CSV data. It provides a user-friendly interface to search and display data from a CSV file using various filters.

## Features
- Search by App ID, Name, Release Date, and Price.
- Display results in a tabular format.
- Fetch data using a REST API with authentication via an API key.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: FastAPI
- **Database**: PostgreSQL
- **Containerization**: Docker

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- Docker
- PostgreSQL

### Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sobebarali/csv-data-explorer.git
   cd csv-data-explorer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the environment variables:**
   Create a `.env` file with the following variables:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/csv_explorer
   SEGWISE_API_KEY=your_secret_api_key
   ```

4. **Run migrations:**
   ```bash
   alembic upgrade head
   ```

5. **Run the application:**
   ```bash
   uvicorn src.main:app --reload --port 8000
   ```

6. **Build and run with Docker:**
   ```bash
   docker build -t data-explorer-api .
   docker run -p 8000:80 data-explorer-api
   ```

7. **Build and run with Docker Compose:**
   ```bash
   docker compose up --build
   ```

## API Documentation

### 1. Upload CSV
```bash
POST /csv/upload-csv
Content-Type: application/json
x-api-key: your_api_key

{
    "csv_url": "https://example.com/data.csv"
}
```

Response:
```json
{
    "message": "CSV data uploaded successfully"
}
```

### 2. Query Data
```bash
GET /csv/query-data?appid=730&name=Counter-Strike&release_date_start=2012-01-01&release_date_end=2023-12-31
x-api-key: your_api_key
```

Response:
```json
{
    "total": 1,
    "limit": 10,
    "offset": 0,
    "data": [
        {
            "appid": 730,
            "name": "Counter-Strike: Global Offensive",
            "release_date": "2012-08-21",
            "price": 0.00,
            "required_age": 18,
            "dlc_count": 0,
            "about_the_game": "...",
            "supported_languages": "English, French, German...",
            "windows": true,
            "mac": true,
            "linux": true
        }
    ]
}
```

## Production Costs (30 Days)

Based on the requirements (1 file upload and 100 queries per day) and using Render's pricing:

1. **Web Service (API)**:
   - Starter Instance ($7/month)
   - 512 MB RAM, 0.5 CPU
   - Sufficient for the given load

2. **PostgreSQL Database**:
   - Basic-1gb ($19/month)
   - 1 GB RAM, 0.5 CPU
   - Includes 1 GB storage
   - Additional storage at $0.30/GB/month

3. **Total Monthly Cost**: $26/month
   - Web Service: $7
   - Database: $19
   - Free features included:
     - SSL/TLS certificates
     - DDoS protection
     - Global CDN
     - Automatic deployments

This setup provides:
- 24/7 availability
- Automatic scaling
- Database backups
- Monitoring and logging
- Zero-downtime deployments

## Usage
- Access the application at `http://localhost:8000` in your web browser.
- Use the search form to query the CSV data.
- For API access, use the provided endpoints with your API key.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, please contact [sobebarali@gmail.com].
