from utilsCourse.utils import excelReader

valueholder = []
feature_holder = []


def courseCirriculum(filename, sheetname):
    data = excelReader(filename, sheetname)
    cleaned_data = data[['Features', 'Learn', 'Requirements']].dropna(how='all')
    valueholder.clear()
    feature_holder.clear()
    for i in data.index:
        mydict = {"Topic": data["Topics"][i], "Subtopic": data["Subtopics"][i]}
        valueholder.append(mydict)

    for j in cleaned_data.index:
        extra_features = {"Features": cleaned_data['Features'][j], "Learn": cleaned_data['Learn'][j],
                         "Requirements": cleaned_data['Requirements'][j]}
        feature_holder.append(extra_features)
    return valueholder, feature_holder
