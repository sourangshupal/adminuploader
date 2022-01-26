from utilsCourse.utils import excelReader

valueholder = []


def courseCirriculum(filename, sheetname):
    data = excelReader(filename, sheetname)
    for i in data.index:
        mydict = {"Topic": data["Topics"][i], "Subtopic": data["Subtopics"][i]}
        valueholder.append(mydict)
    return valueholder
