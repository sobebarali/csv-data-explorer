import logging
from sqlalchemy.orm import Session
import pandas as pd
from src.modules.csv_module.models import CSVData
from src.modules.csv_module.utils import parse_date
from src.modules.csv_module.schemas import CSVDataResponse
import requests
from io import StringIO

logger = logging.getLogger(__name__)

def process_csv_upload(csv_url: str, db: Session):
    response = requests.get(csv_url)
    response.raise_for_status()
    csv_data = pd.read_csv(StringIO(response.text))
    errors = []

    try:
        for index, row in csv_data.iterrows():
            release_date = parse_date(row['Release date'])

            if release_date is None:
                raise ValueError(f"Date format for {row['Release date']} is not recognized")

            data = CSVDataResponse(
                appid=int(row['AppID']) if pd.notna(row['AppID']) else 0,
                name=row['Name'] if pd.notna(row['Name']) else "Unknown",
                release_date=release_date.strftime("%Y-%m-%d"),
                required_age=int(row['Required age']) if pd.notna(row['Required age']) else 0,
                price=float(row['Price']) if pd.notna(row['Price']) else 0.0,
                dlc_count=int(row['DLC count']) if pd.notna(row['DLC count']) else 0,
                about_the_game=row['About the game'] if pd.notna(row['About the game']) else "",
                supported_languages=row['Supported languages'] if pd.notna(row['Supported languages']) else "",
                windows=bool(row['Windows']) if pd.notna(row['Windows']) else False,
                mac=bool(row['Mac']) if pd.notna(row['Mac']) else False,
                linux=bool(row['Linux']) if pd.notna(row['Linux']) else False,
                positive=int(row['Positive']) if pd.notna(row['Positive']) else 0,
                negative=int(row['Negative']) if pd.notna(row['Negative']) else 0,
                score_rank=int(row['Score rank']) if pd.notna(row['Score rank']) else 0,
                developers=row['Developers'] if pd.notna(row['Developers']) else "",
                publishers=row['Publishers'] if pd.notna(row['Publishers']) else "",
                categories=row['Categories'] if pd.notna(row['Categories']) else "",
                genres=row['Genres'] if pd.notna(row['Genres']) else "",
                tags=row['Tags'] if pd.notna(row['Tags']) else ""
            )

            db_data = CSVData(**data.model_dump())
            db.add(db_data)

        # Commit only if all rows are processed successfully
        db.commit()
        logger.info("Successfully processed all rows")

    except (ValueError, IndexError, KeyError) as e:
        error_message = f"Error processing row {index}: {str(e)}"
        logger.error(error_message)
        errors.append(error_message)
        db.rollback()  # Rollback the transaction if any error occurs

    return errors
