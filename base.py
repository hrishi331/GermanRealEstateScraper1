from playwright.sync_api import sync_playwright 
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()


        page_no = 1
        url = f"https://www.engelvoelkers.com/de/en/properties/res/sale/house?businessArea[]=residential&currency=EUR&measurementSystem=metric&page={page_no}&placeId=ChIJa76xwh5ymkcRW-WRjmtd6HU&propertyMarketingType[]=sale&propertyType[]=house&sortingOptions[]=PUBLISHED_AT_DESC&placeName=Germany"
        page.goto(url)
        page.wait_for_timeout(5000)
        
        prop_detail_urls = page.query_selector_all("div.sc-Uxykg.iKmqSV  a")

        n=1
        for prop_detail_url in prop_detail_urls:
            url = prop_detail_url.get_attribute("href")
            url = ''.join(['https://www.engelvoelkers.com',url])
            page1 = browser.new_page()
            page1.goto(url)
            page1.wait_for_timeout(5000)

            prop_type = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(1) > div > ul:nth-child(1) > li:nth-child(1) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            condition = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(1) > div > ul:nth-child(1) > li:nth-child(2) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            rooms = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(1) > div > ul:nth-child(1) > li:nth-child(3) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            bedrooms = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(1) > div > ul:nth-child(1) > li:nth-child(4) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            bathrooms = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(1) > div > ul:nth-child(1) > li:nth-child(5) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            number_of_floors = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(1) > div > ul:nth-child(2) > li:nth-child(1) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            parking_spaces = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(1) > div > ul:nth-child(2) > li:nth-child(2) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            total_surface = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(1) > div > ul:nth-child(2) > li:nth-child(3) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            living_area = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(1) > div > ul:nth-child(2) > li:nth-child(4) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            plot_surface = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(1) > div > ul:nth-child(2) > li:nth-child(5) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')

            construction_year = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(2) > div > ul:nth-child(1) > li:nth-child(1) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            # energy_efficiency_class = page.query_selector('')
            energy_certificate_available = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(2) > div > ul:nth-child(1) > li:nth-child(3) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            energy_certificate_type = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(2) > div > ul:nth-child(1) > li:nth-child(4) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            final_energy_demand = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(2) > div > ul:nth-child(2) > li:nth-child(1) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            type_of_heating = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(2) > div > ul:nth-child(2) > li:nth-child(2) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            energy_source =page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(2) > div > ul:nth-child(2) > li:nth-child(3) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')
            energy_includes_hot_water = page1.query_selector('#__next > div > section.sc-e6ad36e3-0.bBhQyo > div > div > div:nth-child(2) > div > ul:nth-child(2) > li:nth-child(4) > p.sc-760d7490-0.hXRuMp.sc-56a8283-4.cAeJIE')

            location = page1.query_selector('#__next > div > div:nth-child(10) > div > h2')
            

            values = [prop_type,condition,rooms,bedrooms,bathrooms,number_of_floors,parking_spaces,total_surface\
                          ,living_area,plot_surface,construction_year,energy_certificate_available,energy_certificate_type,final_energy_demand,\
                            type_of_heating,energy_source,energy_includes_hot_water]
            
            variable_names = ['prop_type','condition','rooms','bedrooms','bathrooms','number_of_floors','parking_spaces','total_surface'\
                          ,'living_area','plot_surface','construction_year','energy_certificate_available','energy_certificate_type','final_energy_demand',\
                            'type_of_heating','energy_source','energy_includes_hot_water']
            
            info = {}

            for i,j in zip(values,variable_names):
                if i:
                    info[j] = i.text_content()
                else:
                    info[j] = '-' 

            if location:
                info['location'] = location.text_content().split(': ')[1]
            else:
                info['location'] = '-'

            print(f'Proprty No {n}')
            print(info)
            n=n+1
            page1.close()


        browser.close()
            

if __name__=="__main__":
    run()
    
