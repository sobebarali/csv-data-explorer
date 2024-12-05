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
- **Database**: Postgr
- **Containerization**: Docker

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- Docker

### Installation

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
   - Copy the `.env.example` to `.env` and fill in the necessary environment variables.

4. **Run the application:**
   ```bash
   uvicorn src.main:app --reload
   ```

5. **Build and run with Docker:**
   ```bash
   docker build -t data-explorer-api .
   docker run -p 8000:80 data-explorer-api
   ```
6. **Build and run with Docker Compose:**
   ```bash
   docker compose up --build
   ```

## Usage
- Access the application at `http://localhost:8000` in your web browser.
- Use the search form to query the CSV data.

## API Endpoints
- **POST** `/csv/upload-csv`: Upload a CSV file.
- **GET** `/csv/query-data`: Query the CSV data with optional filters.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, please contact [sobebarali@gmail.com].
