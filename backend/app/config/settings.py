from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

class Settings(BaseModel):
    USE_AZURE: bool = os.getenv("USE_AZURE", "False").lower() == "true"
    AZURE_OPENAI_ENDPOINT: str | None = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_KEY: str | None = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_DEPLOYMENT: str | None = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    AZURE_SEARCH_ENDPOINT: str | None = os.getenv("AZURE_SEARCH_ENDPOINT")
    AZURE_SEARCH_API_KEY: str | None = os.getenv("AZURE_SEARCH_API_KEY")
    AZURE_SEARCH_INDEX: str = os.getenv("AZURE_SEARCH_INDEX", "medkb")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.2"))
    TOP_K: int = int(os.getenv("TOP_K", "5"))

settings = Settings()
