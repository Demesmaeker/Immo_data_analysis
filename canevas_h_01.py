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
    




house_loc_garden = locality_garden[locality_garden['type_of_property'] == 'house']
house_loc_garden_0 = house_loc_garden[house_loc_garden['garden'] == 0].groupby('province').fully_equipped_kitchen.agg(['count'])
house_loc_garden_1 = house_loc_garden[house_loc_garden['garden'] == 1].groupby('province').fully_equipped_kitchen.agg(['count'])

house_loc_garden_0.reset_index(level=0, inplace=True)
house_loc_garden_0 = house_loc_garden_0.rename(columns={'count':'No garden'})
house_loc_garden_1.reset_index(level=0, inplace=True)
house_loc_garden_1 = house_loc_garden_1.rename(columns={'count':'Garden'})

house_province_garden = pd.merge(house_loc_garden_0, house_loc_garden_1, how = 'outer', on='province')

house_province_garden


house_province_garden.plot.bar(x = 'province', 
                       y = ['Garden', 'No garden'], 
                       figsize=(15,10), 
                       title="Presence of an aparment's garden by province")


apart_loc_garden = locality_garden[locality_garden['type_of_property'] == 'apartment']
apart_loc_garden_0 = apart_loc_garden[apart_loc_garden['garden'] == 0].groupby('province').fully_equipped_kitchen.agg(['count'])
apart_loc_garden_1 = apart_loc_garden[apart_loc_garden['garden'] == 1].groupby('province').fully_equipped_kitchen.agg(['count'])

apart_loc_garden_0.reset_index(level=0, inplace=True)
apart_loc_garden_0 = apart_loc_garden_0.rename(columns={'count':'No garden'})
apart_loc_garden_1.reset_index(level=0, inplace=True)
apart_loc_garden_1 = apart_loc_garden_1.rename(columns={'count':'Garden'})

apart_province_garden = pd.merge(apart_loc_garden_0, apart_loc_garden_1, how = 'outer', on='province')

apart_province_garden


apart_province_garden.plot.bar(x = 'province', 
                       y = ['Garden', 'No garden'], 
                       figsize=(15,10), 
                       title="Presence of an aparment's garden by province")





house_loc_gard_area = locality_garden[locality_garden['type_of_property'] == 'house']
house_loc_gard_area = house_loc_gard_area.groupby('province').garden_area.describe()
house_loc_gard_area.reset_index(level=0, inplace=True)
house_loc_gard_area

house_loc_gard_area.plot.bar(x = 'province', 
                        y = ['min', 'mean', '75%'],
                       figsize=(15,10),
                       title="min, mean and 75% of the house's garden's area by province")

apart_loc_gard_area = locality_garden[locality_garden['type_of_property'] == 'apartment']
apart_loc_gard_area = apart_loc_gard_area.groupby('province').garden_area.describe()
apart_loc_gard_area.reset_index(level=0, inplace=True)
apart_loc_gard_area


apart_loc_gard_area.plot.bar(x = 'province', 
                        y = ['min', 'mean', '75%'],
                       figsize=(15,10),
                       title="min, mean and 75% of the apartment's garden's area by province")








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