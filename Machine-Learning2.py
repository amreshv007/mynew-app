import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()


# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero()

def answer_one():
    return df['Gold'].argmax()

def answer_two():
    return (df['Gold']-df['Gold.1']).argmax()

def answer_three():
    copy_df=df.copy()
    copy_df = copy_df[(copy_df['Gold']>0) & (copy_df['Gold.1']>0)]
    return ((copy_df['Gold']-copy_df['Gold.1'])/copy_df['Gold.2']).argmax() 


def answer_four():
    df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']
    return df['Points']

census_df = pd.read_csv('census.csv')
census_df.head()

def answer_five():
    return census_df['STNAME'].value_counts().argmax()



def answer_six():
    copy_df = census_df.copy()
    copy_df = copy_df.groupby(['STNAME'])
    states_pop = pd.DataFrame(columns=['pop'])
    for i, c in copy_df:
        states_pop.loc[i] = [c.sort_values(by='CENSUS2010POP', ascending=False)[1:4]['CENSUS2010POP'].sum()]
    top3 = states_pop.nlargest(3,'pop')
    return list(top3.index)


def answer_seven():
    pop = census_df[['STNAME','CTYNAME','POPESTIMATE2015','POPESTIMATE2014','POPESTIMATE2013','POPESTIMATE2012','POPESTIMATE2011','POPESTIMATE2010']]
    pop = pop[pop['STNAME']!=pop['CTYNAME']]
    index = (pop.max(axis=1)-pop.min(axis=1)).argmax()
    return census_df.loc[index]['CTYNAME']
