import pytest
from pages.verticalpage import Vertical

@pytest.mark.smoke
def test_vertical(page):
    v1 = Vertical(page)
    v1.mouse_hover()
