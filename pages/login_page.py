class LoginPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.page.goto(self.url)

    def login(self, user, passw):
        self.page.wait_for_selector("#user-name")

        self.page.fill("#user-name", user)
        self.page.fill("#password", passw)
        self.page.click("#login-button")

    def is_dashboard_visible(self):
        self.page.wait_for_selector("#inventory_container", timeout=5000)
        return True
    
    def get_error_message(self ):
        return self.page.locator("[data-test='error']").inner_text()