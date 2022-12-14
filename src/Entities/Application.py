import asyncio
from src.Entities.Information_Creator import Information_Creator
from src.Entities.OSF_Crawler import OSF_Crawler



class Application:

    def search(self, search_term):
        asyncio.get_event_loop().run_until_complete(self.run(search_term))


    async def run(self, search_term):
        searchResultList = await OSF_Crawler.crawl_information(search_term)
        Information_Creator.create_information(searchResultList, search_term)
