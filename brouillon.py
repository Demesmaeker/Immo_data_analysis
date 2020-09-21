price_kitchen = clean(df, [0,1,3,5])

Working with 51.689 cleaned entries.


h_price_kitchen = price_kitchen[price_kitchen['type_of_property'] == 'house']
a_price_kitchen = price_kitchen[price_kitchen['type_of_property'] == 'apartment']


rf_h_price_kitchen = h_price_kitchen[h_price_kitchen['region']=='Region Flamande'].loc[:,['price', 'fully_equipped_kitchen']]
rf_h_price_kitchen.corr()

bxl_h_price_kitchen = h_price_kitchen[h_price_kitchen['region']=='Region de Bruxelles-capitale'].loc[:,['price', 'fully_equipped_kitchen']]
bxl_h_price_kitchen.corr()

rw_h_price_kitchen = h_price_kitchen[h_price_kitchen['region']=='Region Wallonne'].loc[:,['price', 'fully_equipped_kitchen']]
rw_h_price_kitchen.corr()

rf_a_price_kitchen = a_price_kitchen[a_price_kitchen['region']=='Region Flamande'].loc[:,['price', 'fully_equipped_kitchen']]
rf_a_price_kitchen.corr()

bxl_a_price_kitchen = a_price_kitchen[a_price_kitchen['region']=='Region de Bruxelles-capitale'].loc[:,['price', 'fully_equipped_kitchen']]
bxl_a_price_kitchen.corr()

rw_a_price_kitchen = a_price_kitchen[a_price_kitchen['region']=='Region Wallonne'].loc[:,['price', 'fully_equipped_kitchen']]
rw_a_price_kitchen.corr()