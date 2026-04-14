# siguriaetedhenave_gr10
Projekti nga lënda Siguria e të Dhënave dhe implementimi i Polybius Square Cipher dhe Myszkowski Transposition 

-- Pershkrimi i pjeses se Polybius Square
Ky projekt eshte nje program i thjeshte ne Python qe implementon Polybius Square, nje metode klasike e enkriptimit dhe dekriptimit te tekstit.
Programi mund te:
- Enkriptoje tekstin ne numra
- Dekriptoje numrat ne tekst origjinal

-- Si funksionon :
Programi perdor nje matrice 5x5 me shkronjat e alfabetit anglez (pa J):
A B C D E
F G H I K
L M N O P
Q R S T U
V W X Y Z

Rregulla:
- Çdo shkronje kthehet ne nje çift numrash (rreshti + kolona)
- Shembull:
  - A → 11
  - B → 12
  - I → 24
- Shkronja J zevendesohet me I
- Hapesirat kodohen si 00, ne menyre qe kur te dekriptohet teksti, keto hapesira te ruhen

--Enkriptimi: 
Funksioni encrypt(text):
- Merr tekstin si input
- E konverton ne shkronja te medha
- Zevendeson J me I
- Kthen çdo shkronje ne numerik sipas matrices
 Shembull: HELLO → 23 15 31 31 34

--Dekriptimi:
Funksioni decrypt(code):
- Merr kodin numerik si input
- E ndan ne pjese
- Kthen çdo çift ne shkronjen perkatese nga tabela
 Shembull: 23 15 31 31 34 → HELLO

-- Menuja e programit
Programi punon në mënyrë interaktive në terminal:
1. Enkriptimi tekstit
2. Dekriptimi kodit
3. Exit nga programi
--Ekzekutimi:
1. Hap terminalin
python polybiussquare.py
