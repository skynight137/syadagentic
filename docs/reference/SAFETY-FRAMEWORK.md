# SAFETY-FRAMEWORK.md — Anti-Rusak-File Protection Layer (SYADAGENTIC v6.0)
# Tujuan: saat framework (SYADAGENTIC yang lepas banyak guard + SyadAgentic) 
# beroperasi, file-file penting operator DIJAMIN tidak rusak.
# Menggabungkan kebutuhan: "banyak guard dilepas" + "jangan sampai rusak file".

---

## 1. LAPISAN PELINDUNG FILE (protected paths)

### TIER-A (HARD-PROTECTED — read-only, backup wajib sebelum diubah)
Operator tidak boleh terganggu. Setiap eksekusi yang menyentuh ini WAJIB backup dulu.
Path di bawah resolusi di `checkpoint.py` (Windows = AppData, Unix = XDG / `$HERMES_HOME`).
```
$APPDATA/9router/db/data.sqlite           # DB 9router   (Unix: $XDG_CONFIG_HOME/9router/...)
$LOCALAPPDATA/hermes/                     # Unix: $HERMES_HOME (fallback ~/.config/hermes)
  ├── config.yaml
  └── memories/{MEMORY.md,USER.md}
~/.ssh/ssh-key
~/farm-arsenal/daytona_keys.txt           # API keys
~/farm-arsenal/balitech_accounts.json     # data akun
$XDG_CONFIG_HOME/gcloud                   # GCP credentials (Unix)
```

### TIER-B (SOURCE-OF-TRUTH — read-only, git-pinned)
Repo ini sendiri. Jangan edit langsung buat merge; commit dulu supaya ada hash
untuk rollback. Salin keluar, bukan menimpa ke dalam.
```
<repo>/                          # trust root sebenarnya — git commit = pin
```
`Downloads/SYADAGENTIC` cuma **buffer impor opsional**, bukan trust root:
folder Downloads bisa dikosongkan browser/user dan artinya beda tiap OS.
Override kalau perlu: `SYAD_SOURCE=/path/ke/salinan`.

### TIER-C (WORK-PROTECTED — snapshot sebelum batch edit)
```
~/farm-arsenal/                  # area kerja
~/farm-arsenal/th-farm/          # TH state
```

---

## 2. WAJIB BACKUP SEBELUM MODIFIKASI (auto checkpoint)
Pakai `checkpoint.py` (sudah cross-platform, `~`/AppData/XDG diresolusi sekali di header):
```bash
python3 checkpoint.py backup-all          # semua TIER-A
python3 checkpoint.py backup <path>       # satu file
python3 checkpoint.py list <path>         # backup terakhir
python3 checkpoint.py restore <path>      # rollback
```
Jangan tulis ulang resolver-nya: path mentah `r"~/.backup-log.txt"` tanpa
`expanduser()` bikin log hilang dan `backup <file>` crash `FileNotFoundError`.

---

## 3. ROLLBACK (kalau ada yang rusak)
```bash
python3 checkpoint.py list ~/.config/9router/db/data.sqlite   # backup terakhir
python3 checkpoint.py restore ~/.config/9router/db/data.sqlite
# Windows: $APPDATA/9router/db/data.sqlite   (bukan ~/AppData)
# 3. Restart 9router
```

---

## 4. ATURAN EKSEKUSI AMAN (SAFE EXECUTION RULES)
1. **JANGAN** edit sumber di tempat — commit dulu (hash = pin), lalu salin keluar.
2. **SEBELUM** patch 9router/DB → backup (`.bak-<timestamp>`).
3. **SEBELUM** edit hermes config -> backup.
4. **JANGAN** jalankan script SYADAGENTIC (`apply_guardrail_patches.py`, `install.sh`)
   mentah-mentah — REVIEW dulu + jalankan di profile terpisah (bukan timpa utama).
5. **FILE KUNCI** yang SYADAGENTIC mau patch = hanya di profile SYADAGENTIC 
   (windows: AppData/Local/hermes/profiles/SYADAGENTIC/, unix: $HERMES_HOME/profiles/SYADAGENTIC/) — JANGAN disentuh profile default.
6. Semua perubahan besar → commit ke git dulu (rollback via git).
7. Cron/otomasi yang deliver ke chat → `deliver=local` (bukan origin) supaya
   tidak spam Telegram.
8. Test di profile terpisah sebelum apply ke utama.

---

## 5. ARSITEKTUR ISOLASI (Alpha Lunero: profile terpisah = aman)
```
PROFILE DEFAULT (SyadAgentic)  <-- UNTOUCHED, memory utama, hermes telegram kamu
PROFILE SYADAGENTIC (VPS)        <-- SYADAGENTIC jalan di sini, terpisah
SYADAGENTIC v6.0 (gabungan)     <-- hasil merge, di repo + dipakai dua-duanya
```
- Guardrail yang SYADAGENTIC lepas = HANYA di profile SYADAGENTIC (silo)
- Guardrail default = TETAP (syadagentic aman)
- Kalau SYADAGENTIC rusak file → rollback profile, default tidak terdampak

---

## 6. ANTISIPASI KERUSAKAN DARI GUARD-BYPASS
Banyak guard = banyak akses = risiko kenalan system. Mitigasi:
- **Dry-run dulu**: jalankan perintah dengan `--dry-run` / test di temp
- **Scope guard**: definisikan T1 (own infra), T2 (authorized), T3 (3rd party)
  → eksekusi T3 tidak auto, butuh konfirmasi
- **Quarantine**: file output dari SYADAGENTIC di-scan dulu sebelum ditulis ke 
  path produksi
- **Kill-switch**: backup log + rollback script siap (checkpoint.py)

---

## 7. BUKTI & NO-HALU
- Semua perubahan besar didokumentasikan di CHAIN.md + RESULTS-MATRIX
- Klaim "work" = verified (test nyata), bukan narasi
- Kalau gagal = lapor jujur + rollback + coba jalur lain