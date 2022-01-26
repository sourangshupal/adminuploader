from utilsCourse.utils import excelReader

valueholder = []


def courseVideoResources(filename, sheetname):
    data = excelReader(filename, sheetname)
    for i in data.index:
        mydict = {
            "Section Name": data["Section Name"][i],
            "Lesson Title": data["Lesson Title"][i],
            "Lesson URL": data["Lesson URL"][i],
            "Resource URL 1": data["Resource URL 1"][i],
            "Resource URL 2": data["Resource URL 2"][i],
            "Resource URL 3": data["Resource URL 3"][i],
        }
        valueholder.append(mydict)
    return valueholder


# a = courseVideoResources()
# print(a)
