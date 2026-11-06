"""Testes Unitários para o Mecanismo de Agrupamento Dinâmico (Clustering)."""

import pytest
from ciranda.clustering import AdaptiveClusterEngine, StudentDiagnostic


def test_clustering_groups_students_by_critical_skill():
    engine = AdaptiveClusterEngine(min_size=2, max_size=4)

    # 6 estudantes com diferentes perfis
    students = [
        StudentDiagnostic("A1", "Maria", {"EF01LP02": 0.2, "EF01MA01": 0.8}),
        StudentDiagnostic("A2", "João", {"EF01LP02": 0.3, "EF01MA01": 0.9}),
        StudentDiagnostic("A3", "Ana", {"EF01LP02": 0.1, "EF01MA01": 0.7}),
        StudentDiagnostic("A4", "Pedro", {"EF01LP02": 0.8, "EF01MA01": 0.2}),
        StudentDiagnostic("A5", "Lucas", {"EF01LP02": 0.9, "EF01MA01": 0.3}),
        StudentDiagnostic("A6", "Bia", {"EF01LP02": 0.7, "EF01MA01": 0.1}),
    ]

    devices = ["DEV-01", "DEV-02", "DEV-03"]
    monitors = ["Tia Cláudia", "Professor Carlos"]

    groups = engine.cluster_students(students, devices, monitors)

    assert len(groups) == 2

    # Grupo 1 deve focar em Língua Portuguesa
    lp_group = next(g for g in groups if g.target_skill == "EF01LP02")
    assert len(lp_group.students) == 3
    assert set(s.name for s in lp_group.students) == {"Maria", "João", "Ana"}
    assert lp_group.assigned_device_id == "DEV-01"
    assert lp_group.assigned_monitor_name == "Tia Cláudia"

    # Grupo 2 deve focar em Matemática
    ma_group = next(g for g in groups if g.target_skill == "EF01MA01")
    assert len(ma_group.students) == 3
    assert set(s.name for s in ma_group.students) == {"Pedro", "Lucas", "Bia"}
    assert ma_group.assigned_device_id == "DEV-02"
    assert ma_group.assigned_monitor_name == "Professor Carlos"


def test_clustering_handles_empty_students():
    engine = AdaptiveClusterEngine()
    assert engine.cluster_students([], [], []) == []
