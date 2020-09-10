
def first():
    '''1) Use Python lists and dictionaries. How to do slicing of lists using the colon (:) specifications. '''
    print('Question 1:')
    # Initializing the a sample dictionay and list
    dic = {'1':'satya', '2':'prakash', '3':'sharma'}
    lis = [i+1 for i in range(10)]

    #printing the dict and list
    print("Sample Dictionary", dic)
    print("Sample list", lis)
    print("-------------------------------")

    # We can simply get the dictionary value if we know the key.
    print('Getting the dictionary of key 1->', dic['1'])

    ## Slicing of list using colon(:)
    # Get the list's value of specific left based index by list[i], it start with 0 based index
    print("2nd index's value from left 0 based index->", lis[2])

    # Get the list's value from right based index by  list[-i], it start with 1 based index
    print("2nd index's value from the right 1 based index->", lis[-2])

    # Get the list's sublist's by list[i:j] where i in inclusive and j is exclusive
    print("list's value from 2 index to 8 index->", lis[2:8])

    # Reverse the list by list[::-1]
    print("Reverse the list->", lis[::-1])

    print('___________________________________________________________')

def second():
    '''2) Create a DataFrame object from the data loaded from a dataset. '''
    print('Question 2')
    # Import the pandas library
    import pandas as pd

    # read the iris data set in data frame of pandas library
    data = pd.read_csv('iris.data')
    print("data type-> ",type(data))
    print(data.head())

    print('____________________________________________________________')
    return data

def third(data):
    '''3) Print various rows and columns of the dataset. '''
    print('Question 3')
    # get the len/size of the data by len(data)/ data.size()
    print('Length/Rows of data set->', len(data))

    # get the first n rows by data.head(n)
    print('\nPrint rows from 1-10', data.head(10))

    # get the column by data.column, and len by len(data.column)
    print('Number of columns->', len(data.columns))
    print('All columns name: ', data.columns)

    # get the rows and column by data.shape
    print('Shape (r*c): ', data.shape)

    # get the specific column by data['column_name'].head()
    print('print petal length column\n', data['petal length'].head())

    # get the specific rows x by data[x:x+1]
    print('\n 3rd row of the data set')
    print(data[3:4].head())
    print('____________________________________________________________')

def four(data):

    '''4) Print a subset of rows and a subset of columns'''
    print('Question 4')
    # Select subset of column
    tmp = data[['sepal length', 'sepal width']]
    print('shape r*c: ', tmp.shape)
    print(tmp.head())

    # Select subset of rows
    # select specific rows based on some condition on column value
    sepal_len_gth_3 = data[data['sepal length']>3]
    print('\nsepal_len_gth_3 r*c: ', tmp.shape)
    # print(sepal_len_gth_3.head())

    # select the specific rows based on list based condition on column value
    tmp2 = data[data['class'].isin(['Iris-setosa'])]
    print('shape of data based on isin:', tmp2.shape)
    # print(tmp2.head())

    # select specific rows and column
    tmp3 = data.loc[data['sepal length']>3,'class']
    print('shape of data for specific row and column based on condition:', tmp3.shape)
    print(tmp3.head())

    # select specific rows and column based on row number and column number
    tmp4 = data.iloc[9:25, 2:5]
    print('shape of data for specific row and column number:', tmp4.shape)
    print(tmp4.head())
    print('____________________________________________________________')

def five(data):

    '''5) How to group (aggregate) specific columns that correspond to certain specific values of rows. (use DataFrame.groupby()) '''
    print('Question 5')
    # groupby have multiple arguments like by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=<object object>, observed=False, dropna=True
    # Example of groupby
    group_by_class = data.groupby(['class'])
    print('group by class')
    print(group_by_class.head())
    # group_by_class.head()

    # Example of groupby then apply aggregate function like mean(), sum(), etc
    group_by_class_with_mean = data.groupby(by=['class']).mean()
    print('\ngroup by class then apply aggregate function mean()')
    print(group_by_class_with_mean.head())
    # group_by_class_with_mean.head()

    # Example of groupby then sort them
    group_by_class_with_sort = data.groupby('class', sort=True).head()
    print('\ngroup by class then sort them in ascending order')
    print(group_by_class_with_sort.head())
    # group_by_class_with_sort.head()
    print('____________________________________________________________')


if __name__ == "__main__":
    first()
    data = second()
    third(data)
    four(data)
    five(data)