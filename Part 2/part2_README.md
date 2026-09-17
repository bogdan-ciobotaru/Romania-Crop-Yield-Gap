# Romania's Crop Yield Gap

**Part 2: The County-Level Picture**

A QGIS choropleth follow-up to [Part 1: The International Benchmark](../part1/README.md).

Part 1 showed Romania trails Western Europe on average. Part 2 shows the nuance behind that national average.

## The Question

A national yield average obscures spatial performance variations across Romanian counties. This section evaluates county-level yield distributions for wheat, maize, barley, and sunflower seed in 2021 (a baseline year) and 2024 (a drought year).
## Scope

- **Crops:** wheat, maize, barley, sunflower seed
- **Geography:** Romania's 42 NUTS3 units. Bucharest municipality is excluded due to negligible agricultural output, leaving 41 counties.
- **Years:** 2021 (a baseline pre-shock year) and 2024 (a severe drought year).
- **Data:** county-level yield (kg/ha), private-sector farms, from Romania's National Institute of Statistics (INS TEMPO Online)

## The Maps

### Wheat

![Wheat yield by county, Romania, 2021](maps/Wheat%20Yield%20by%20County,%20Romania,%202021.png)
![Wheat yield by county, Romania, 2024](maps/Wheat%20Yield%20by%20County,%20Romania,%202024.png)

### Barley

![Barley yield by county, Romania, 2021](maps/Barley%20Yield%20by%20County,%20Romania,%202021.png)
![Barley yield by county, Romania, 2024](maps/Barley%20Yield%20by%20County,%20Romania,%202024.png)

### Maize

![Maize yield by county, Romania, 2021](maps/Maize%20Yield%20by%20County,%20Romania,%202021.png)
![Maize yield by county, Romania, 2024](maps/Maize%20Yield%20by%20County,%20Romania,%202024.png)

### Sunflower

![Sunflower yield by county, Romania, 2021](maps/Sunflower%20Yield%20by%20County,%20Romania,%202021.png)
![Sunflower yield by county, Romania, 2024](maps/Sunflower%20Yield%20by%20County,%20Romania,%202024.png)

## Key Findings

**Qualitative Agronomic Summary**

County-level crop yields reveal distinct spatial patterns shaped by soil geography, regional climate, and crop phenology. Southern and eastern counties contain highly fertile cernoziom soils that provide high natural yield potential. Winter crops, including wheat and barley, complete critical reproductive stages before peak midsummer stress, maintaining stable yields across both 2021 and 2024. Summer crops, such as maize and sunflower, depend directly on seasonal precipitation during summer grain filling. In 2021, adequate rainfall supported high summer crop yields nationwide. In 2024, severe atmospheric drought caused substantial yield reductions concentrated in the eastern and southeastern plains. Western counties maintained moderate productivity due to higher regional precipitation margins. Central Transylvanian counties show lower overall baseline yields for summer crops due to cooler thermal regimes, higher elevation, and less fertile soil profiles.

## Data & Method

- **Yield data:** [INS TEMPO Online](http://statistici.insse.ro/shop/?lang=ro), filtered to `Sector privat` (private-sector farms, for comparability with market-driven production) and the target year, via `Main.py`
- **County boundaries:** [Eurostat GISCO](https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics), NUTS 2024, 1:1M scale, filtered to Romania (`CNTR_CODE = 'RO'`)
- **Join key:** `NUTS_ID` (e.g. `RO111`), mapped by hand from county name to NUTS3 code in `Main.py`. Joining on the code rather than the Romanian county name avoids diacritics mismatches
- **Symbology:** Graduated, 5 classes, classified independently per crop. This classification enables direct year-to-year comparison within a crop and establishes independent scales across different crops.
- **Tools:** QGIS, Python, pandas

## Limitations & Caveats

- **Not a time series.** The 2021 and 2024 datasets isolate baseline spatial variation and drought impact.
- **Bucharest municipality is excluded.** The administrative unit contains no measurable crop yield.
- **Private sector only.** Data selection matches Part 1 parameters, excluding state-owned agricultural holdings. Figures represent private commercial farming performance.

## Repo contents

- `Main.py`: filters raw TEMPO exports to yield-by-county-by-year CSVs, joined to NUTS3 codes
- `data/`: raw TEMPO exports, the Eurostat NUTS3 shapefile, and the filtered per-crop-per-year CSVs
- `maps/`: the 8 exported choropleth maps
- `romania_crop_yields_counties.qgz`: the QGIS project file

## Sources

- National Institute of Statistics (INS), TEMPO Online
- Eurostat GISCO, NUTS territorial units
