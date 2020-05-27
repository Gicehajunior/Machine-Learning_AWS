import pandas 

wine_dataset_path = "Resources/wine_dataset/winequality-red.csv"
def read_csv_file(path):
    
    filename = pandas.read_csv(path, sep=';')
    csv_file = filename.head()
    
    return csv_file

csv = read_csv_file(wine_dataset_path)
# print(csv)

# Renaming columns
def rename_column(csv):
    csv.columns =  [label.replace(' ', "_") for label in csv.columns]
    csv_file = csv.head()
    
    return csv_file

edited_csv = rename_column(csv)

# print(edited_csv)


def numeric_to_buckets(csv, column_name):
    median = csv[column_name].median()
    for i, val in enumerate(csv[column_name]):
        if val >= median:
            csv.loc[i, column_name] = 'high'
        else:
            csv.loc[i, column_name] = 'low'
            

# numeric_to_buckets(csv, feature)

for feature in csv.columns[:-1]:
    numeric_to_buckets(csv, feature)
    print (csv.groupby(feature).quality.mean(), '\n')
