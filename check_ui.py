"""Verificação da navegação e da apresentação da wiki em Chromium."""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pathlib import Path

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/chromium'
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
with webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options) as browser:
    browser.set_window_size(1440, 1000)
    browser.get('http://127.0.0.1:8088/')
    assert 'Wiki de TI' in browser.title
    assert len(browser.find_elements(By.CSS_SELECTOR, '#navigation a')) == len(list((Path(__file__).parent.parent / 'docs').rglob('*.md')))
    browser.find_element(By.CSS_SELECTOR, 'a[href="/sistemas/03-multivendas-pdv.md"]').click()
    assert browser.find_element(By.CSS_SELECTOR, 'article h1').text == 'MultiVendas PDV'
    assert browser.find_element(By.CSS_SELECTOR, 'article table').is_displayed()
    assert browser.find_element(By.CSS_SELECTOR, '.contents .toc').is_displayed()
    assert '[informação ausente]' not in browser.find_element(By.CSS_SELECTOR, 'article').text
    assert browser.find_element(By.ID, 'edit-button').is_displayed()
    browser.save_screenshot('/tmp/handover-wiki-desktop.png')
    browser.set_window_size(390, 844)
    browser.refresh()
    assert not browser.find_element(By.ID, 'navigation').is_displayed()
    browser.find_element(By.ID, 'menu-button').click()
    assert browser.find_element(By.ID, 'navigation').is_displayed()
    browser.find_element(By.ID, 'menu-button').click()
    assert browser.execute_script('return document.documentElement.scrollWidth <= window.innerWidth')
    browser.save_screenshot('/tmp/handover-wiki-mobile.png')
    browser.get('http://127.0.0.1:8088/sistemas/04-ezpoint-web.md?source=1')
    assert '# EzPoint Web' in browser.find_element(By.TAG_NAME, 'body').text
print('Navegação, índice, tabelas, editor local, menu móvel e Markdown original conferidos.')
