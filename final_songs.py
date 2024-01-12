def parse_file(filename): 
    
    """Parses a desired file by opening it, reading line by line and adding it into a unique table.
    Parameters: filename, a string
    Returns: A table that contains each row of a file in a form of a list.
    Preconditions: Filename has to be a file.
    Postconditions: /"""
    fin = open(filename, encoding="utf-8") # File that we intend to open.
    fin.readline()
    table=[]                               # List that we append the rows of the table to.
    for line in fin:
        line=line.strip()
        table.append(line.split(','))
    fin.close()
    return table

def get_title(row):
    """Gets the title column from a certain row of the table.
Parameters: row, a list
Returns: a string, a title of the song from the desired row
Preconditions: row has to be a list and a row in the table
Postconditions/"""

    return row[1]

def get_artist(row):
    
    """Gets the artist column from a certain row of the table.
    Parameters: row, a list
    Returns: a string, a name of the artist of the song from the desired row
    Preconditions: row has to be a list and a row in the table
    Postconditions/"""
    return row[2]

def get_genre(row):
    """Gets the genre column from a certain row of the table.
    Parameters: row, a list 
    Returns: a string, a genre of the song from the desired row
    Preconditions: row has to be a list and a row in the table
    Postconditions/"""
    return row[3]

def get_year(row):
    """Gets the year column from a certain row of the table.
    Parameters: row, a list 
    Returns: an integer, a year of the song from the desired row
    Preconditions: row has to be a list and a row in the table
    Postconditions/"""
    return (row[4])

def get_dance(row):
    """Gets the danceability column from a certain row of the table.
    Parameters: row, a list 
    Returns: an integer, a level of danceability of the song from the desired row
    Preconditions: row has to be a list and a row in the table
    Postconditions/"""
    return int(row[7])

def get_bpm(row):
    """Gets the bpm column from a certain row of the table.
    Parameters: row, a list 
    Returns: an integer, tempo (bpm) of the song from the desired row
    Preconditions: row has to be a list and a row in the table
    Postconditions/"""
    return int(row[5])

def get_liveness(row):
    """Gets the liveness column from a certain row of the table.
    Parameters: row, a list 
    Returns: an integer, a level of liveness of the song from the desired row
    Preconditions: row has to be a list and a row in the table
    Postconditions/"""
    return int(row[9])

def get_valence(row):
    """Gets the valence column from a certain row of the table.
    Parameters: row, a list 
    Returns: an integer, a level of valence of the song from the desired row
    Preconditions: row has to be a list and a row in the table
    Postconditions/"""
    return int(row[10])

def get_acc(row): # acc stands for acousticness
    """Gets the acousticness column from a certain row of the table.
    Parameters: row, a list 
    Returns: an integer, a level of acousticness of the song from the desired row
    Preconditions: row has to be a list and a row in the table
    Postconditions/"""
    return int(row[12])



def filter_genre(table, genre):
    """Filters the given table by the desired genre.
Parameters:
table: a list
genre: a string that gives the genre that we want to filter the table by
Returns: a list of the rows in the table that fall under the desired genre
Preconditions: table has to be a list
genre has to be a string
Postconditions: /"""
    return [row for row in table if get_genre(row) == genre]


def filter_year(table,year):
    """Filters the given table by the desired year.
Parameters:
table: a list
year: an integer that gives the year that we want to filter the table by
Returns: a list of the rows in the table that fall under the desired year
Preconditions: table has to be a list
genre has to be an integer
Postconditions: /"""
    return [row for row in table if get_year(row) ==year]

def filter_artist(table,artist):
    """Filters the given table by the desired artist.
Parameters:
table: a list
artist: a string that gives the artist that we want to filter the table by
Returns: a list of the rows in the table that fall under the desired artist
Preconditions: table has to be a list
artist has to be a string
Postconditions: /"""
    
    return [row for row in table if get_artist(row) == artist]


tempos = {}
def group_by_tempo(table):
    """Groups the values in the given table based on whether they present a slow,medium or fast tempo.
Parameters:
table: a list
Returns: a globaly defined dicitionary with the keys slow,medium and fast.
Preconditions: table has to be a list
Postconditions:
if  60<tempo<105, tempo is classified as slow
if 105<=tempo<150, tempo is classified as medium
if 150<tempo, tempo is classified as fast
"""
    tempos['slow'] = lst1 = []
    tempos['medium'] = lst2 = []
    tempos['fast'] = lst3 = []
    for row in table:
        if 60<get_bpm(row)<105:
            lst1.append(row)
        elif 105<=get_bpm(row)<150:
            lst2.append(row)
        else:
            lst3.append(row)
    return tempos

dance = {}
def group_by_dance(table):
    """Groups the values in the given table based on whether they present a bad,medium or good danceability.
Parameters:
table: a list
Returns: a globaly defined dicitionary with the keys bad,med(medium) and good.
Preconditions: table has to be a list
Postconditions:
if  0<danceability<33, danceability is classified as bad
if 33<=danceability<66, danceability is classified as medium
if 66<danceability, danceability is classified as good
"""
    
    dance['bad'] = lst1 = []
    dance['med'] = lst2 = []
    dance['good'] = lst3 = []
    for row in table:
        if 0<get_dance(row)<33:
            lst1.append(row)
        elif 33<=get_dance(row)<66:
            lst2.append(row)
        else:
            lst3.append(row)
    return dance
            
live = {}
"""Groups the values in the given table based on whether they present a song that sounds like a live performance or not.
Parameters:
table: a list
Returns: a globaly defined dicitionary with the keys n_live(doesn't sound like a live performance) and live(sounds like a live performance.).
Preconditions: table has to be a list
Postconditions:
if  0<liveness<50, liveness is classified as n_live
if 66<liveness, liveness is classified as live
"""
def group_by_liveness(table):
    live['n_live'] = lst1 = []
    live['live'] = lst2 = []
    for row in table:
        if 0<get_liveness(row)<50:
            lst1.append(row)
        else:
            lst2.append(row)
    return live

acoustic={}
def group_by_acoustic(table):
    """Groups the values in the given table based on whether they present a low,moderate or good high acousticness.
Parameters:
table: a list
Returns: a globaly defined dicitionary with the keys low, moderate and high.
Preconditions: table has to be a list
Postconditions:
if  0<acousticness<33, acousticness is classified as low
if 33<=acousticness<66, acousticness is classified as moderate
if 66<acousticness, acousticness is classified as high
"""
    acoustic['low'] = lst1 = []
    acoustic['moderate'] = lst2 = []
    acoustic['high'] = lst3 = []
    for row in table:
        if 0<get_acc(row)<33:
            lst1.append(row)
        elif 33<=get_acc(row)<66:
            lst2.append(row)
        else:
            lst3.append(row)
    return acoustic

valence={}
def group_by_valence(table):
    """Groups the values in the given table based on the level of positive emotions they reinforce.
Parameters:
table: a list
Returns: a globaly defined dicitionary with the keys sad, neutral and happy.
Preconditions: table has to be a list
Postconditions:
if  0<valence<33, valence is classified as sad
if 33<=valence<66, valence is classified as neutral
if 66<valence, valence is classified as happy
"""
    
    
    valence['sad'] = lst1 = []
    valence['neutral'] = lst2 = []
    valence['happy'] = lst3 = []
    for row in table:
        if 0<get_valence(row)<33:
            lst1.append(row)
        elif 33<=get_valence(row)<66:
            lst2.append(row)
        else:
            lst3.append(row)
    return valence



def main():
    import random
    
    
    decade = int(input("Choose a decade from 1950 to 2010:"))
    if decade ==1950:
        t = parse_file('1950.csv')
        
    elif decade ==1960:
        t = parse_file('1960.csv')
        
    elif decade ==1970:
        t = parse_file('1970.csv')
           
    elif decade ==1980:
        t = parse_file('1980.csv')
        
    elif decade ==1990:
        t = parse_file('1990.csv')
        
    elif decade ==2000:
        t = parse_file('2000.csv')
        
    elif decade == 2010: 
        t = parse_file('2010.csv')
        
    else:
        print("This decade is not available in our datatbase")
    
    x = (input('Select by which categories you want to narrow your search by: Artist/Genre/Release year/Tempo/Danceability/Valence/Liveness/Acousticness:\n'))
    preference = x
   
        
    f1=[]
    if 'artist' in preference.lower():
        e=input('Choose an artist: ')
        f1.append(filter_artist(t,e))
    
    f2=[]
    if 'genre' in preference.lower():
        c=input('Choose a genre: ')
        f2.append(filter_genre(t,c))
        
        
    f3=[]   
    if 'year' in preference.lower():
        f=input('Choose a year: ')
        f3.append(filter_year(t,f))
       
    f4=[]
    if 'tempo' in preference.lower():
        group_by_tempo(t)
        i=input('Choose from slow/medium/fast/ tempo: ')
        if i=='slow':
            f4.append(tempos['slow'])
            
            
        elif i=='medium':
            f4.append(tempos['medium'])
            
        elif i=='fast':
            f4.append(tempos['fast'])
        else:
            print('There are no songs in our dataset with that tempo.')
        
    f5=[]    
    if 'danceability' in preference.lower():
        group_by_dance(t)
        b=input('Choose from Not danceable/Danceable/Very danceable: ')
        if b=='Not danceable':
            f5.append(dance['bad'])
            
        elif b=='Danceable':
            f5.append(dance['med'])
            
        elif b=='Very danceable':
            f5.append(dance['good'])
        else:
            print('There are no songs in our dataset with that danceability.')
            
     
        
        
    f6=[]
    if 'valence' in preference.lower():
        group_by_valence(t)
        d=input('Choose from Sad/Neutral/Happy/ valence: ')
        if d=='Sad':
            f6.append(valence['sad'])
            
            
        elif d=='Neutral':
            f6.append(valence['neutral'])
            
        elif d=='Happy':
            f6.append(valence['happy'])
        else:
            print('There are no songs in our dataset with that valence.')
            
    f7 = []
    if 'liveness' in preference.lower():
        group_by_liveness(t)
        h = input('Choose from Not live/Live feel:')
        if h == 'Not live':
            f7.append(live['n_live'])
            
        elif h == 'Live feel':
            f7.append(live['live'])
            
        else:
            print('There are no songs in our dataset with liveness.')
            
 
       
   
       
           
    f8=[]   
    if 'acousticness' in preference.lower():
        group_by_acoustic(t)
        g=input('Choose from Low/Medium/High ,acousticness: ')
        if g=='Low':
            f8.append(acoustic['low'])
           
        elif g=='Medium':
            f8.append(acoustic['moderate'])
           
        elif g=='High':
            f8.append(acoustic['high'])
        else:
            print('There are no songs in our dataset with that acousticness.')
        

    final=[]  

    if f1:
        final.append(random.choice(f1))
    if f2:
        final.append(random.choice(f2))
    if f3:
        final.append(random.choice(f3))
    if f4:
        final.append(random.choice(f4))
    if f5:
        final.append(random.choice(f5))
    if f6:
        final.append(random.choice(f6))
    if f7:
        final.append(random.choice(f7))
    if f8:
        final.append(random.choice(f8))
    if len(final)==0:
        print('There are no songs in our database with that preference.')
    else:
        y=[]
        rate=0
        while len(y)<5:
            song=random.choice(final[random.randint(0,len(final)-1)])
            if song not in y:
                print(get_title(song), end='')
                print(',', end=' ')
                print(get_artist(song))
                y.append(song)
                rating=int(input('Rate this song from 1-5:'))
                rate+=rating
        print('The accuracy of our program for this sample of songs is:',(rate/25)*100,'%')
        
            
        

        

 
        
    
            
    
        
        

        
    
    
    
main()
