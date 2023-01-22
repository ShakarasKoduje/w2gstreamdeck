import os, sys
from Scripts import authentication
#from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import socket

if len(sys.argv) > 1:
    dane_logowania = authentication.DaneLogowania(sys.argv[1], sys.argv[2], sys.argv[3])
    print(dane_logowania)
print(f'''Informacja z pliku .env MOJA_INFORMACJA {os.environ.get("MOJA_INFORMACJA")}''')

browser = webdriver.Firefox()
browser.get("https://www.wp.pl")
browser.minimize_window()

time.sleep(1)
def akceptujWarunki(browser):
    #/html/body/div[2]/div/div[2]/div[3]/div/button[2]
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div/button[2]").click()

def Poczta(browser):
    browser.find_element(By.XPATH, "/html/body/div[3]/div[6]/div[2]/div[3]/a[1]").click()

buffer_size = 1024
text = "Koniec"
while(True):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.bind(('0.0.0.0', 8080))
    mysocket.listen(5)
    (client, (ip,port)) = mysocket.accept()
    #print(client, port)
    client.send(b"knock knock knock, I'm the server")
    data = client.recv(buffer_size)
    data_decode = data.decode().lower()
    print(data.decode().lower()) #tu moglaby byc logika zarzadzajaca np. selenium i sterowaniem w2g
    if(data.decode()==text): break
    if(data_decode=="akceptuj"): akceptujWarunki(browser=browser)
    if(data_decode=="poczta"): Poczta(browser=browser)
    mysocket.close()
    time.sleep(0.75)
mysocket.close()
browser.close()