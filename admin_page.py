from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_user_management(self):
        self.page.click('text=Admin')
        self.page.wait_for_selector('text=System Users')

    def add_user(self, role, status, username, password):
        self.page.click('text=Add')
        self.page.select_option('select[role="combobox"]', label=role)
        self.page.fill('input[placeholder="Username"]', username)
        self.page.select_option('select[role="combobox"]', label=status)
        self.page.fill('input[type="password"]', password)
        self.page.fill('input[type="password"]:right-of(:text("Confirm Password"))', password)
        self.page.click('button:has-text("Save")')

    def search_user(self, username):
        self.page.fill('input[placeholder="Search"]', username)
        self.page.click('button:has-text("Search")')
        self.page.wait_for_timeout(2000)

    def delete_user(self, username):
        self.search_user(username)
        self.page.click('input[type="checkbox"]')
        self.page.click('button:has-text("Delete")')
        self.page.click('button:has-text("Yes, Delete")')

    def verify_user_present(self, username):
        return self.page.is_visible(f'text={username}')
