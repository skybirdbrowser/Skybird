# SPDX-License-Identifier: GPL-3.0-or-later
"""Skybird — ponto de entrada.  python main.py   (ou scripts/run/run_skybird.bat / scripts/run/run_skybird.sh)"""
import sys

if getattr(sys, "frozen", False):
    # Versão instalada (sem console): grava mensagens e erros em um arquivo de log para diagnóstico.
    try:
        from skybird.paths import data_dir

        _log_dir = data_dir()
        _log_dir.mkdir(parents=True, exist_ok=True)
        sys.stdout = sys.stderr = open(_log_dir / "skybird.log", "w", encoding="utf-8", buffering=1)
    except OSError:
        pass

from skybird.app import run  # noqa: E402

if __name__ == "__main__":
    sys.exit(run())
