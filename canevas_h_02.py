dataframes = []
for element in [0.0,
                1.0,
                2.0,
                3.0,
                4.0,
                5.0,
                6.0,
                7.0,
                8.0,
                9.0,
                10.0,
                11.0,
                12.0,
                13.0,
                14.0,
                15.0,
                16.0,
                17.0,
                18.0,
                19.0,
                20.0,
                22.0,
                23.0,
                24.0,
                30.0,
                165.0]:
    dataframe = house_loc_bedrooms[house_loc_bedrooms['number_of_rooms'] == element].province.agg(['value_counts'])
    dataframe.reset_index(level=0, inplace=True)
    dataframe = dataframe.rename(columns={'index':'Province', 'value_counts':element})
    dataframes.append(dataframe)

house_province_bedrooms = pd.merge(dataframes[0], dataframes[1], how = 'outer', on='Province')

for i in range(2, len(dataframes)):
    house_province_bedrooms = pd.merge(house_province_bedrooms, dataframes[i], how = 'outer', on='Province')

house_province_bedrooms








house_province_bedrooms.plot.bar(x = 'Province', 
                                y = [0.0,
                                    1.0,
                                    2.0,
                                    3.0,
                                    4.0,
                                    5.0
                                   ],
                               logy=True,
                               figsize=(15,10),
                               title="Number of houses by province for each bedrooms : part 1")


house_province_bedrooms.plot.bar(x = 'Province', 
                                y = [6.0,
                                    7.0,
                                    8.0,
                                    9.0,
                                    10.0
                                   ],
                               logy=True,
                               figsize=(15,10),
                               title="Number of houses by province for each bedrooms : part 1")


house_province_bedrooms.plot.bar(x = 'Province', 
                                y = [10.0,
                                    11.0,
                                    12.0,
                                    13.0,
                                    14.0,
                                    15.0,
                                    16.0,
                                    17.0,
                                    18.0,
                                    19.0
                                   ],
                               logy=True,
                               figsize=(15,10),
                               title="Number of houses by province for each bedrooms : part 3")


house_province_bedrooms.plot.bar(x = 'Province', 
                                y = [20.0,
                                    22.0,
                                    23.0,
                                    24.0,
                                    30.0,
                                    165.0
                                   ],
                               logy=True,
                               figsize=(15,10),
                               title="Number of houses by province for each bedrooms : part 3")