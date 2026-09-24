import shutil
import sys
from pathlib import Path

import pytest

ROT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROT / "verktoy"))

import kjerne  # noqa: E402


@pytest.fixture
def kopi(tmp_path, monkeypatch):
    """En kopi av data/ og docs/ som testen kan endre. Verktøyene peker dit."""
    shutil.copytree(ROT / "data", tmp_path / "data")
    shutil.copytree(ROT / "docs", tmp_path / "docs")
    monkeypatch.setattr(kjerne, "DATA", tmp_path / "data")
    monkeypatch.setattr(kjerne, "DOCS", tmp_path / "docs")
    return tmp_path


def erstatt(sti: Path, gammel: str, ny: str, antall: int = 1) -> None:
    tekst = sti.read_text(encoding="utf-8")
    assert tekst.count(gammel) >= antall, f"fant ikke {gammel!r} i {sti.name}"
    sti.write_text(tekst.replace(gammel, ny, antall), encoding="utf-8")
