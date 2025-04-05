Analýza teplotných záznamov pomocou Pythonu

1. Úpvod
Analyzujeme teplotné záznamy za obdobie 30 dní. Údaje boli získané na simuláciu skutočných denných meraní teploty s priemerom 15°C a štandardnou odchýlkou ​​5°C, ale napísal som aj kód na generovanie náhodných údajov. Cieľom analýzy je získať dôležité štatistické charakteristiky, vizualizovať rozdelenie teplôt a určiť trend ich vývoja.

2. Použité metódy a nástroje
Program bol napísaný v jazyku Python s využitím knižníc NumPy, Pandas, Matplotlib, Seaborn a SciPy. Tieto nástroje umožnili efektívne spracovanie a vizualizáciu dát.

3. Spracovanie dát
Generované teplotné dáta boli uložené do tabuľky obsahujúcej 30 dní s príslušnými hodnotami teploty. Na týchto dátach boli vykonané nasledujúce štatistické výpočty:

- Priemerná teplota
- Medián
- Smerodajná odchýlka
- Rozptyl
- Náhodné generovanie údajov

4. Vizualizácia výsledkov
Na zobrazenie výsledkov boli použité tri hlavné grafy:

Histogram teplôt – zobrazuje frekvenciu výskytu jednotlivých hodnôt.

Čiarový graf teplotného trendu – znázorňuje priebeh denných teplôt, doplnený o trendovú priamku.

Boxplot – poskytuje informáciu o rozložení dát, mediáne a extrémnych hodnotách.

5. Záver:
Analýza ukázala, že teploty sa pohybujú okolo priemernej hodnoty 15°C s miernymi výkyvmi aj ľubovoľno. Trendová čiara označuje mierny nárast/pokles teploty počas určitého obdobia, čo sa dá len zriedka povedať, ak sú údaje náhodné

Tento program poskytuje základné nástroje na spracovanie meraných teplotných dát a môže byť ďalšie rozšírený o predikcie budúceho vývoja alebo hlbšie štatistické analýzy.
