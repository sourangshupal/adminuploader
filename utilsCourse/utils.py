import pandas as pd

def excelReader(filename, sheetname):
    """

    :param filename:
    :param sheetname:
    :return: Dataframe
    """
    dataframe = pd.read_excel(filename, sheet_name=sheetname)
    return dataframe
