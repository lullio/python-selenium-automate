from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurando o ChromeDriver com webdriver_manager
service = Service(ChromeDriverManager().install())

# Inicializando o navegador Chrome
driver = webdriver.Chrome(service=service)

# Acessando um site específico
driver.get("https://www.seusite.com")

# Seu código de automação aqui

# Fechando o navegador após a automação (opcional)
driver.quit()