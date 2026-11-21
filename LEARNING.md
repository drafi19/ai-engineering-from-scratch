# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission
Pindah karier ke AI. Target akhir: membangun **agent** dan **produk RAG**.
Belajar secepat mungkin — tanpa target mingguan, ambil sebanyak yang bisa.

Keputusan arah: mulai dari **dasar (Phase 0)**, bukan dari hasil placement.
Alasan: skor placement membuktikan pemahaman konsep, bukan pengalaman
membangun. Fondasi mau dibangun ulang supaya tidak bolong.

## Placement
- Date: 2026-11-21
- Score: 10/10 (Math & Statistics 2/2, Classical ML 2/2, Deep Learning 2/2, NLP & Transformers 2/2, Applied AI 2/2)
- Entry point (from quiz): Phase 14: Agent Engineering
- Entry point (chosen by learner): **Phase 0: Setup & Tooling**
- Pace: as fast as possible

## Path
| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Do | 16 |
| 1 | Math Foundations | Do | 23 |
| 2 | ML Fundamentals | Do | 26 |
| 3 | Deep Learning Core | Do | 15 |
| 4 | Computer Vision | Do | 27 |
| 5 | NLP — Foundations to Advanced | Do | 30 |
| 6 | Speech & Audio | Do | 18 |
| 7 | Transformers Deep Dive | Do | 14 |
| 8 | Generative AI | Do | 14 |
| 9 | Reinforcement Learning | Do | 13 |
| 10 | LLMs from Scratch | Do | 26 |
| 11 | LLM Engineering | Do | 19 |
| 12 | Multimodal AI | Do | 65 |
| 13 | Tools & Protocols | Do | 76 |
| 14 | Agent Engineering | Do | 55 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 34 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |

## Progress log
| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-11-21 | 00/01-dev-environment | 3/3 | Benar pada `Route` (required vs optional) dan exit code. Salah saat menelusuri `digits`/`parts` — mengira `.split()` menempel semua digit jadi "24181" dan `parts[0]` = 24181, padahal list `['24','18','1']` dan `parts[0]` = `'24'`. Juga salah exit code saat 3/4 (menjawab 0, seharusnya 1). Perlu diulang: cara kerja `.split()` tanpa argumen, dan kenapa `main()` mengembalikan non-zero saat gagal. |
| 2026-11-21 | 00/02-git-and-collaboration | 3/3 | Paham commit sebagai snapshot (bukan diff) dan branch sebagai pointer 41 byte. Satu koreksi: file untracked saat `checkout` tidak dikembalikan DAN tidak dihapus — tetap di disk. Dipraktikkan langsung di repo demo: fast-forward vs merge commit dua parent. Repo lokal masih shallow (5 commit), `git log` tidak bisa telusuri sejarah penuh sampai `git fetch --unshallow upstream`. |
| 2026-11-21 | 00/03-gpu-setup-and-cloud | 3/3 | GPU lokal nyata: GTX 1050, 2 GB VRAM, compute 6.1, torch 2.11.0+cu126. `gpu_check.py` jalan: CPU 0.790s vs GPU 0.658s = **1x speedup** (bukan 100x) karena VRAM kecil + overhead PCIe. Paham `synchronize()` untuk timing asinkron dan OOM bersifat biner. Koreksi: hitung 7B fp16 = 14 GB (bukan 14,7 — itu salah pakai 2,1 GB VRAM sebagai bytes/param). Perlu diingat: batas VRAM teoretis vs realistis (activations + CUDA context). |

## Review queue


## Session workflow (delegated to the tutor)

Standing instruction for every /learn session in this repo:

1. **Before teaching**, fetch upstream lesson updates:

```bash
git fetch upstream
git merge upstream/main
```

If it merges cleanly, continue. If it conflicts, stop and report the conflicting paths instead of forcing anything.

2. **After the lesson and quiz**, save progress as one commit:

```bash
git add -A
git commit -m "learn(<phase>): <lesson slug> - <score>"
git push
```

`LEARNING.md` **is tracked and must be committed** — it is the only backup of
this progress log. Never edit lesson files under `phases/`.