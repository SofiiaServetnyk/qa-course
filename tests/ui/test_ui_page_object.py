from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # Create page object
    sign_in_page = SignInPage()

    # Open the URL
    sign_in_page.go_to()

    # Try to login into into GitHub
    sign_in_page.try_login(" ", " ")

    # Assert the page title
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Close the browser
    sign_in_page.close()
