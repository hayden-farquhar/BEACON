"""Shared utilities for the traveller fever differential pipeline."""

from pathlib import Path
# Region and diagnosis constants
REGIONS = [
    "southeast_asia", "south_central_asia", "northeast_asia", "oceania",
    "sub_saharan_africa", "north_africa_middle_east", "latin_america_caribbean",
    "europe", "north_america",
]

DIAGNOSES = [
    "malaria_falciparum", "malaria_vivax", "dengue", "chikungunya", "zika",
    "enteric_fever", "acute_bacterial_gastroenteritis", "hepatitis_a",
    "hepatitis_b_acute", "hepatitis_e", "rickettsial_infection", "leptospirosis",
    "acute_hiv_seroconversion", "influenza", "covid_19", "measles",
    "japanese_encephalitis", "melioidosis", "tuberculosis", "schistosomiasis",
    "strongyloides_acute", "amoebiasis", "brucellosis", "q_fever", "mpox",
    "oropouche", "yellow_fever", "rabies", "community_acquired_pneumonia",
    "uti_pyelonephritis", "viral_urti", "infectious_mononucleosis",
    "undifferentiated_viral_syndrome",
]


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"
CLINICAL_DIR = DATA_DIR / "clinical_knowledge"

# Output directories
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"
SUPPLEMENTARY_DIR = OUTPUTS_DIR / "supplementary"


def ensure_dirs() -> None:
    """Create all data/output directories if they don't exist."""
    for d in [
        RAW_DIR / "geosentinel",
        RAW_DIR / "nndss",
        RAW_DIR / "promed_archive",
        RAW_DIR / "who_don_archive",
        INTERIM_DIR,
        PROCESSED_DIR,
        CLINICAL_DIR,
        FIGURES_DIR,
        TABLES_DIR,
        SUPPLEMENTARY_DIR,
    ]:
        d.mkdir(parents=True, exist_ok=True)
