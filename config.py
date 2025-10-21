# Leboncoin Scraper Configuration
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database Configuration
    DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'sqlite')  # sqlite, postgresql, mysql
    DATABASE_PATH = os.getenv('DATABASE_PATH', 'leboncoin_data.db')  # For SQLite

    # PostgreSQL Configuration (if using PostgreSQL)
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'leboncoin_db')
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')

    # Scraping Configuration
    RESPECT_ROBOTS_TXT = os.getenv('RESPECT_ROBOTS_TXT', 'true').lower() == 'true'
    MIN_DELAY_SECONDS = float(os.getenv('MIN_DELAY_SECONDS', '1.0'))
    MAX_DELAY_SECONDS = float(os.getenv('MAX_DELAY_SECONDS', '3.0'))
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '10'))

    # Default Search Parameters
    DEFAULT_LIMIT = int(os.getenv('DEFAULT_LIMIT', '100'))
    DEFAULT_CATEGORIES = os.getenv('DEFAULT_CATEGORIES', '2,9,15').split(',')  # Cars, Real Estate, IT

    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'leboncoin_scraper.log')

    # Export Configuration
    EXPORT_FORMAT = os.getenv('EXPORT_FORMAT', 'csv')  # csv, json, xlsx
    EXPORT_DIRECTORY = os.getenv('EXPORT_DIRECTORY', './exports/')

    # Leboncoin API Configuration
    BASE_URL = "https://www.leboncoin.fr"
    API_BASE_URL = "https://api.leboncoin.fr/finder/search"

    # User Agent Rotation
    ROTATE_USER_AGENTS = os.getenv('ROTATE_USER_AGENTS', 'true').lower() == 'true'

    # Category Mapping
    CATEGORIES = {
        1: "Véhicules",
        2: "Voitures", 
        3: "Motos",
        4: "Caravaning",
        5: "Utilitaires",
        6: "Equipement auto",
        7: "Nautisme",
        8: "Immobilier",
        9: "Ventes immobilières",
        10: "Locations",
        11: "Colocations",
        12: "Locations de vacances",
        13: "Bureaux & Commerces",
        14: "Multimedia",
        15: "Informatique",
        16: "Consoles & Jeux vidéo",
        17: "Image & Son",
        18: "Téléphonie",
        19: "Maison",
        20: "Ameublement",
        21: "Electroménager",
        22: "Arts de la table",
        23: "Décoration",
        24: "Linge de maison",
        25: "Bricolage",
        26: "Jardinage",
        27: "Vêtements",
        28: "Chaussures",
        29: "Accessoires & Bagagerie",
        30: "Montres & Bijoux",
        31: "Equipement bébé",
        32: "Vêtements bébé",
        33: "Loisirs",
        34: "DVD / Films",
        35: "CD / Musique", 
        36: "Livres",
        37: "Animaux",
        38: "Vélos",
        39: "Sports & Hobbies",
        40: "Instruments de musique",
        41: "Collection",
        42: "Jeux & Jouets",
        43: "Vins & Gastronomie",
        44: "Emploi",
        45: "Mode",
        46: "Autres",
        47: "Prestations de services",
        48: "Billetterie",
        49: "Evénements",
        50: "Cours particuliers",
        51: "Covoiturage"
    }

    @classmethod
    def get_database_url(cls):
        """Get database connection URL based on configuration"""
        if cls.DATABASE_TYPE == 'postgresql':
            return f"postgresql://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}@{cls.POSTGRES_HOST}:{cls.POSTGRES_PORT}/{cls.POSTGRES_DB}"
        elif cls.DATABASE_TYPE == 'sqlite':
            return f"sqlite:///{cls.DATABASE_PATH}"
        else:
            raise ValueError(f"Unsupported database type: {cls.DATABASE_TYPE}")
