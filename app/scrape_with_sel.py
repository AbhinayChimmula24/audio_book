from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

class Request:
    def __init__(self, url):
        self.url = url

    def get_job_elements(self, class_name):
        try:
            # Set up user agent rotation
            software_names = [SoftwareName.CHROME.value]
            operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
            user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
            user_agent = user_agent_rotator.get_random_user_agent()

            # Set up Chrome options
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument('--window-size=1420,1080')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument(f'user-agent={user_agent}')

            # Initialize Chrome webdriver
            browser = webdriver.Chrome(options=chrome_options)
            browser.get(self.url)

            # Wait for elements with the specified class name
            time_to_wait = 5
            WebDriverWait(browser, time_to_wait).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, f'div.{class_name}'))
            )

            # Get all div elements with the specified class name
            job_elements = browser.find_elements(By.CSS_SELECTOR, f'div.{class_name}')

            # Extract HTML content from each div element
            job_html_content = [element.get_attribute('outerHTML') for element in job_elements]

            # Close the browser
            browser.quit()
            print(job_html_content)
            return job_html_content


        except Exception as e:
            print(f"An error occurred: {e}")
            return []

if __name__ == "__main__":
    # Example usage: Fetch job elements with class 'job_seen_beacon' from Indeed search results
    request = Request("https://medium.com/@amanatulla1606/transformer-architecture-explained-2c49e2257b4c")
    job_html_content = request.get_job_elements('job_seen_beacon')    
    for html_content in job_html_content:
        print(html_content)
