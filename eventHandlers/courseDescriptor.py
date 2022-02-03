from utilsCourse.utils import excelReader

valueholder = []


def courseDescriptor(filename, sheetname):
    valueholder.clear()
    data = excelReader(filename, sheetname)
    data_json = dict(zip(data.Fields, data.Values))
    valueholder.append(data_json)
    return valueholder


# a = courseDescriptor()
# print(a)
