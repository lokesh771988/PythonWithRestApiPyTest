from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browserName = "Edge"

if browserName == "Edge":
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
elif browserName == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
else:
    print("no browser name present")

driver.get("https://www.google.com")

driver.close()
