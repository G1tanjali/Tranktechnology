import pytest
from pages.technologypage import Technology

@pytest.mark.smoke
def test_technology(page):
    tech = Technology(page)

    tech.mouse_hover()     # Hover on Technologies
    tech.ecom_links()      # Click all eCommerce links
