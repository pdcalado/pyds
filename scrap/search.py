from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.caixagest.pt/fundos_cotacoes.aspx")

try:
    if "Caixagesti" not in driver.title:
        raise ValueError("bad title: " + driver.title)
    
    elem = driver.find_elements_by_xpath('//*[@id="Form1"]/table[2]/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[4]/td[2]')
    
    basepath = '//*[@id="Form1"]/table[2]/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[4]/'
    
    elrow = driver.find_elements_by_xpath(basepath + 'td[1]/a')
    
    if "Seleção Global Moderado" not in elrow[0].text:
        raise ValueError("wrong row: " + elrow[0].text)
        
    elcol = driver.find_elements_by_xpath(basepath + 'td[2]')
    value = elcol[0].text.replace('€', '').replace(' ','').replace(',','')
    print("text is", value)

except ValueError as e:
    print("raised error:", e)

driver.close()
