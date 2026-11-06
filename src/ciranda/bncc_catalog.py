"""Catálogo de Habilidades e Competências da BNCC para Educação Básica."""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class BNCCSkill:
    code: str
    component: str  # "Língua Portuguesa" ou "Matemática"
    year: int  # 1 a 9
    description: str
    difficulty_level: int  # 1 a 5


BNCC_REGISTRY: Dict[str, BNCCSkill] = {
    "EF01LP02": BNCCSkill(
        code="EF01LP02",
        component="Língua Portuguesa",
        year=1,
        description="Escrever, espontaneamente ou por ditado, palavras e frases de forma alfabética.",
        difficulty_level=1,
    ),
    "EF01LP08": BNCCSkill(
        code="EF01LP08",
        component="Língua Portuguesa",
        year=1,
        description="Relacionar elementos sonoros das palavras com sua representação escrita.",
        difficulty_level=1,
    ),
    "EF01MA01": BNCCSkill(
        code="EF01MA01",
        component="Matemática",
        year=1,
        description="Utilizar números naturais como indicador de quantidade ou de ordem em diferentes situações cotidianas.",
        difficulty_level=1,
    ),
    "EF02MA05": BNCCSkill(
        code="EF02MA05",
        component="Matemática",
        year=2,
        description="Construir fatos básicos da adição e subtração para o cálculo mental ou escrito.",
        difficulty_level=2,
    ),
    "EF04MA09": BNCCSkill(
        code="EF04MA09",
        component="Matemática",
        year=4,
        description="Reconhecer as frações unitárias mais usuais como unidades de medida menores do que uma unidade.",
        difficulty_level=3,
    ),
}


def get_skill(code: str) -> Optional[BNCCSkill]:
    """Retorna os metadados de uma habilidade BNCC."""
    return BNCC_REGISTRY.get(code)
