province_apart_sub = locality_subtype[locality_subtype['type_of_property'] == 'apartment']

anvers_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Anvers'].subtype_of_property.agg(['value_counts'])
anvers_apart_sub.reset_index(level=0, inplace=True)
anvers_apart_sub = anvers_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Anvers'})
anvers_apart_sub

bf_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Brabant Flamand'].subtype_of_property.agg(['value_counts'])
bf_apart_sub.reset_index(level=0, inplace=True)
bf_apart_sub = bf_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Brabant Flamand'})
bf_apart_sub
apart_subtype_province = pd.merge(anvers_apart_sub, bf_apart_sub, how = 'outer', on='Subtype')


bw_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Brabant Wallon'].subtype_of_property.agg(['value_counts'])
bw_apart_sub.reset_index(level=0, inplace=True)
bw_apart_sub = bw_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Brabant Wallon'})
bw_apart_sub
apart_subtype_province = pd.merge(apart_subtype_province, bw_apart_sub, how = 'outer', on='Subtype')

bxl_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Bruxelles'].subtype_of_property.agg(['value_counts'])
bxl_apart_sub.reset_index(level=0, inplace=True)
bxl_apart_sub = bxl_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Bruxelles'})
bxl_apart_sub
apart_subtype_province = pd.merge(apart_subtype_province, bxl_apart_sub, how = 'outer', on='Subtype')

focci_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Flandre-Occidentale'].subtype_of_property.agg(['value_counts'])
focci_apart_sub.reset_index(level=0, inplace=True)
focci_apart_sub = focci_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Flandre-Occidentale'})
focci_apart_sub
apart_subtype_province = pd.merge(apart_subtype_province, focci_apart_sub, how = 'outer', on='Subtype')

forient_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Flandre-Orientale'].subtype_of_property.agg(['value_counts'])
forient_apart_sub.reset_index(level=0, inplace=True)
forient_apart_sub = forient_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Flandre-Orientale'})
forient_apart_sub
apart_subtype_province = pd.merge(apart_subtype_province, forient_apart_sub, how = 'outer', on='Subtype')

hainaut_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Hainaut'].subtype_of_property.agg(['value_counts'])
hainaut_apart_sub.reset_index(level=0, inplace=True)
hainaut_apart_sub = hainaut_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Hainaut'})
hainaut_apart_sub
apart_subtype_province = pd.merge(apart_subtype_province, hainaut_apart_sub, how = 'outer', on='Subtype')

liege_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Liege'].subtype_of_property.agg(['value_counts'])
liege_apart_sub.reset_index(level=0, inplace=True)
liege_apart_sub = liege_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Liege'})
liege_apart_sub
apart_subtype_province = pd.merge(apart_subtype_province, liege_apart_sub, how = 'outer', on='Subtype')

limb_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Limbourg'].subtype_of_property.agg(['value_counts'])
limb_apart_sub.reset_index(level=0, inplace=True)
limb_apart_sub = limb_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Limbourg'})
limb_apart_sub
apart_subtype_province = pd.merge(apart_subtype_province, limb_apart_sub, how = 'outer', on='Subtype')

lux_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Luxembourg'].subtype_of_property.agg(['value_counts'])
lux_apart_sub.reset_index(level=0, inplace=True)
lux_apart_sub = lux_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Luxembourg'})
lux_apart_sub
apart_subtype_province = pd.merge(apart_subtype_province, lux_apart_sub, how = 'outer', on='Subtype')

namur_apart_sub = province_apart_sub[province_apart_sub['province'] == 'Namur'].subtype_of_property.agg(['value_counts'])
namur_apart_sub.reset_index(level=0, inplace=True)
namur_apart_sub = namur_apart_sub.rename(columns={'index':'Subtype', 'value_counts':'Namur'})
namur_apart_sub
apart_subtype_province = pd.merge(apart_subtype_province, namur_apart_sub, how = 'outer', on='Subtype')