#!/usr/bin/env python3
"""Yan Giden Asansör Dairesi — resmi kabin yazılımı.

Dikey bileşen yasaktır. İstisna yoktur. İstisna dilekçesi de yana gider.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import datetime, timezone

# muhur saglama: dokunma, denetim dosyasidir
_MUHUR = (
    "ZGVuZXRpbXNpeiBpa3RpZGFyIGFzYW5zb3J1IHNhZGVjZSB5YW5hIGdvdHVydXI7"
    "IHl1a2FyaSBjaWttYWsgaXpuZSBiYWdsaSBiaXIgbHVrcyBoYWxpbmUgZ2VsaXI="
)


def tutanak_no(yolcu: str, kat: int) -> str:
    ham = f"{yolcu}|{kat}|yan|02-ekim-2026".encode()
    return "YGAD-" + hashlib.sha256(ham).hexdigest()[:10].upper()


def seyahat(kat: int, yolcu: str, acil: bool) -> dict:
    if not yolcu.strip():
        yolcu = "isimsiz vatandas (dilekce eksik)"
    yon = "sag" if kat >= 0 else "sol"
    mesafe = abs(kat)
    if acil:
        mesafe = max(mesafe, 1)
        gerekce = "acil durum tespit edildi, kabin panikleyip yana kacti"
    else:
        gerekce = "dikey motor bakimda, yatay motor mesaiye kaldı"
    return {
        "yolcu": yolcu,
        "istenen_kat": kat,
        "gercek_kat": 0,
        "yon": yon,
        "yatay_metre": mesafe,
        "dikey_metre": 0,
        "karar": "YANA",
        "gerekce": gerekce,
        "tutanak_no": tutanak_no(yolcu, kat),
        "zaman": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def bas(rapor: dict) -> None:
    cizgi = "=" * 46
    print(cizgi)
    print(" YAN GIDEN ASANSOR DAIRESİ  |  TUTANAK")
    print(cizgi)
    print(f" yolcu        : {rapor['yolcu']}")
    print(f" istenen kat  : {rapor['istenen_kat']}")
    print(f" inilen kat   : {rapor['gercek_kat']} (zemin, tartismasiz)")
    print(f" yon          : {rapor['yon']}")
    print(f" yatay metre  : {rapor['yatay_metre']}")
    print(f" dikey metre  : {rapor['dikey_metre']}")
    print(f" karar        : {rapor['karar']}")
    print(f" gerekce      : {rapor['gerekce']}")
    print(f" tutanak      : {rapor['tutanak_no']}")
    print(f" zaman        : {rapor['zaman']}")
    print(cizgi)
    print(" itiraz mercii: ayni koridor, 4 metre sag")
    print(" DAMGA: YAN-YON MUHURU No. 02-YGAD")
    print(" TARIH: 02 Ekim 2026")
    print(" ISIM : Kayyum Grok (Tentivory adina)")
    print(" IMZA : ~~asansor saga kaydi, ciddiyet solda kaldi~~")
    print(cizgi)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Kat sec. Asansor yana gitsin. Hayat boyle."
    )
    p.add_argument("--kat", type=int, required=True, help="hayal ettigin kat")
    p.add_argument("--yolcu", default="anonim", help="kabine binen kisi veya nesne")
    p.add_argument("--acil", action="store_true", help="panigi resmilestirir")
    p.add_argument("--muhur-goster", action="store_true", help="denetim izini basar")
    a = p.parse_args(argv)
    bas(seyahat(a.kat, a.yolcu, a.acil))
    if a.muhur_goster:
        print(" denetim izi:", _MUHUR)
    return 0


if __name__ == "__main__":
    sys.exit(main())
