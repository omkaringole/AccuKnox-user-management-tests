import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_add_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.login("Admin", "admin123")
    admin.go_to_user_management()
    admin.add_user(role="ESS", status="Enabled", username="testuser1", password="Test@1234")
    assert admin.verify_user_present("testuser1")
