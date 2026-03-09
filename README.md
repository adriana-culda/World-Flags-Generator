# World-Flags-Generator

Acest proiect utilizează biblioteca **OpenCV** pentru a genera digital steagurile diferitelor țări prin manipularea pixelilor și aplicarea unor algoritmi geometrici. Spre deosebire de simpla afișare a unor imagini existente, acest script "construiește" steagurile direct în matricea de pixeli.

**Caracteristici**
* **Generare Algoritmică:** Steagurile sunt desenate prin iterații și condiții matematice (ex: pentru triunghiurile zimțate ale Bahrainului sau diagonalele Tanzaniei).
* **Geometrie Variată:** Include implementări pentru steaguri tricolore (verticale/orizontale), steaguri cu cruce (Islanda, Finlanda) și modele complexe (Congo, Tanzania).
* **Integrare Date:** Numele țărilor sunt citite dintr-un fișier extern `tari.txt`, asigurând o structură organizată.

**Logica de Programare**
Fiecare steag are o funcție dedicată care manipulează regiuni specifice din imagine (obiectul `imagine` de tip NumPy array):
* **Slicing de bază:** Folosit pentru steaguri simple (ex: România, Bulgaria).
* **Funcții matematice:** Utilizate pentru a crea forme geometrice complexe prin calcularea distanțelor și pantelor (ex: steagul Bahrainului folosește funcția `abs()` pentru a desena dinții de fierăstrău).

**Tehnologii utilizate**
* **Python**
* **OpenCV (cv2):** Pentru manipularea matricelor de culori și afișarea ferestrelor grafice.
* **NumPy:** Gestionarea eficientă a coordonatelor pixelilor.

**Cum funcționează?**
1. **Încărcarea:** Scriptul citește o imagine de bază (`imagine.jpg`) și o redimensionează la un format standard de **900x600**.
2. **Procesarea:** În funcție de selecție, se apelează funcția specifică (ex: `steag_Bahrain()`, `steag_Tanzania()`).
3. **Afișarea:** Rezultatul este randat instantaneu folosind `cv2.imshow`.

**Steaguri Incluse**
Proiectul acoperă o gamă largă de modele, printre care:
* **Simple:** România, Bulgaria, Benin, Cehia.
* **Cu Cruce:** Finlanda, Islanda, Georgia.
* **Complexe:** Bahrain (zig-zag), Tanzania (diagonale), Emiratele Arabe Unite.
