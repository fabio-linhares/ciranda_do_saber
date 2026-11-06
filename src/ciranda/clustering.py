"""Algoritmo de Agrupamento Dinâmico (Adaptive Micro-Clustering).

Divide turmas de contraturno em microgrupos homogêneos por lacuna cognitiva
para atendimento em dispositivos comunitários com monitor.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import math


@dataclass
class StudentDiagnostic:
    student_id: str  # Token pseudonimizado (LGPD)
    name: str  # Primeiro nome ou apelido
    skill_scores: Dict[str, float]  # Código BNCC -> score (0.0 a 1.0)

    @property
    def critical_skill(self) -> str:
        """Identifica a habilidade mais deficitária (menor score)."""
        if not self.skill_scores:
            return "EF01LP02"
        return min(self.skill_scores.items(), key=lambda kv: kv[1])[0]


@dataclass
class MicroGroup:
    group_id: str
    target_skill: str
    students: List[StudentDiagnostic] = field(default_factory=list)
    assigned_device_id: Optional[str] = None
    assigned_monitor_name: Optional[str] = None

    @property
    def size(self) -> int:
        return len(self.students)


class AdaptiveClusterEngine:
    def __init__(self, min_size: int = 2, max_size: int = 4):
        self.min_size = min_size
        self.max_size = max_size

    def cluster_students(
        self,
        students: List[StudentDiagnostic],
        available_devices: List[str],
        available_monitors: List[str],
    ) -> List[MicroGroup]:
        """Agrupa estudantes pela habilidade prioritária comum em microgrupos de 2 a 4."""
        if not students:
            return []

        # 1. Particionar estudantes pela habilidade crítica
        by_skill: Dict[str, List[StudentDiagnostic]] = {}
        for s in students:
            skill = s.critical_skill
            by_skill.setdefault(skill, []).append(s)

        groups: List[MicroGroup] = []
        group_counter = 1

        for skill, skill_students in by_skill.items():
            # Ordenar por score relativo para refinar homogeneidade
            skill_students.sort(key=lambda s: s.skill_scores.get(skill, 0.0))

            total = len(skill_students)
            # Calcular fatiamento em blocos de até max_size
            num_chunks = max(1, math.ceil(total / self.max_size))
            chunk_size = math.ceil(total / num_chunks)

            for i in range(0, total, chunk_size):
                chunk = skill_students[i : i + chunk_size]
                device = (
                    available_devices.pop(0) if available_devices else f"DEV-TEMP-{group_counter}"
                )
                monitor = (
                    available_monitors.pop(0)
                    if available_monitors
                    else f"Monitor Voluntário #{group_counter}"
                )

                group = MicroGroup(
                    group_id=f"CIRANDA-G{group_counter:02d}",
                    target_skill=skill,
                    students=chunk,
                    assigned_device_id=device,
                    assigned_monitor_name=monitor,
                )
                groups.append(group)
                group_counter += 1

        return groups
