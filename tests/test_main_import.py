"""Importar el paquete localens no ejecuta la CLI ni mata el proceso (FIX-001)."""

from __future__ import annotations

import pkgutil

import localens
import localens.__main__  # noqa: F401 — regresión: importar no debe ejecutar la CLI


def test_walk_packages_sobre_localens_no_mata_el_proceso() -> None:
    modulos = [m.name for m in pkgutil.walk_packages(localens.__path__, prefix="localens.")]
    assert "localens.__main__" in modulos
    assert "localens.cli" in modulos