class Technology:

    def __init__(self, page):
        self.page = page

        self.technology = page.locator('(//a[text()="Technologies"])[1]')
        self.ecom_dev = page.locator('//strong[text()="eCommerce Development"]')
        self.mob_app_dev = page.locator('//strong[text()="Mobile App Development"]')
        self.art_int = page.locator('//strong[text()="Artificial Intelligence"]')

        # Ecommerce
        self.magento = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.codeigniter = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.bigcommerce = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.cscart = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.nopcommerce = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.laravel = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.drupal = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.joomla = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.express = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.opencart = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.wordpress = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.shopify = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.nodejs = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.woocommerce = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.prestashop = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.wix = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.react = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
    def mouse_hover(self):

        tech_list = [
            self.ecom_dev,
            self.mob_app_dev,
            self.art_int
        ]

        for item in tech_list:
            self.technology.hover()
            item.hover()
            self.page.wait_for_timeout(3000)

    def ecom_links(self):

        links = [
            self.magento,
            self.codeigniter,
            self.bigcommerce,
            self.cscart,
            self.nopcommerce,
            self.laravel,
            self.drupal,
            self.joomla,
            self.express,
            self.opencart,
            self.wordpress,
            self.shopify,
            self.nodejs,
            self.woocommerce,
            self.prestashop,
            self.wix,
            self.react
        ]

        for link in links:
            self.technology.hover()
            self.ecom_dev.hover()

            link.click()

            self.page.go_back()
            self.page.wait_for_load_state("load")