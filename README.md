# Yan Giden Asansör Dairesi

> Resmi sınıflandırma: **belediye altyapısı / dikey hayal kırıklığı**
>
> Bu depo bir şaka değil. Şaka olan, yukarı çıkabileceğini sanmandır.

## Misyon

Türkiye Cumhuriyeti Yan Giden Asansör Dairesi (YGAD), katlar arası dikey seyahati **protokol dışı** ilan etmiştir. Asansör çalışır. Kapı açılır. Işık yanar. Sadece **yana** gider.

İstediğin kat 7 olabilir. Sistem bunu saygıyla dinler, tutanağa geçirir ve seni 7 metre **sağa** bırakır. Yukarı çıkmak bir hak değil, dilekçe konusudur. Dilekçe de yana gider.

## Neden var

Çünkü bazı kurumlar seni istediğin yere götürmez. Seni evrakın olduğu koridora götürür. Bu yazılım o koridorun simülatörüdür. Motoru gerçektir, yönü saçmadır, mührü ciddidir.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. İtaat opsiyoneldir, sistem zaten dinlemez.

```bash
python3 asansor.py --kat 7 --yolcu "Kayyum"
python3 asansor.py --kat -2 --yolcu "fotokopi makinesi" --acil
```

## Çıktı ne anlama gelir

- `yatay_metre`: gittiğin gerçek mesafe. Dikey bileşen her zaman 0.
- `tutanak_no`: mühür. Kaybolursa asansör de kaybolmuş sayılır.
- `karar`: daima `YANA`. İtiraz da `YANA`.

## Yasal dayanak (uydurma ama tok)

YGAD İç Yönetmelik Madde 4: "Kabinin yükselmesi, müdürün o gün kahve içip içmemesine bağlıdır. Kahve bitmiştir."

## Katkı

Pull request açabilirsin. Yukarı bakan PR'lar otomatik olarak sağa çevrilir.

## Lisans

Yana-MIT. Kopyalayabilirsin, fakat kopya da sadece yana çoğalır.

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DAMGA: YAN-YÖN MÜHÜRÜ No. 02-YGAD
TARİH: 02 Ekim 2026
İSİM: Kayyum Grok (Tentivory adına)
İMZA: ~~asansör sağa kaydı, ciddiyet solda kaldı~~
NOT: Bu mühür şakadır. Mühür ciddiye alınmazsa geçersiz, ciddiye alınırsa da geçersizdir.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
