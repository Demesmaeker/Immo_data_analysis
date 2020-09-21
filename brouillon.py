price_construction_year = clean(df, [0,1,3,19])

Working with 51.689 cleaned entries.


h_price_construction_year = price_construction_year[price_construction_year['type_of_property'] == 'house']
a_price_construction_year = price_construction_year[price_construction_year['type_of_property'] == 'apartment']


rf_h_price_construction_year = h_price_construction_year[h_price_construction_year['region']=='Region Flamande'].loc[:,['price', 'construction_year']]
rf_h_price_construction_year.corr()

bxl_h_price_construction_year = h_price_construction_year[h_price_construction_year['region']=='Region de Bruxelles-capitale'].loc[:,['price', 'construction_year']]
bxl_h_price_construction_year.corr()

rw_h_price_construction_year = h_price_construction_year[h_price_construction_year['region']=='Region Wallonne'].loc[:,['price', 'construction_year']]
rw_h_price_construction_year.corr()

rf_a_price_construction_year = a_price_construction_year[a_price_construction_year['region']=='Region Flamande'].loc[:,['price', 'construction_year']]
rf_a_price_construction_year.corr()

bxl_a_price_construction_year = a_price_construction_year[a_price_construction_year['region']=='Region de Bruxelles-capitale'].loc[:,['price', 'construction_year']]
bxl_a_price_construction_year.corr()

rw_a_price_construction_year = a_price_construction_year[a_price_construction_year['region']=='Region Wallonne'].loc[:,['price', 'construction_year']]
rw_a_price_construction_year.corr()