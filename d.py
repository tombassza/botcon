import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def login(email, password):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    base_url = "https://www.allticket.com/category/concert"

    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(5)

    try:
        login_button = driver.find_element(By.XPATH, "/html/body/app-root/app-navbar/div/header/div/div[1]/div/div/div[3]/div/div[2]/button")
        login_button.click()
        sleep(30)
        username = driver.find_element(By.ID, "username")
        username.send_keys(email)
        pwd = driver.find_element(By.ID, "password")
        pwd.send_keys(password)
        robot_button = driver.find_element(By.XPATH, "//div[@class='recaptcha-checkbox-border']")
        robot_button.click()
        
        login_button = driver.find_element(By.XPATH, "/html/body/app-root/app-navbar/div/div[2]/div/div/app-login/form/div[5]/button")
        login_button.click()
        sleep(30)
        driver.implicitly_wait(50)
        cur_url = driver.current_url
        while cur_url == base_url:
            # Add the necessary steps to continue with the booking process after login
            # This might involve calling other functions or actions
            pass
        driver.implicitly_wait(10)
    except Exception as e:
        print("Login failed:", e)
    driver.quit()

def book_tickets(email, password, zone, concert, seats, show):
    login(email, password)
    # Rest of your booking process function remains the same
    # ...

def create_gui():
    def on_book_tickets_click():
        email = email_entry.get()
        password = password_entry.get()
        zone = zone_entry.get()
        concert = concert_entry.get()
        seats = seats_entry.get()
        show = show_entry.get()
        book_tickets(email, password, zone, concert, seats, show)

    root = tk.Tk()
    root.title("Concert Ticket Booking")

    email_label = tk.Label(root, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    zone_label = tk.Label(root, text="Zone:")
    zone_label.pack()
    zone_entry = tk.Entry(root)
    zone_entry.pack()

    concert_label = tk.Label(root, text="Concert Name:")
    concert_label.pack()
    concert_entry = tk.Entry(root)
    concert_entry.pack()

    seats_label = tk.Label(root, text="Number of Seats:")
    seats_label.pack()
    seats_entry = tk.Entry(root)
    seats_entry.pack()

    show_label = tk.Label(root, text="Show Number:")
    show_label.pack()
    show_entry = tk.Entry(root)
    show_entry.pack()

    book_button = tk.Button(root, text="Book Tickets", command=on_book_tickets_click)
    book_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
