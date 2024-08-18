import pandas as pd
from src.config import Config


class Utils:
    def read_excel(self):
        """read excel file for ration card
        """
        return pd.read_excel(Config.EXCEL_FILE_PATH, sheet_name=Config.SHEET_NAME, header=1).to_dict(orient="records")
