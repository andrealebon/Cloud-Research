from dataclasses import dataclass

@dataclass
class Product:
    Category: str
    Service: str
    Title: str
    Ranking: int