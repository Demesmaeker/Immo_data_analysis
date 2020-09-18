import pandas as pd
df = pd.read_csv("dataset_house_apartment.csv")


nom_colonne = {}
for x in df.columns.tolist():
    nom_colonne[df.columns.tolist().index(x)] = x

    
    
def menu():
    
    y = -1
    
    choix_clean = []
    
    while y != "q":
        
        print(nom_colonne)
        y = input("que voulez-vous clean ? ( q => sortir  // a => tous)")
        try:
            y = int(y)
        except:
            if y == "a":
                for x in range(0,17):
                    choix_clean.append(x)
                break
            elif y == "q":
                break
            print("entrer une donnée valide")


        
        if y != "q":
            choix_clean.append(y)
    
    return choix_clean



def clean( df):
    
    df = pre_clean(df)
    choix_clean = menu()
    
    for x in choix_clean:
        
        print(nom_colonne[x] + " : nbr ligne = " + str(df.shape[0]))

        if x == 0: 
            pass
        elif x == 1: 
            df['province'] = df['locality'].apply(get_province)
            df["region"] = df['province'].apply(get_region)
        elif x == 2: pass
        elif x == 3:             
            df = df[(df.price != "no price")]
            df = df[df["price"] > 50000]
            print("removed price = 0")
            print("removed price under 50 000")
        elif x == 4: pass
        elif x == 5: 
            df = df[(df.house_area != 0)]
            print("removed house area = 0")
        elif x == 6: pass
        elif x == 7: pass
        elif x == 8: 
            df = df[(df.terrace == 0) | ((df.terrace == 1) & (df.terrace_area != 0))]
            print("removed terrace that exist = 0")
        elif x == 9: pass
        elif x == 10: 
            df = df[(df.garden == 0) | ((df.garden == 1) & (df.garden_area != 0))]
        elif x == 11: pass
        elif x == 12: 
            df = df[df.surface_of_the_land != 0]
            print("removed surface of the land = 0")
        elif x == 13: 
            df = df[df.number_of_facades != 0]
            print("removed facade = 0")
        elif x == 14: pass
        elif x == 15:
            df = df[df.state_of_the_building != 0]
        elif x == 16:
            df = df[df.construction_year != 0]
            
        else:
            continue

        print(df.shape[0])
        
        
    return df





def pre_clean(df):
    """
    Cleaning that don't remove row except for duplicate

    """ 
    df = df.drop(["furnished", "surface_of_the_plot_of_land", "type_of_sale"], axis=1)
    df = df.fillna("None")
    df = df.replace("None", 0)
    df.drop_duplicates()
    df = df.replace("no price", 0)
    print("changed \"no price\" to 0")
    df['garden_area'] = pd.to_numeric(df['garden_area'])
    df['house_area'] = pd.to_numeric(df['house_area'])
    df['terrace_area'] = pd.to_numeric(df['terrace_area'])
    df['construction_year'] = pd.to_numeric(df['construction_year'])
    df['number_of_facades'] = pd.to_numeric(df['number_of_facades'])
    df['price'] = pd.to_numeric(df['price'])
    df = df.replace("to be done up", "to renovate")
    df = df.replace("to restore", "to renovate")
    df[(df["type_of_property"] == 'apartment') & (df["surface_of_the_land"] == 0)].surface_of_the_land = df['house_area'] + df['terrace_area'] + df['garden_area']
    
    
    print("3 useless row deleted")
    print("None replaced by 0")
    print("duplicated row cleaned")
    print("string value changed to numeric")
    print("correlled renovation statut")
    
    return df





def get_province(locality):
    if locality < 1300:
        return "Bruxelles"
    elif locality < 1500:
        return "Brabant Wallon"
    elif locality < 2000:
        return "Brabant Flamand"
    elif locality < 3000:
        return "Anvers"
    elif locality < 3500:
        return "Brabant Flamand"
    elif locality < 4000:
        return "Limbourg"
    elif locality < 5000:
        return "Liege"
    elif locality < 6000:
        return "Namur"
    elif locality < 6600:
        return "Hainaut"
    elif locality < 7000:
        return "Luxembourg"
    elif locality < 8000:
        return "Hainaut"
    elif locality < 9000:
        return "Flandre-Occidentale"
    elif locality < 10000:
        return "Flandre-Orientale"



def get_region(province):
    if province == "Bruxelles":
        return "Region de Bruxelles-capitale"
    elif province in ["Brabant Wallon", "Liege", "Namur", "Hainaut", "Luxembourg"]:
        return "Region Wallonne"
    else:
        return "Region Flamande"
