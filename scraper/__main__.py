import os
import sys
import argparse
import getpass
from twitter_scraper import Twitter_Scraper

try:
    from dotenv import load_dotenv

    print("Loading .env file")
    load_dotenv()
    print("Loaded .env file\n")
except Exception as e:
    print(f"Error loading .env file: {e}")
    sys.exit(1)


def main():
    try:
        parser = argparse.ArgumentParser(
            add_help=True,
            usage="python scraper [option] ... [arg] ...",
            description="Twitter Scraper is a tool that allows you to scrape tweets from twitter without using Twitter's API.",
        )

        try:
            parser.add_argument(
                "--mail",
                type=str,
                default=os.getenv("TWITTER_MAIL"),
                help="Your Twitter mail.",
            )

            parser.add_argument(
                "--user",
                type=str,
                default=os.getenv("TWITTER_USERNAME"),
                help="Your Twitter username.",
            )

            parser.add_argument(
                "--password",
                type=str,
                default=os.getenv("TWITTER_PASSWORD"),
                help="Your Twitter password.",
            )

            parser.add_argument(
                "--headlessState",
                type=str,
                default=os.getenv("HEADLESS"),
                help="Headless mode? [yes/no]"
            )
        except Exception as e:
            print(f"Error retrieving environment variables: {e}")
            sys.exit(1)

        parser.add_argument(
            "-t",
            "--tweets",
            type=int,
            default=50,
            help="Number of tweets to scrape (default: 50)",
        )

        parser.add_argument(
            "-u",
            "--username",
            type=str,
            default=None,
            help="Twitter username. Scrape tweets from a user's profile.",
        )

        parser.add_argument(
            "-ht",
            "--hashtag",
            type=str,
            default=None,
            help="Twitter hashtag. Scrape tweets from a hashtag.",
        )

        parser.add_argument(
            "--bookmarks",
            action='store_true',
            help="Twitter bookmarks. Scrape tweets from your bookmarks.",
        )

        parser.add_argument(
            "-ntl",
            "--no_tweets_limit",
            nargs='?',
            default=False,
            help="Set no limit to the number of tweets to scrape (will scrap until no more tweets are available).",
        )

        parser.add_argument(
            "-l",
            "--list",
            type=str,
            default=None,
            help="List ID. Scrape tweets from a list.",
        )

        parser.add_argument(
            "-q",
            "--query",
            type=str,
            default=None,
            help="Twitter query or search. Scrape tweets from a query or search.",
        )

        parser.add_argument(
            "-a",
            "--add",
            type=str,
            default="",
            help="Additional data to scrape and save in the .csv file.",
        )

        parser.add_argument(
            "--latest",
            action="store_true",
            help="Scrape latest tweets",
        )

        parser.add_argument(
            "--top",
            action="store_true",
            help="Scrape top tweets",
        )

        args = parser.parse_args()

        USER_MAIL = args.mail
        USER_UNAME = args.user
        USER_PASSWORD = args.password
        HEADLESS_MODE= args.headlessState

        if USER_UNAME is None:
            USER_UNAME = input("Twitter Username: ")

        if USER_PASSWORD is None:
            USER_PASSWORD = getpass.getpass("Enter Password: ")

        if HEADLESS_MODE is None:
            HEADLESS_MODE - str(input("Headless?[Yes/No]")).lower()

        print()

        tweet_type_args = []

        if args.username is not None:
            tweet_type_args.append(args.username)
        if args.hashtag is not None:
            tweet_type_args.append(args.hashtag)
        if args.list is not None:
            tweet_type_args.append(args.list)
        if args.query is not None:
            tweet_type_args.append(args.query)
        if args.bookmarks is not False:
            tweet_type_args.append(args.query)

        additional_data: list = args.add.split(",")

        if len(tweet_type_args) > 1:
            print("Please specify only one of --username, --hashtag, --bookmarks, or --query.")
            sys.exit(1)

        if args.latest and args.top:
            print("Please specify either --latest or --top. Not both.")
            sys.exit(1)

        if USER_UNAME is not None and USER_PASSWORD is not None:
            scraper = Twitter_Scraper(
                mail=USER_MAIL,
                username=USER_UNAME,
                password=USER_PASSWORD,
                headlessState=HEADLESS_MODE
            )
            scraper.login()

            
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

            for candidates in candidates_grouped_name_split:
                candidates_query = "%20OR%20".join(candidates)
                scraper.scrape_tweets(
                    max_tweets=args.tweets,
                    no_tweets_limit= args.no_tweets_limit if args.no_tweets_limit is not None else True,
                    scrape_username=args.username,
                    scrape_hashtag=args.hashtag,
                    scrape_bookmarks=args.bookmarks,
                    scrape_query=f"({candidates_query})%20(%23eleksyon2025%2C%20OR%20%23halalan2025%2C%20OR%20%23phvote%2C%20OR%20%23phvote2025%2C%20OR%20%23nle2025%2C%20OR%20%23midtermelections2025%2C%20OR%20%23pilipinas2025)%20min_faves%3A10%20until%3A2025-05-10%20since%3A2024-05-10",
                    scrape_list=args.list,
                    scrape_latest=args.latest,
                    scrape_top=args.top,
                    scrape_poster_details="pd" in additional_data,
                )
            scraper.save_to_csv()
            if not scraper.interrupted:
                scraper.driver.close()
        else:
            print(
                "Missing Twitter username or password environment variables. Please check your .env file."
            )
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nScript Interrupted by user. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    sys.exit(1)


if __name__ == "__main__":
    main()
