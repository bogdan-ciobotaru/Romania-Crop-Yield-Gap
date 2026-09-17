# Romania's Crop Yield Gap

A two-part data project on Romanian agricultural productivity: how Romania compares to its peers internationally, and how unevenly that performance is actually distributed within the country itself.

## Scope

The project evaluates four primary row crops: wheat, maize, barley, and sunflower seed. The analysis covers production data from 2014 through 2024. Part 1 establishes an international baseline, and Part 2 examines county-level yield variations across baseline and drought years.
## Project evolution

**Part 1** evaluates Romania's relative position within European and global agricultural systems using eleven years of FAOSTAT data. Production figures and financial yields in dollar terms are benchmarked against France, Germany, Ukraine, and the United States. National annual averages mask regional variance caused by distinct climatic and irrigation differences across Romanian regions.

**Part 2** Part 2 quantifies internal regional variations. For multiple crops, county-level yield gaps within Romania exceed the international yield deficit measured against Germany. In 2024, drought damage concentrated specifically within a distinct cluster of southeastern counties.

## Contents

- **[Part 1: The International Benchmark](Part%201/part1_README.md)**
SQL + Python pipeline analyzing FAOSTAT production and price data. Evaluates yield metrics, land productivity in dollar terms, 2022 production shifts, and 2024 regional drought impacts.
- **[Part 2: The County-Level Picture](Part%202/part2_README.md)**
QGIS + Python spatial workflow joining INS TEMPO county yield metrics with Eurostat NUTS3 boundaries to map internal spatial yield distributions.

## Tools across both parts

Python, pandas · SQLite (Part 1) · QGIS (Part 2) · matplotlib/seaborn (Part 1) · Jupyter Notebook (Part 1)

## Author

Ciobotaru Bogdan
