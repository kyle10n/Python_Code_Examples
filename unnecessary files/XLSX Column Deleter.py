
import pandas as pd

#Ensure the python file is inside the folder with the xlsx files


#Name of xlsx files you want to "edit"

xlsx_names = ['FÅGEL;_KÖTT,_KORV;_STYCKNINGSDETALJER_2017-10-25_11-27-44.xlsx', 'Fisk;_Skaldjur_2017-10-25_11-27-10.xlsx',
              'Grönsaker_2017-10-25_11-25-03.xlsx', 'KÖTTALTERNATIV;_SVAMP;_BÄR_2017-10-25_11-27-36.xlsx',
              'Kryddor_&_Örter_2017-10-25_11-25-30.xlsx', 'LINSER;_BÖNOR;_LÖK_2017-10-25_11-27-22.xlsx',
              'Matfett;_Mejeri;_Ost;_Allmänt_2017-10-25_11-25-55.xlsx', 'Måltid_2017-10-25_11-26-31.xlsx',
              'NÖTTER,_FRÖN,_FRUKTER_2017-10-25_11-27-30.xlsx', 'Skafferiet_allmänt_2017-10-25_11-27-53.xlsx',
              'Skafferiet_mjöl;_Skafferiet_gryn_2017-10-25_11-27-16.xlsx', 'Tillagningssätt;_Egenskap_2017-10-25_11-26-14.xlsx',
              'Tillfälle_2017-10-25_11-26-21.xlsx', 'Typ_av_recept_allmän_2017-10-25_11-26-57.xlsx',
              'Typ_av_recept_pasta;_typ_av_recept_sås_2017-10-25_11-26-46.xlsx', 'Världens_kök;_Kockar_2017-10-25_11-26-02.xlsx']

for name in xlsx_names:
    df = pd.read_excel(name, sheetname = 1)
    #Columns you want to drop
    #Don't forget, Python Indexs from 0
    df.drop(df.columns[[0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8]], axis=1, inplace=True)
    df.to_excel(name, index = False)

