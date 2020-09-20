house_loc_bedrooms = locality_bedrooms[locality_bedrooms['type_of_property'] == 'house']

dataframes = []
for element in ['Anvers', 
                'Brabant Flamand', 
                'Brabant Wallon', 
                'Bruxelles', 
                'Flandre-Occidentale',
                'Flandre-Orientale',
                'Hainaut',
                'Liege',
                'Limbourg',
                'Luxembourg',
                'Namur'
               ]:
    dataframe = house_loc_bedrooms[house_loc_bedrooms['province'] == element].number_of_rooms.agg(['value_counts'])
    dataframe.reset_index(level=0, inplace=True)
    dataframe = dataframe.rename(columns={'index':'Number of bedrooms', 'value_counts':element})
    dataframes.append(dataframe)

house_bedrooms_province = pd.merge(dataframes[0], dataframes[1], how = 'outer', on='Number of bedrooms')

for i in range(2, len(dataframes)):
    house_bedrooms_province = pd.merge(house_bedrooms_province, dataframes[i], how = 'outer', on='Number of bedrooms')
    












house_bedrooms_province.plot.bar(x = 'Number of bedrooms', 
                                y = ['Anvers', 
                                      'Brabant Flamand',
                                      'Flandre-Occidentale',
                                      'Flandre-Orientale',
                                      'Limbourg'],
                               logy=True,
                               figsize=(15,10),
                               title="Number of houses by bedrooms for the Flemish Region")



house_bedrooms_province.plot.bar(x = 'Number of bedrooms', 
                                y = 'Bruxelles',
                               logy=True,
                               figsize=(15,10),
                               title="Number of houses by bedrooms for Bruxelles")



house_bedrooms_province.plot.bar(x = 'Number of bedrooms', 
                                y = ['Brabant Wallon',
                                      'Hainaut',
                                      'Liege',
                                      'Luxembourg',
                                      'Namur'],
                               logy=True,
                               figsize=(15,10),
                               title="Number of houses by bedrooms for the Walloon Region")