class Vertical:
    def __init__(self, page):
        self.page = page

        self.ver = page.locator('(//a[text()="Verticals"])[1]')
        self.trading = page.locator('//strong[text()="Trading"]')
        self.retail = page.locator('//strong[text()="Retail and Ecommerce"]')
        self.healthcare = page.locator('//strong[text()="Healthcare"]')
        self.fintech = page.locator('//strong[text()="Fintech"]')
        self.custom_app = page.locator('//strong[text()="Custom App"]')

    def mouse_hover(self):
        # Hover on Verticals menu first
        self.ver.hover()

        items = [
            self.trading,
            self.retail,
            self.healthcare,
            self.fintech,
            self.custom_app
        ]

        for item in items:
            item.wait_for(state="visible")   # Wait until submenu is visible
            item.hover()
            self.page.wait_for_timeout(1000)  # Optional (1 second)
            self.ver.hover()                  # Hover back to Verticals menu