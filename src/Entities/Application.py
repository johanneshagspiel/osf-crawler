import asyncio

from src.Entities.Information.Information_Creator_API import Information_Creator_API
from src.Entities.Information.Information_Creator_Crawler import Information_Creator
from src.Entities.Interaction.OSF_API import OSF_API
from src.Entities.Interaction.OSF_Crawler import OSF_Crawler


class Application:

    def search(self, search_term):
        asyncio.get_event_loop().run_until_complete(self.run(search_term))

    async def run(self, search_term):
        searchResultList = await OSF_Crawler.crawl_information(search_term)
        Information_Creator.create_information(searchResultList, search_term)

    def run_api(self, mode):

        osf_api = OSF_API()
        osf_api.get_all_projects(mode=mode)

        information_creator = Information_Creator_API()
        information_creator.create_excel_file(mode=mode)
