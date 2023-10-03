import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook

hero_data = [
    {"id": 1, "mapi_id": 1, "name": "Miya", "liquidpedia_url": "Miya"},
    {"id": 2, "mapi_id": 2, "name": "Balmond", "liquidpedia_url": "Balmond"},
    {"id": 3, "mapi_id": 3, "name": "Saber", "liquidpedia_url": "Saber"},
    {"id": 4, "mapi_id": 4, "name": "Alice", "liquidpedia_url": "Alice"},
    {"id": 5, "mapi_id": 5, "name": "Nana", "liquidpedia_url": "Nana"},
    {"id": 6, "mapi_id": 6, "name": "Tigreal", "liquidpedia_url": "Tigreal"},
    {"id": 7, "mapi_id": 7, "name": "Alucard", "liquidpedia_url": "Alucard"},
    {"id": 8, "mapi_id": 8, "name": "Karina", "liquidpedia_url": "Karina"},
    {"id": 9, "mapi_id": 9, "name": "Akai", "liquidpedia_url": "Akai"},
    {"id": 10, "mapi_id": 10, "name": "Franco", "liquidpedia_url": "Franco"},
    {"id": 11, "mapi_id": 11, "name": "Bane", "liquidpedia_url": "Bane"},
    {"id": 12, "mapi_id": 12, "name": "Bruno", "liquidpedia_url": "Bruno"},
    {"id": 13, "mapi_id": 13, "name": "Clint", "liquidpedia_url": "Clint"},
    {"id": 14, "mapi_id": 14, "name": "Rafaela", "liquidpedia_url": "Rafaela"},
    {"id": 15, "mapi_id": 15, "name": "Eudora", "liquidpedia_url": "Eudora"},
    {"id": 16, "mapi_id": 16, "name": "Zilong", "liquidpedia_url": "Zilong"},
    {"id": 17, "mapi_id": 17, "name": "Fanny", "liquidpedia_url": "Fanny"},
    {"id": 18, "mapi_id": 18, "name": "Layla", "liquidpedia_url": "Layla"},
    {"id": 19, "mapi_id": 19, "name": "Minotaur", "liquidpedia_url": "Minotaur"},
    {"id": 20, "mapi_id": 20, "name": "Lolita", "liquidpedia_url": "Lolita"},
    {"id": 21, "mapi_id": 21, "name": "Hayabusa", "liquidpedia_url": "Hayabusa"},
    {"id": 22, "mapi_id": 22, "name": "Freya", "liquidpedia_url": "Freya"},
    {"id": 23, "mapi_id": 23, "name": "Gord", "liquidpedia_url": "Gord"},
    {"id": 24, "mapi_id": 24, "name": "Natalia", "liquidpedia_url": "Natalia"},
    {"id": 25, "mapi_id": 25, "name": "Kagura", "liquidpedia_url": "Kagura"},
    {"id": 26, "mapi_id": 26, "name": "Chou", "liquidpedia_url": "Chou"},
    {"id": 27, "mapi_id": 27, "name": "Sun", "liquidpedia_url": "Sun"},
    {"id": 28, "mapi_id": 28, "name": "Alpha", "liquidpedia_url": "Alpha"},
    {"id": 29, "mapi_id": 29, "name": "Ruby", "liquidpedia_url": "Ruby"},
    {"id": 30, "mapi_id": 30, "name": "Yi Sun Shin", "liquidpedia_url": "Yi Sun Shin"},
    {"id": 31, "mapi_id": 31, "name": "Moskov", "liquidpedia_url": "Moskov"},
    {"id": 32, "mapi_id": 32, "name": "Johnson", "liquidpedia_url": "Johnson"},
    {"id": 33, "mapi_id": 33, "name": "Cyclops", "liquidpedia_url": "Cyclops"},
    {"id": 34, "mapi_id": 34, "name": "Estes", "liquidpedia_url": "Estes"},
    {"id": 35, "mapi_id": 35, "name": "Hilda", "liquidpedia_url": "Hilda"},
    {"id": 36, "mapi_id": 36, "name": "Aurora", "liquidpedia_url": "Aurora"},
    {"id": 37, "mapi_id": 37, "name": "Lapu Lapu", "liquidpedia_url": "Lapu Lapu"},
    {"id": 38, "mapi_id": 38, "name": "Vexana", "liquidpedia_url": "Vexana"},
    {"id": 39, "mapi_id": 39, "name": "Roger", "liquidpedia_url": "Roger"},
    {"id": 40, "mapi_id": 40, "name": "Karrie", "liquidpedia_url": "Karrie"},
    {"id": 41, "mapi_id": 41, "name": "Gatotkaca", "liquidpedia_url": "Gatotkaca"},
    {"id": 42, "mapi_id": 42, "name": "Harley", "liquidpedia_url": "Harley"},
    {"id": 43, "mapi_id": 43, "name": "Irithel", "liquidpedia_url": "Irithel"},
    {"id": 44, "mapi_id": 44, "name": "Grock", "liquidpedia_url": "Grock"},
    {"id": 45, "mapi_id": 45, "name": "Argus", "liquidpedia_url": "Argus"},
    {"id": 46, "mapi_id": 46, "name": "Odette", "liquidpedia_url": "Odette"},
    {"id": 47, "mapi_id": 47, "name": "Lancelot", "liquidpedia_url": "Lancelot"},
    {"id": 48, "mapi_id": 48, "name": "Diggie", "liquidpedia_url": "Diggie"},
    {"id": 49, "mapi_id": 49, "name": "Hylos", "liquidpedia_url": "Hylos"},
    {"id": 50, "mapi_id": 50, "name": "Zhask", "liquidpedia_url": "Zhask"},
    {"id": 51, "mapi_id": 51, "name": "Helcurt", "liquidpedia_url": "Helcurt"},
    {"id": 52, "mapi_id": 52, "name": "Pharsa", "liquidpedia_url": "Pharsa"},
    {"id": 53, "mapi_id": 53, "name": "Lesley", "liquidpedia_url": "Lesley"},
    {"id": 54, "mapi_id": 54, "name": "Jawhead", "liquidpedia_url": "Jawhead"},
    {"id": 55, "mapi_id": 55, "name": "Angela", "liquidpedia_url": "Angela"},
    {"id": 56, "mapi_id": 56, "name": "Gusion", "liquidpedia_url": "Gusion"},
    {"id": 57, "mapi_id": 57, "name": "Valir", "liquidpedia_url": "Valir"},
    {"id": 58, "mapi_id": 58, "name": "Martis", "liquidpedia_url": "Martis"},
    {"id": 59, "mapi_id": 59, "name": "Uranus", "liquidpedia_url": "Uranus"},
    {"id": 60, "mapi_id": 60, "name": "Hanabi", "liquidpedia_url": "Hanabi"},
    {"id": 61, "mapi_id": 61, "name": "Change", "liquidpedia_url": "Change"},
    {"id": 62, "mapi_id": 62, "name": "Kaja", "liquidpedia_url": "Kaja"},
    {"id": 63, "mapi_id": 63, "name": "Selena", "liquidpedia_url": "Selena"},
    {"id": 64, "mapi_id": 64, "name": "Aldous", "liquidpedia_url": "Aldous"},
    {"id": 65, "mapi_id": 65, "name": "Claude", "liquidpedia_url": "Claude"},
    {"id": 66, "mapi_id": 66, "name": "Vale", "liquidpedia_url": "Vale"},
    {"id": 67, "mapi_id": 67, "name": "Leomord", "liquidpedia_url": "Leomord"},
    {"id": 68, "mapi_id": 68, "name": "Lunox", "liquidpedia_url": "Lunox"},
    {"id": 69, "mapi_id": 69, "name": "Hanzo", "liquidpedia_url": "Hanzo"},
    {"id": 70, "mapi_id": 70, "name": "Belerick", "liquidpedia_url": "Belerick"},
    {"id": 71, "mapi_id": 71, "name": "Kimmy", "liquidpedia_url": "Kimmy"},
    {"id": 72, "mapi_id": 72, "name": "Thamuz", "liquidpedia_url": "Thamuz"},
    {"id": 73, "mapi_id": 73, "name": "Harith", "liquidpedia_url": "Harith"},
    {"id": 74, "mapi_id": 74, "name": "Minsitthar", "liquidpedia_url": "Minsitthar"},
    {"id": 75, "mapi_id": 75, "name": "Kadita", "liquidpedia_url": "Kadita"},
    {"id": 76, "mapi_id": 76, "name": "Faramis", "liquidpedia_url": "Faramis"},
    {"id": 77, "mapi_id": 77, "name": "Badang", "liquidpedia_url": "Badang"},
    {"id": 78, "mapi_id": 78, "name": "Khufra", "liquidpedia_url": "Khufra"},
    {"id": 79, "mapi_id": 79, "name": "Granger", "liquidpedia_url": "Granger"},
    {"id": 80, "mapi_id": 80, "name": "Guinevere", "liquidpedia_url": "Guinevere"},
    {"id": 81, "mapi_id": 81, "name": "Esmeralda", "liquidpedia_url": "Esmeralda"},
    {"id": 82, "mapi_id": 82, "name": "Terizla", "liquidpedia_url": "Terizla"},
    {"id": 83, "mapi_id": 83, "name": "Xborg", "liquidpedia_url": "Xborg"},
    {"id": 84, "mapi_id": 84, "name": "Ling", "liquidpedia_url": "Ling"},
    {"id": 85, "mapi_id": 85, "name": "Dyrroth", "liquidpedia_url": "Dyrroth"},
    {"id": 86, "mapi_id": 86, "name": "Lylia", "liquidpedia_url": "Lylia"},
    {"id": 87, "mapi_id": 87, "name": "Baxia", "liquidpedia_url": "Baxia"},
    {"id": 88, "mapi_id": 88, "name": "Masha", "liquidpedia_url": "Masha"},
    {"id": 89, "mapi_id": 89, "name": "Wanwan", "liquidpedia_url": "Wanwan"},
    {"id": 90, "mapi_id": 90, "name": "Silvanna", "liquidpedia_url": "Silvanna"},
    {"id": 91, "mapi_id": 91, "name": "Cecilion", "liquidpedia_url": "Cecilion"},
    {"id": 92, "mapi_id": 92, "name": "Carmilla", "liquidpedia_url": "Carmilla"},
    {"id": 93, "mapi_id": 93, "name": "Atlas", "liquidpedia_url": "Atlas"},
    {
        "id": 94,
        "mapi_id": 94,
        "name": "Popol and Kupa",
        "liquidpedia_url": "Popol and Kupa",
    },
    {"id": 95, "mapi_id": 95, "name": "Yu Zhong", "liquidpedia_url": "Yu Zhong"},
    {"id": 96, "mapi_id": 96, "name": "Lou Yi", "liquidpedia_url": "Lou Yi"},
    {"id": 97, "mapi_id": 97, "name": "Benedetta", "liquidpedia_url": "Benedetta"},
    {"id": 98, "mapi_id": 98, "name": "Khaleed", "liquidpedia_url": "Khaleed"},
    {"id": 99, "mapi_id": 99, "name": "Barat", "liquidpedia_url": "Barat"},
    {"id": 100, "mapi_id": 100, "name": "Brody", "liquidpedia_url": "Brody"},
    {"id": 101, "mapi_id": 101, "name": "Yve", "liquidpedia_url": "Yve"},
    {"id": 102, "mapi_id": 102, "name": "Mathilda", "liquidpedia_url": "Mathilda"},
    {"id": 103, "mapi_id": 103, "name": "Paquito", "liquidpedia_url": "Paquito"},
    {"id": 104, "mapi_id": 104, "name": "Gloo", "liquidpedia_url": "Gloo"},
    {"id": 105, "mapi_id": 105, "name": "Beatrix", "liquidpedia_url": "Beatrix"},
    {"id": 106, "mapi_id": 106, "name": "Phoveus", "liquidpedia_url": "Phoveus"},
    {"id": 107, "mapi_id": 107, "name": "Natan", "liquidpedia_url": "Natan"},
    {"id": 108, "mapi_id": 108, "name": "Aulus", "liquidpedia_url": "Aulus"},
    {"id": 109, "mapi_id": 109, "name": "Aamon", "liquidpedia_url": "Aamon"},
    {"id": 110, "mapi_id": 110, "name": "Valentina", "liquidpedia_url": "Valentina"},
    {"id": 111, "mapi_id": 111, "name": "Edith", "liquidpedia_url": "Edith"},
    {"id": 112, "mapi_id": 112, "name": "Floryn", "liquidpedia_url": "Floryn"},
    {"id": 113, "mapi_id": 113, "name": "Yin", "liquidpedia_url": "Yin"},
    {"id": 114, "mapi_id": 114, "name": "Melissa", "liquidpedia_url": "Melissa"},
    {"id": 115, "mapi_id": 115, "name": "Xavier", "liquidpedia_url": "Xavier"},
    {"id": 116, "mapi_id": 116, "name": "Julian", "liquidpedia_url": "Julian"},
    {"id": 117, "mapi_id": 117, "name": "Fredrinn", "liquidpedia_url": "Fredrinn"},
    {"id": 118, "mapi_id": 118, "name": "Joy", "liquidpedia_url": "Joy"},
    {"id": 119, "mapi_id": 120, "name": "Arlott", "liquidpedia_url": "Arlott"},
    {"id": 120, "mapi_id": 121, "name": "Ixia", "liquidpedia_url": "Ixia"},
    {"id": 121, "mapi_id": 122, "name": "Nolan", "liquidpedia_url": "Nolan"},
]


TESTING_PURPOSES = [
    {"id": 39, "mapi_id": 39, "name": "Roger", "liquidpedia_url": "Roger"},
]

for i in range(len(hero_data)):
    print("START SCRAPING......", hero_data[i]["name"])
    MAPI_url = (
        "https://mapi.mobilelegends.com/hero/detail?id="
        + str(hero_data[i]["mapi_id"])
        + "&language=en"
    )
    MAPI_response = requests.get(MAPI_url)
    MAPI_data_response = MAPI_response.json()["data"]
    MAPI_skill = MAPI_data_response["skill"]["skill"]
    MAPI_skill_len = len(MAPI_skill)

    for j in range(len(MAPI_skill)):
        # Create a dictionary to hold the data
        if MAPI_skill[j]["name"] == "":
            data = {
                "id": hero_data[i]["id"],
                "hero_id": hero_data[i]["id"],
                "hero_name": hero_data[i]["name"],
                "skill_name": "N / A",
                "skill_img": "N / A",
                "lang": "en",
                "description": "N / A",
                "available": False,
            }
        else:
            data = {
                "id": hero_data[i]["id"],
                "hero_id": hero_data[i]["id"],
                "hero_name": hero_data[i]["name"],
                "skill_name": MAPI_skill[j]["name"],
                "skill_img": MAPI_skill[j]["icon"],
                "lang": "en",
                "description": MAPI_skill[j]["des"],
                "available": True,
            }

        # Create a Pandas DataFrame from the new data
        df_new = pd.DataFrame([data])

        # Read the existing data from the Excel file, if it exists
        try:
            df_existing = pd.read_excel("mobile_legends_skill.xlsx")
        except FileNotFoundError:
            df_existing = pd.DataFrame()

        # Concatenate the existing data with the new data
        df_combined = pd.concat([df_existing, df_new])

        # Write the combined data back to the Excel file
        df_combined.to_excel("mobile_legends_skill.xlsx", index=False)

    print("DONE SCRAPING => ", hero_data[i]["name"])

print("SUCCESFULLY SCRAPED ", len(hero_data), " skills.")
