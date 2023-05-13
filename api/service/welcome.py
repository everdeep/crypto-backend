from api.model.welcome import WelcomeModel


class WelcomeService:
    def __init__(self):
        pass

    def get_welcome(self):
        return WelcomeModel()
