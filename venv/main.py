
import pandas as pd

# abir archivo 
archivo_json = 'E:/Mis documentos/henry/proyecto_final_1_reaload/venv/Include/output_steam_games.json'

# Carga el archivo JSON en un DataFrame
df_juegos = pd.read_json(archivo_json, lines=True)


def clean_df_juegos(df_juegos):
    
    # Drop rows with missing data across all columns
    df_juegos = df_juegos.dropna()
    # Drop column: 'url'
    df_juegos = df_juegos.drop(columns=['url'])
    # Drop column: 'price'
    df_juegos = df_juegos.drop(columns=['price'])
    # Drop column: 'early_access'
    df_juegos = df_juegos.drop(columns=['early_access'])
    # Drop column: 'reviews_url'
    df_juegos = df_juegos.drop(columns=['reviews_url'])
    # Sort by column: 'release_date' (ascending)
    df_juegos = df_juegos.sort_values(['release_date'])
    # Sort by column: 'release_date' (descending)
    df_juegos = df_juegos.sort_values(['release_date'], ascending=[False])
    # Replace all instances of "Sep 2014" with "2014-09-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Sep 2014", "2014-09-01", case=False, regex=False)
    # Replace all instances of "Sep 2009" with "2009-09-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Sep 2009", "2009-09-01", case=False, regex=False)
    # Replace all instances of "SOON™" with "2025-01-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("SOON™", "2025-01-01", case=False, regex=False)
    # Replace all instances of "SOON" with "2025-01-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("SOON", "2025-01-01", case=False, regex=False)
    # Replace all instances of "Oct 2016" with "2016-10-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Oct 2016", "2016-10-01", case=False, regex=False)
    # Replace all instances of "Oct 2010" with "2010-10-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Oct 2010", "2010-10-01", case=False, regex=False)
    # Replace all instances of "Oct 2009" with "2009-10-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Oct 2009", "2009-10-01", case=False, regex=False)
    # Replace all instances of "Nov 2016" with "2016-11-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Nov 2016", "2016-11-01", case=False, regex=False)
    # Replace all instances of "Nov 2014" with "2014-11-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Nov 2014", "2014-11-01", case=False, regex=False)
    # Replace all instances of "May 2015" with "2015-05-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("May 2015", "2015-05-01", case=False, regex=False)
    # Replace all instances of "May 2014" with "2014-05-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("May 2014", "2014-05-01", case=False, regex=False)
    # Replace all instances of "Mar 2010" with "2010-03-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Mar 2010", "2010-03-01", case=False, regex=False)
    # Replace all instances of "Jun 2016" with "2016-06-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jun 2016", "2016-06-01", case=False, regex=False)
    # Replace all instances of "Jun 2015" with "2015-06-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jun 2015", "2015-06-01", case=False, regex=False)
    # Replace all instances of "Jun 2009" with "2009-06-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jun 2009", "2009-06-01", case=False, regex=False)
    # Replace all instances of "Jul 2017" with "2017-07-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jul 2017", "2017-07-01", case=False, regex=False)
    # Replace all instances of "Jul 2016" with "2016-07-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jul 2016", "2016-07-01", case=False, regex=False)
    # Replace all instances of "Jul 2014" with "2014-07-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jul 2014", "2014-07-01", case=False, regex=False)
    # Replace all instances of "Jul 2010" with "2010-07-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jul 2010", "2010-07-01", case=False, regex=False)
    # Replace all instances of "Jan 2017" with "2017-01-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jan 2017", "2017-01-01", case=False, regex=False)
    # Replace all instances of "Jan 2015" with "2015-01-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jan 2015", "2015-01-01", case=False, regex=False)
    # Replace all instances of "Jan 2010" with "2010-01-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jan 2010", "2010-01-01", case=False, regex=False)
    # Replace all instances of "Feb 2013" with "2013-02-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Feb 2013", "2013-02-01", case=False, regex=False)
    # Replace all instances of "Feb 2011" with "2011-02-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Feb 2011", "2011-02-01", case=False, regex=False)
    # Replace all instances of "Dec 2012" with "2012-12-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Dec 2012", "2012-12-01", case=False, regex=False)
    # Replace all instances of "Aug 2015" with "2015-08-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Aug 2015", "2015-08-01", case=False, regex=False)
    # Replace all instances of "Aug 2014" with "2014-08-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Aug 2014", "2014-08-01", case=False, regex=False)
    # Replace all instances of "Apr 2017" with "2017-04-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Apr 2017", "2017-04-01", case=False, regex=False)
    # Replace all instances of "Apr 2016" with "2016-04-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Apr 2016", "2016-04-01", case=False, regex=False)
    # Replace all instances of "Jun 2009" with "2009-06-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jun 2009", "2009-06-01", case=False, regex=False)
    # Replace all instances of "Jun 2009" with "2009-06-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jun 2009", "2009-06-01", case=False, regex=False)
    # Replace all instances of "Oct 2010" with "2010-10-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Oct 2010", "2010-10-01", case=False, regex=False)
    # Replace all instances of "Feb 2011" with "2011-02-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Feb 2011", "2011-02-01", case=False, regex=False)
    # Replace all instances of "Sep 2014" with "201-09-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Sep 2014", "2014-09-01", case=False, regex=False)
    # Replace all instances of "Apr 2016" with "2016-04-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Apr 2016", "2016-04-01", case=False, regex=False)
    # Replace all instances of "Jul 2017" with "2017-07-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("Jul 2017", "2017-07-01", case=False, regex=False)
    # Replace all instances of "SOON" with "2025-01-01" in column: 'release_date'
    df_juegos['release_date'] = df_juegos['release_date'].str.replace("SOON", "2025-01-01", case=False, regex=False)
    # Filter rows based on column: 'release_date'
    df_juegos = df_juegos[~(df_juegos['release_date'] == "2018")]
    # Split text using string '-' in column: 'release_date'
    loc_0 = df_juegos.columns.get_loc('release_date')
    df_juegos_split = df_juegos['release_date'].str.split(pat='-', expand=True).add_prefix('release_date_')
    df_juegos = pd.concat([df_juegos.iloc[:, :loc_0], df_juegos_split, df_juegos.iloc[:, loc_0:]], axis=1)
    df_juegos = df_juegos.drop(columns=['release_date'])
    # Rename column 'release_date_0' to 'release_date_anio'
    df_juegos = df_juegos.rename(columns={'release_date_0': 'release_date_anio'})
    # Rename column 'release_date_1' to 'release_date_mes'
    df_juegos = df_juegos.rename(columns={'release_date_1': 'release_date_mes'})
    # Rename column 'release_date_2' to 'release_date_dia'
    df_juegos = df_juegos.rename(columns={'release_date_2': 'release_date_dia'})

    # reset index
    df_juegos = df_juegos.reset_index(drop=True)
    
    return df_juegos

df_juegos= clean_df_juegos(df_juegos)
