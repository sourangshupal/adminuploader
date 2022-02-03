from utilsCourse.utils import excelReader

valueholder = []


def courseAssignments(filename, sheetname):
    data = excelReader(filename, sheetname)
    valueholder.clear()
    for i in data.index:
        mydict = {
            "Section Name": data["Section Name"][i],
            "Lesson Title": data["Lesson Title"][i],
            "Lesson URL": data["Lesson URL"][i],
            "Maximum Points User Can Obtain": data["Maximum Points User Can Obtain"][i],
        }
        valueholder.append(mydict)
    return valueholder


# a = courseAssignments()
# print(a)
