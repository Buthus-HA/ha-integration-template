"""Constantes de l'intégration."""
from __future__ import annotations

import json
from datetime import timedelta
from pathlib import Path

DOMAIN = "mon_integration"
# Source unique de vérité : la version de manifest.json
VERSION: str = json.loads((Path(__file__).parent / "manifest.json").read_text(encoding="utf-8"))["version"]

DEFAULT_SCAN_INTERVAL = timedelta(minutes=30)
