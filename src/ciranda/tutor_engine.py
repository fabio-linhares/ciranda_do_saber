"""Motor Pedagógico de Tutoria: Simbiose Tutor IA e Monitor Humano."""

from dataclasses import dataclass
from typing import List
from ciranda.bncc_catalog import get_skill
from ciranda.clustering import MicroGroup


@dataclass
class LessonStep:
    step_number: int
    audio_narrative: str
    monitor_action: str
    student_task: str
    expected_duration_minutes: int


@dataclass
class LessonPlan:
    group_id: str
    skill_code: str
    skill_name: str
    student_names: List[str]
    steps: List[LessonStep]


class TutorSessionEngine:
    """Gera planos de aula interativos em áudio para o aparelho do microgrupo."""

    def generate_lesson_plan(self, group: MicroGroup) -> LessonPlan:
        skill = get_skill(group.target_skill)
        skill_desc = skill.description if skill else "Desenvolvimento de competência básica"
        names = [s.name for s in group.students]
        names_str = ", ".join(names)

        steps = [
            LessonStep(
                step_number=1,
                audio_narrative=(
                    f"Olá, pessoal! Bem-vindos à nossa Ciranda. Hoje nós vamos aprender juntos "
                    f"sobre {skill_desc.lower()}. {names_str}, estão prontos?"
                ),
                monitor_action="Acolha o grupo com um sorriso e garanta que todos tenham lápis e papel à mesa.",
                student_task="Responder oralmente e sentar em semicírculo ao redor do monitor.",
                expected_duration_minutes=5,
            ),
            LessonStep(
                step_number=2,
                audio_narrative=(
                    "Agora, vamos ao nosso desafio prático. Monitor, por favor, escreva na lousa "
                    "o nosso exemplo do dia e desenhe os elementos para os alunos contarem."
                ),
                monitor_action="Desenhe na lousa conforme a instrução de áudio e aponte para cada estudante.",
                student_task="Observar a lousa e anotar o padrão em seu caderno.",
                expected_duration_minutes=15,
            ),
            LessonStep(
                step_number=3,
                audio_narrative=(
                    "Muito bem! Agora cada um vai fazer a sua tentativa individual no papel. "
                    "Não tenham medo de errar, a Ciranda serve exatamente para aprendermos juntos!"
                ),
                monitor_action="Circule entre as crianças, tirando dúvidas pontuais sem dar a resposta pronta.",
                student_task="Resolver o exercício individual com o apoio dos colegas e do monitor.",
                expected_duration_minutes=20,
            ),
            LessonStep(
                step_number=4,
                audio_narrative=(
                    "Parabéns pelo esforço! Vocês completaram a rodada da Ciranda. "
                    "Monitor, por favor registre o progresso de cada um no aplicativo."
                ),
                monitor_action="Registrar no app se cada aluno atingiu a maestria do conceito.",
                student_task="Celebrar com o grupo e guardar os materiais.",
                expected_duration_minutes=5,
            ),
        ]

        return LessonPlan(
            group_id=group.group_id,
            skill_code=group.target_skill,
            skill_name=skill_desc,
            student_names=names,
            steps=steps,
        )
