import pandas as pd

def filter_csv(filepath, crop_name, year):
    df = pd.read_csv(filepath)
    df_filtered = df[(df["FORME_DE_PROPRIETATE"] == "Sector privat") & (df["TIME_PERIOD"] == year)].copy()
    nuts3_codes = {
        "Bihor": "RO111", "Bistrita-Nasaud": "RO112", "Cluj": "RO113",
        "Maramures": "RO114", "Satu Mare": "RO115", "Salaj": "RO116",
        "Alba": "RO121", "Brasov": "RO122", "Covasna": "RO123",
        "Harghita": "RO124", "Mures": "RO125", "Sibiu": "RO126",
        "Bacau": "RO211", "Botosani": "RO212", "Iasi": "RO213",
        "Neamt": "RO214", "Suceava": "RO215", "Vaslui": "RO216",
        "Braila": "RO221", "Buzau": "RO222", "Constanta": "RO223",
        "Galati": "RO224", "Tulcea": "RO225", "Vrancea": "RO226",
        "Arges": "RO311", "Calarasi": "RO312", "Dambovita": "RO313",
        "Giurgiu": "RO314", "Ialomita": "RO315", "Prahova": "RO316",
        "Teleorman": "RO317", "Ilfov": "RO322",
        "Dolj": "RO411", "Gorj": "RO412", "Mehedinti": "RO413",
        "Olt": "RO414", "Valcea": "RO415",
        "Arad": "RO421", "Caras-Severin": "RO422", "Hunedoara": "RO423",
        "Timis": "RO424",
    }
    df_filtered["NUTS_ID"] = df_filtered["REF_AREA"].map(nuts3_codes)
    df_final = df_filtered[["NUTS_ID", "REF_AREA", "OBS_VALUE"]].rename(
        columns={"REF_AREA": "county_name", "OBS_VALUE": f"{crop_name}_yield_{year}_kg_ha"}
    )
    df_final = df_final.sort_values("NUTS_ID")
    df_final.to_csv(f"data/{crop_name}_{year}.csv", index=False)

crop_data = {
    'wheat': 'Wheat_unfiltered',
    'sunflower': 'Sunflower_unfiltered',
    'barley': 'Barley_unfiltered',
    'maize': 'Maize_unfiltered'
}

years = [2021, 2024]

for crop_name, filename_stem in crop_data.items():
    filepath = f"Data/{filename_stem}.csv"
    for year in years:
        filter_csv(filepath, crop_name, year)