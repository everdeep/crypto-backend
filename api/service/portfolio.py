from api.service import DataService
from api.enums import OrderSide

class PortfolioService:

    def get_earnings(self, user_id):
        """ Returns the earnings of the user """
    
        return {
            'total_value': 0.0,
            'total_invested': 0.0,
            'total_earnings': 0.0
        }







