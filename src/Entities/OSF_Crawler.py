from random import uniform
from time import sleep
from bs4 import BeautifulSoup, Comment
from pyppeteer import launch

from src.Entities.Search_Result import Search_Result

class OSF_Crawler:

    @staticmethod
    async def crawl_information(search_term):
        print(f"Crawling osf.io for the term: {search_term}")

        browser = await launch()
        page = await browser.newPage()

        searchResultList = []

        response = await page.goto(f'https://osf.io/search/?q={search_term}&page=1')
        status_code = response.headers["status"]

        if status_code != '200':
            print(response.headers)

        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.body
        for element in body(text=lambda text: isinstance(text, Comment)):
            element.extract()

        pagger = body.find_all("ul", class_="pager")[0]
        max_page_number = int(pagger.findChild("span").text.split(" of ")[1])

        for osf_page in range(1, max_page_number):

            print_str = f"Checking Page {osf_page} / {max_page_number}"
            print(print_str)

            search_results = body.find_all("div", class_="search-result")

            for result in search_results:

                title = None
                file_name = None
                registration_date = None
                description = None
                contributors = []
                tags = []

                h4_child = result.findChild("h4")
                if h4_child:
                    a_child = h4_child.findChild("a")
                    if a_child:
                        title = a_child.text
                        file_name = a_child["href"]


                span_children = result.findChildren("span")
                if span_children:
                    for span in span_children:
                        data_bind = span["data-bind"]

                        if data_bind == "text: 'Date Registered: ' + dateRegistered['local'], tooltip: {title: dateRegistered['utc']}":
                            registration_date = span.text.split("Date Registered: ")[1]

                        elif data_bind == "foreach: contributors":
                            a_children = span.findChildren("a")
                            if a_children:
                                for a_child in a_children:
                                    contributors.append(a_child.text)

                        elif data_bind == "fitText: {text: description, length: 500}":
                            description = span.text

                        elif data_bind == "text: $data":
                            tags.append(span.text)

                newSearchResult = Search_Result(title, file_name, registration_date, description, contributors, tags)
                searchResultList.append(newSearchResult)

            next_page_number = osf_page + 1
            if next_page_number == max_page_number + 1:
            #if next_page_number == 4:
                print(f"Finished crawling osf.io for the term: {search_term}")
                break
            else:
                get_next_page = True
                while get_next_page:

                    try:
                        random_wait_time = uniform(1.0, 5.0)
                        sleep(random_wait_time)

                        print("Before")
                        response = await page.goto(f'https://osf.io/search/?q={search_term}&page={next_page_number}')
                        print("After")

                        status_code = response.headers["status"]
                        while status_code != '200':
                            wrong_status_code_message = f"Error - response status code: {status_code}. Will try again after short delay."
                            print(wrong_status_code_message)

                            random_wait_time = uniform(1.0, 5.0)
                            sleep(random_wait_time)

                            print("Before")
                            response = await page.goto(f'https://osf.io/search/?q={search_term}&page={next_page_number}')
                            print("After")

                            status_code = response.headers["status"]

                        get_next_page = False
                    except Exception as e:
                        print(e)
                        random_wait_time = uniform(1.0, 5.0)
                        sleep(random_wait_time)

                html = await page.content()
                soup = BeautifulSoup(html, 'html.parser')
                body = soup.body
                for element in body(text=lambda text: isinstance(text, Comment)):
                    element.extract()

        return searchResultList
