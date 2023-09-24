class DiscountData:
    def __init__(self, data):
        pass


class Product:
    def __init__(self, product) -> None:
        self.discounts = []

    def add_discount(self, discount_details: DiscountData):
        pass


class User:
    def __init__(self, user, products):
        pass

    def has_previously_bought(self, product: Product):
        pass


class Notifier:
    def notify(self, user: User, message: str):
        pass


class DiscountManager:
    def __init__(self, notifier):
        self.notifier = notifier

    def create_discount(self,
                        product: Product,
                        discount_details: DiscountData,
                        users: list[User]) -> None:
        if users:
            key_user = users[0]
        else:
            raise RuntimeError(
                "can't create a discount for a product with no key")

        product.add_discount(discount_details)

        for user in users:
            if user.has_previously_bought(product):
                self.notifier.notify(
                    key_user, "you may be interested in discount in this product")
