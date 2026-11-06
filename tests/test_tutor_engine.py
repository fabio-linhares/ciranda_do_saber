"""Testes Unitários para a Geração do Plano de Tutoria e Simbiose IA-Monitor."""

import pytest
from ciranda.clustering import MicroGroup, StudentDiagnostic
from ciranda.tutor_engine import TutorSessionEngine


def test_generate_lesson_plan_contains_audio_and_monitor_steps():
    engine = TutorSessionEngine()

    group = MicroGroup(
        group_id="CIRANDA-G01",
        target_skill="EF01LP02",
        students=[
            StudentDiagnostic("A1", "Maria", {"EF01LP02": 0.2}),
            StudentDiagnostic("A2", "João", {"EF01LP02": 0.3}),
        ],
        assigned_device_id="DEV-01",
        assigned_monitor_name="Monitor Marcos",
    )

    plan = engine.generate_lesson_plan(group)

    assert plan.group_id == "CIRANDA-G01"
    assert plan.skill_code == "EF01LP02"
    assert "Maria" in plan.student_names
    assert "João" in plan.student_names
    assert len(plan.steps) == 4

    # Verificar se as falas em áudio e ações do monitor existem em todos os passos
    for step in plan.steps:
        assert step.audio_narrative != ""
        assert step.monitor_action != ""
        assert step.student_task != ""
        assert step.expected_duration_minutes > 0
