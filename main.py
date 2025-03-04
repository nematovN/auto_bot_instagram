from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Instagram login ma'lumotlari
USERNAME = "your_username"
PASSWORD = "your_password"

# Selenium uchun browser sozlamalari
chrome_options = Options()
chrome_options.add_argument("--headless")  # Brauzerni yashirin rejimda ochish
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Selenium drayverini ishga tushiramiz
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


def login():
    """ Instagramga login qilish """
    print("[INFO] Instagramga login qilinmoqda...")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    # Username va password kiritish
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    print("[SUCCESS] Instagramga muvaffaqiyatli kirdik!")


def like_posts_by_tag(tag, amount=10):
    """ Berilgan hashtag bo'yicha postlarga like bosish """
    print(f"[INFO] #{tag} bo‘yicha {amount} ta postga like bosilmoqda...")
    driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
    time.sleep(5)

    posts = driver.find_elements(By.CSS_SELECTOR, "article a")[:amount]

    for i, post in enumerate(posts, 1):
        try:
            post.click()
            time.sleep(3)

            like_button = driver.find_element(By.XPATH, '//span[@aria-label="Like"]')
            like_button.click()
            print(f"[LIKE] {i}/{amount} - Postga like bosildi")
            time.sleep(random.randint(2, 5))  # Tasodifiy kutish
            driver.find_element(By.XPATH, '//button[@aria-label="Close"]').click()
            time.sleep(2)
        except:
            print("[ERROR] Like bosishda xatolik yuz berdi")
            continue


def follow_users_by_tag(tag, amount=5):
    """ Hashtag bo‘yicha foydalanuvchilarni follow qilish """
    print(f"[INFO] #{tag} bo‘yicha {amount} ta foydalanuvchini follow qilinmoqda...")
    driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
    time.sleep(5)

    posts = driver.find_elements(By.CSS_SELECTOR, "article a")[:amount]

    for i, post in enumerate(posts, 1):
        try:
            post.click()
            time.sleep(3)

            follow_button = driver.find_element(By.XPATH, '//button[text()="Follow"]')
            follow_button.click()
            print(f"[FOLLOW] {i}/{amount} - Foydalanuvchi follow qilindi")
            time.sleep(random.randint(2, 5))  # Tasodifiy kutish
            driver.find_element(By.XPATH, '//button[@aria-label="Close"]').click()
            time.sleep(2)
        except:
            print("[ERROR] Follow qilishda xatolik yuz berdi")
            continue


def comment_on_posts(tag, comments, amount=5):
    """ Hashtag bo‘yicha postlarga comment yozish """
    print(f"[INFO] #{tag} bo‘yicha {amount} ta postga comment yozilmoqda...")
    driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
    time.sleep(5)

    posts = driver.find_elements(By.CSS_SELECTOR, "article a")[:amount]

    for i, post in enumerate(posts, 1):
        try:
            post.click()
            time.sleep(3)

            comment = random.choice(comments)
            comment_box = driver.find_element(By.CSS_SELECTOR, "textarea")
            comment_box.send_keys(comment)
            comment_box.send_keys(Keys.RETURN)
            print(f"[COMMENT] {i}/{amount} - \"{comment}\" yozildi")
            time.sleep(random.randint(2, 5))  # Tasodifiy kutish
            driver.find_element(By.XPATH, '//button[@aria-label="Close"]').click()
            time.sleep(2)
        except:
            print("[ERROR] Comment yozishda xatolik yuz berdi")
            continue


if __name__ == "__main__":
    login()
    like_posts_by_tag("python", 10)
    follow_users_by_tag("python", 5)
    comment_on_posts("python", ["Great!", "Nice!", "Love this!"], 5)

    driver.quit()
    print("[DONE] Bot ishini tugatdi!")
