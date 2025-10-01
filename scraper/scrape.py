import os
import sys
import argparse
import getpass
from twitter_scraper import Twitter_Scraper

candidates = ['Benhur Abalos', 'Jerome Adonis', 'Wilson Amad', 'Jocelyn Andamo', 'Bam Aquino', 'Ronnel Arambulo', 'Ernesto Arellano', 'Roberto Ballon', 'Abigail Binay', 'Jimmy Bondoc', 'Bong Revilla', 'Bonifacio Bosita', 'Arlene Brosas', 'Roy Cabonegro', 'Allen Capuyan', 'Teodoro Casiño', 'France Castro', 'Pia Cayetano', "David d'Angelo", 'Angelo de Alban', 'Leody de Guzman', 'Ronald dela Rosa', 'Mimi Doringo', 'Arnel Escobal', 'Luke Espiritu', 'Mody Floranda', 'Marc Gamboa', 'Bong Go', 'Norberto Gonzales', 'Jesus Hinlo Jr.', 'Gregorio Honasan', 'Relly Jose Jr.', 'Panfilo Lacson', 'Raul Lambino    PDP', 'Lito Lapid', 'Wilbert T. Lee', 'Amirah Lidasan', 'Rodante Marcoleta', 'Imee Marcos', 'Norman Marquez', 'Eric Martinez', 'Richard Mata', 'Sonny Matula', 'Liza Maza', 'Heidi Mendoza', 'Jose Montemayor Jr.', 'Subair Mustapha', 'Jose Olivar', 'Willie Ong', 'Manny Pacquiao', 'Francis Pangilinan', 'Ariel Querubin', 'Apollo Quiboloy', 'Danilo Ramos', 'Willie Revillame', 'Vic Rodriguez', 'Nur-Ana Sahidulla', 'Phillip Salvador', 'Tito Sotto', 'Michael Tapado', 'Francis Tolentino', 'Ben Tulfo', 'Erwin Tulfo', 'Mar Valbuena', 'Leandro Verceles Jr.', 'Camille Villar']
partylists = ['Nacionalista', 'DuterTen', 'PLM', 'Reform PH', 'Lakas', 'KANP', 'PPP', 'Liberal', 'Aksyon', 'NPC', 'PFP', 'DPP', 'PDP', 'KBL', 'Makabayan', 'KKK', 'Bunyog', 'PM', 'PDSP', 'Independent', 'WPP']

candidates_grouped = [candidates[i:i + 3] for i in range(0, len(candidates), 3)]
partylists_grouped = [partylists[i:i + 3] for i in range(0, len(partylists), 3)]

candidates_grouped_name_split = []

for candidate_group in candidates_grouped:
    c_group = []
    for candidate in candidate_group:
        name = candidate.split()
        for name_part in name:
            if len(name_part) > 3:
                c_group.append(name_part)
    candidates_grouped_name_split.append(c_group)

try:
    from dotenv import load_dotenv

    print("Loading .env file")
    load_dotenv()
    print("Loaded .env file\n")
except Exception as e:
    print(f"Error loading .env file: {e}")
    sys.exit(1)

# access
USER_UNAME = os.getenv("TWITTER_USERNAME")
USER_PASSWORD = os.getenv("TWITTER_PASSWORD")
HEADLESS_MODE = os.getenv("HEADLESS_MODE", "True").lower() in ("true", "1", "t", "yes")

scraper = Twitter_Scraper(
                mail=USER_UNAME,
                username=USER_UNAME,
                password=USER_PASSWORD,
                headlessState="yes"
            )

scraper.login()

for candidates in candidates_grouped_name_split:
    candidates_query = "%20OR%20".join(candidates)
    scraper.scrape_tweets(
        max_tweets=1000,
        # scrape_username="something",
        # scrape_hashtag="#",
        scrape_query=f"({candidates_query})%20(%23eleksyon2025%2C%20OR%20%23halalan2025%2C%20OR%20%23phvote%2C%20OR%20%23phvote2025%2C%20OR%20%23nle2025%2C%20OR%20%23midtermelections2025%2C%20OR%20%23pilipinas2025)%20min_faves%3A10%20until%3A2025-05-10%20since%3A2024-05-10",
        scrape_latest=True,
        scrape_poster_details=True,
    )
scraper.save_to_csv()
if not scraper.interrupted:
    scraper.driver.close()