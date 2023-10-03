# Mobile Legends Data Scraper

This Python script allows you to scrape Mobile Legends data, including heroes' images, IDs, roles, and skills. It simplifies the process of extracting essential information from the game for analysis, categorization, and further research.

## Features
**mole_scrape_heroes_images.py**
- **Hero Images**: The script retrieves high-quality images of Mobile Legends heroes, enabling visual representation and identification.

**mole_scrape_items.py**
- **Hero Images**: The script retrieves high-quality images of Mobile Legends items.

**mlbb_scrape_skills_mapi.py**
- **Hero Skills**: Gather comprehensive information about hero skills for detailed analysis and comparison, exported to xlsx in this format id, hero_id, hero_name, skill_name, skill_img, lang, description, available.

**mlbb_scrape_hero_mapi_liquidpedia_fandom.py**
- **Hero Data**: Gather comprehensive information about heroes, exported to xlsx in this format id, hero_id, hero_name, primary_role, secondary_role, durability, offense, control effect, difficulty, specialty_primary, specialty_seconday.

## Requirements

To run this script, make sure you have the following:

- Python 3.x installed on your machine.
- Required Python libraries, such as `requests`, `beautifulsoup4`, and `pandas`. You can install them using the following command:

  ```shell
  pip install requests beautifulsoup4 pandas
