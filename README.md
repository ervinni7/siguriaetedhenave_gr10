# Siguria e të Dhënave — Gr. 10

Projekt nga lënda **Siguria e të Dhënave** që implementon dy algoritme klasike të kriptografisë në Python:

- `polybiussquare.py` — Polybius Square Cipher
- `mystransposition.py` — Myszkowski Transposition Cipher

---

## Si ekzekutohet programi

### Polybius Square

```bash
python polybiussquare.py
```

Programi hapet me një meny interaktive në terminal:

```
Zgjidhni një opsion::
1. Encrypt
2. Decrypt
3. Exit

Zgjedh:
```

Zgjidhni `1` për enkriptim, `2` për dekriptim, ose `3` për të dalë.

---

### Myszkowski Transposition

```bash
python mystransposition.py
```

Programi hapet me meny interaktive:

```
==================================================
   Myszkowski Transposition Cipher
==================================================

  Zgjidhni një opsion:
  1. Enkriptim
  2. Dekriptim
  3. Dilni
```

Zgjidhni `1` për enkriptim (kërkon tekst + çelës), `2` për dekriptim (kërkon ciphertext + çelës), ose `3` për të dalë.

---

## Përshkrimi i algoritmeve

### Polybius Square Cipher

Polybius Square është një metodë klasike e **zëvendësimit** (substitution cipher), ku çdo shkronjë e alfabetit zëvendësohet me dy shifra numerike që tregojnë pozicionin e saj në një matricë 5×5.

**Matrica:**

```
    1  2  3  4  5
1 [ A  B  C  D  E ]
2 [ F  G  H  I  K ]
3 [ L  M  N  O  P ]
4 [ Q  R  S  T  U ]
5 [ V  W  X  Y  Z ]
```

**Rregullat:**
- Çdo shkronjë → çift numrash (rresht + kolonë): `A → 11`, `H → 23`, `Z → 55`
- Shkronja **J** zëvendësohet me **I**
- Hapësirat kodifikohen si **`00`** për t'u ruajtur gjatë dekriptimit

---

### Myszkowski Transposition Cipher

Myszkowski Transposition është një metodë klasike e **transpozitimit** (transposition cipher), ku shkronjat e tekstit nuk zëvendësohen, por **rirenditen** sipas një çelësi teksti.

**Si funksionon:**
1. Teksti vendoset në rreshta brenda një rrjeti (grid), me numër kolonash = gjatësia e çelësit. Nëse teksti nuk e plotëson rreshtin e fundit, plotësohet me **X**.
2. Kolonat renditen alfabetikisht sipas çelësit. Kolonat me shkronjë të njëjtë lexohen bashkërisht.
3. Ciphertexti ndërtohet duke lexuar kolonat sipas rendit alfabetik.

---

## Shembuj të ekzekutimit

### Polybius Square — Enkriptim

```
Zgjedh: 1
Shkruaj tekstin qe doni ta enkriptoni: HELLO WORLD
Encrypted: 23 15 31 31 34 00 52 34 42 31 14
```

### Polybius Square — Dekriptim

```
Zgjedh: 2
Shkruaj tekstin qe doni ta dekriptoni: 23 15 31 31 34 00 52 34 42 31 14
Decrypted: HELLO WORLD
```

---

### Myszkowski Transposition — Enkriptim

```
Zgjedh: 1
Teksti origjinal  : HELLO WORLD
Çelësi            : MAMMA

  Rrjeti i enkriptimit:
      M   A   M   M   A
     (2) (1) (2) (2) (1)
     --------------------
  1 | H   E   L   L   O
  2 | W   O   R   L   D

Teksti i enkriptuar: EOODHLLWRL
```

### Myszkowski Transposition — Dekriptim

```
Zgjedh: 2
Teksti i enkriptuar: ULRSLELMONXXISXIFNEXX
Çelësi             : BALLOON

  Rrjeti i enkriptimit:
      B   A   L   L   O   O   N
     (2) (1) (3) (3) (5) (5) (4)
     ----------------------------
  1 | S   U   L   M   I   F   I
  2 | L   L   O   N   N   E   S
  3 | E   R   X   X   X   X   X

Teksti i dekriptuar: SULMIFILLONNESER
```

---

## Struktura e projektit

```
siguriaetedhenave_gr10/
├── polybiussquare.py    # Polybius Square Cipher
├── mystransposition.py  # Myszkowski Transposition Cipher
├── README.md            # Dokumentacioni
└── LICENSE
```

---

## Autorët
Ernesa Mavraj
Euron Ademaj
Ervin Nimani
