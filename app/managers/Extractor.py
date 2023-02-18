import random
import requests
import string
import time
from ..utils.Announcements import Announcements

class Extractor:

    last_scrapped_announcement: str = ""

    def get_queries(self):
        rand_page_size = random.randint(1, 50)
        letters = string.ascii_letters
        random_string = "".join(random.choice(letters) for i in range(random.randint(10, 20)))
        random_number = random.randint(1, 99999999999999999999)
        # queries = [
        #     "type=1",
        #     "catalogId=48",
        #     "pageNo=1",
        #     f"pageSize={str(rand_page_size)}",
        #     f"rnd={str(time.time())}",
        #     f"{random_string}={str(random_number)}",
        # ]
        queries = [
            "type=1",
            "catalogId=48",
            "pageNo=1",
            f"pageSize={str(rand_page_size)}",
        ]
        return queries

    def get_symbol_from_contract(self, announcement: str) -> str:
        res: str = ""
        splitted_announcement: str = announcement.split(Announcements.usd)[1]
        splitted_announcement = splitted_announcement.split(Announcements.contract)[0]
        splitted_announcement = splitted_announcement.split("and")[0]
        if "(" in splitted_announcement and ")" in splitted_announcement:
            splitted_announcement = splitted_announcement.split("(")[1]
            splitted_announcement = splitted_announcement[:-2]
        splitted_announcement = splitted_announcement.strip()
        return splitted_announcement

    def get_trading_pairs_list(self, announcement: str):
        res: list[str] = []
        if "," in announcement:
            announcement = announcement.split(",")
        if "&" in announcement:
            announcement = announcement.split("&")
        for pair in announcement:
            if "&" in pair:
                sub_pairs = pair.split("&")
                for sub_pair in sub_pairs:
                    res.append(sub_pair.strip())
            else:
                res.append(pair)
        return res

    def get_symbol_from_trading_pair(self, announcement: str) -> str:
        res: str = ""
        splitted_announcement: str = announcement.split(Announcements.binance_adds)[1]
        splitted_announcement = splitted_announcement.split(Announcements.trading_pair)[0]
        splitted_announcement = splitted_announcement.strip()
        trading_pairs_list = self.get_trading_pairs_list(splitted_announcement)
        for pair in trading_pairs_list:
            if "/" in pair and pair.split("/")[1] == Announcements.usdt:
                return pair.split("/")[0].strip()
        return res

    def get_symbol_from_listing(self, announcement: str) -> str:
        res: str = ""
        splitted_announcement: str = announcement.split(Announcements.binance_will_list)[1]
        splitted_announcement = splitted_announcement.split(Announcements.trading_pair)[0]
        res = self.__get_symbol_from_brackets(splitted_announcement)
        return res

    def __get_symbol_from_brackets(self, listing: str) -> str:
        res: str = ""
        if "(" in listing and ")" in listing:
            listing = listing.split("(")[1]
            res = listing.split(")")[0]
        return res

    def get_symbol(self, announcement: str):
        if announcement.endswith(Announcements.contract):
            return self.get_symbol_from_contract(announcement)
        if announcement.startswith(Announcements.binance_adds) and (announcement.endswith(Announcements.trading_pair) or announcement.endswith(Announcements.trading_pairs)):
            return self.get_symbol_from_trading_pair(announcement)
        if announcement.startswith(Announcements.binance_will_list) and not Announcements.innovation_zone in announcement:
            return self.get_symbol_from_listing(announcement)
        return ""

    def get_last_announcement(self):
        """
        Retrieves new coin listing announcements
        """
        queries = self.get_queries()
        random.shuffle(queries)
        request_url = (
            f"https://www.binance.com/gateway-api/v1/public/cms/article/list/query"
            f"?{queries[0]}&{queries[1]}&{queries[2]}&{queries[3]}"
        )

        latest_announcement = requests.get(request_url)

        if latest_announcement.status_code == 200:
            try:
                pass
                # logger.debug(f'X-Cache: {latest_announcement.headers["X-Cache"]}')
            except KeyError:
                # No X-Cache header was found - great news, we're hitting the source.
                pass

            latest_announcement = latest_announcement.json()
            last = latest_announcement["data"]["catalogs"][0]["articles"][0]["title"]
            return last

        else:
            return "Error"

    def extract_announcement(self, announcement: str):
            if announcement != "Error":
                return self.get_symbol(announcement)
            return announcement

