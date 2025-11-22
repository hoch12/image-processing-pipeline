# Parallel Image Processing Pipeline

**Autor:** Dominik Hoch  
**Škola:** SPŠE Ječná   
**Datum:** 2025  
**Popis:**  
Tento projekt je školní aplikace pro paralelní zpracování obrázků. Program načítá obrázky z adresáře `input/`, umožňuje jejich validaci a připravuje je pro další zpracování. Cílem projektu je ukázat schopnost práce s paralelními procesy a souběžným zpracováním dat.

## Struktura projektu
image-processing-pipeline/  
│   
├── docs/ ← dokumentace     
├── src/ ← zdrojové kódy  
├── tests/ ← unit testy     
├── input/ ← vstupní obrázky    
├── output/ ← výstupy zpracování    
└── README.md 

## Spuštění projektu
1. Stáhnout projekt z GitHub    

2. Nainstaloat potřebné balíčky

3.`python -m src.main --input input --output output --workers 4 --resize 800`    
**input** : Složka odkud se berou obrázky (vstup)    
**output** : Složka kam se nahrává csv a procesované obrázky (výstup)    
**workers** : Počet pracujících vláken   
**resize** : Nová velikost px původních obrázků