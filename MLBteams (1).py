from tkinter import *

root = Tk()
root.title("MLB Prediction program")
picking=True
def get_players():
    global picking
    picking=False
    if tkvar1.get()=='Arizona Diamondbacks':
        hitters_list1=diamondbacks_hitters
        pitchers_list1=diamondbacks_pitchers
    elif tkvar1.get()=='Atlanta Braves':
        hitters_list1=braves_hitters
        pitchers_list1=braves_pitchers
    elif tkvar1.get()=='Baltimore Orioles':
        hitters_list1=orioles_hitters
        pitchers_list1=orioles_pitchers
    elif tkvar1.get()=='Boston Red Sox':
        hitters_list1=redsox_hitters
        pitchers_list1=redsox_pitchers
    elif tkvar1.get()=='Chicago Cubs':
        hitters_list1=cubs_hitters
        pitchers_list1=cubs_pitchers
    elif tkvar1.get()=='Chicago White Sox':
        hitters_list1=whitesox_hitters
        pitchers_list1=whitesox_pitchers
    elif tkvar1.get()=='Cincinnati Reds':
        hitters_list1=reds_hitters
        pitchers_list1=reds_pitchers
    elif tkvar1.get()=='Cleveland Indians':
        hitters_list1=indians_hitters
        pitchers_list1=indians_pitchers
    elif tkvar1.get()=='Colorado Rockies':
        hitters_list1=rockies_hitters
        pitchers_list1=rockies_pitchers
    elif tkvar1.get()=='Detroit Tigers':
        hitters_list1=tigers_hitters
        pitchers_list1=tigers_pitchers
    elif tkvar1.get()=='Houston Astros':
        hitters_list1=astros_hitters
        pitchers_list1=astros_pitchers
    elif tkvar1.get()=='Kansas City Royals':
        hitters_list1=royals_hitters
        pitchers_list1=royals_pitchers
    elif tkvar1.get()=='Los Angeles Angels':
        hitters_list1=angels_hitters
        pitchers_list1=angels_pitchers
    elif tkvar1.get()=='Los Angeles Dodgers':
        hitters_list1=dodgers_hitters
        pitchers_list1=dodgers_pitchers
    elif tkvar1.get()=='Miami Marlins':
        hitters_list1=marlins_hitters
        pitchers_list1=marlins_pitchers
    elif tkvar1.get()=='Milwaukee Brewers':
        hitters_list1=brewers_hitters
        pitchers_list1=brewers_pitchers
    elif tkvar1.get()=='Minnesota Twins':
        hitters_list1=twins_hitters
        pitchers_list1=twins_pitchers
    elif tkvar1.get()=='New York Mets':
        hitters_list1=mets_hitters
        pitchers_list1=mets_pitchers
    elif tkvar1.get()=='New York Yankees':
        hitters_list1=yankees_hitters
        pitchers_list1=yankees_pitchers
    elif tkvar1.get()=='Oakland Athletics':
        hitters_list1=athletics_hitters
        pitchers_list1=athletics_pitchers
    elif tkvar1.get()=='Philadelphia Phillies':
        hitters_list1=phillies_hitters
        pitchers_list1=phillies_pitchers
    elif tkvar1.get()=='Pittsburgh Pirates':
        hitters_list1=pirates_hitters
        pitchers_list1=pirates_pitchers
    elif tkvar1.get()=='San Diego Padres':
        hitters_list1=padres_hitters
        pitchers_list1=padres_pitchers
    elif tkvar1.get()=='San Francisco Giants':
        hitters_list1=giants_hitters
        pitchers_list1=giants_pitchers
    elif tkvar1.get()=='Seattle Mariners':
        hitters_list1=mariners_hitters
        pitchers_list1=mariners_pitchers
    elif tkvar1.get()=='St. Louis Cardinals':
        hitters_list1=cardinals_hitters
        pitchers_list1=cardinals_pitchers
    elif tkvar1.get()=='Tampa Bay Rays':
        hitters_list1=rays_hitters
        pitchers_list1=rays_pitchers
    elif tkvar1.get()=='Texas Rangers':
        hitters_list1=rangers_hitters
        pitchers_list1=rangers_pitchers
    elif tkvar1.get()=='Toronto Blue Jays':
        hitters_list1=bluejays_hitters
        pitchers_list1=bluejays_pitchers
    elif tkvar1.get()=='Washington Nationals':
        hitters_list1=nationals_hitters
        pitchers_list1=nationals_pitchers
    if tkvar2.get()=='Arizona Diamondbacks':
        hitters_list2=diamondbacks_hitters
        pitchers_list2=diamondbacks_pitchers
    elif tkvar2.get()=='Atlanta Braves':
        hitters_list2=braves_hitters
        pitchers_list2=braves_pitchers
    elif tkvar2.get()=='Baltimore Orioles':
        hitters_list2=orioles_hitters
        pitchers_list2=orioles_pitchers
    elif tkvar2.get()=='Boston Red Sox':
        hitters_list2=redsox_hitters
        pitchers_list2=redsox_pitchers
    elif tkvar2.get()=='Chicago Cubs':
        hitters_list2=cubs_hitters
        pitchers_list2=cubs_pitchers
    elif tkvar2.get()=='Chicago White Sox':
        hitters_list2=whitesox_hitters
        pitchers_list2=whitesox_pitchers
    elif tkvar2.get()=='Cincinnati Reds':
        hitters_list2=reds_hitters
        pitchers_list2=reds_pitchers
    elif tkvar2.get()=='Cleveland Indians':
        hitters_list2=indians_hitters
        pitchers_list2=indians_pitchers
    elif tkvar2.get()=='Colorado Rockies':
        hitters_list2=rockies_hitters
        pitchers_list2=rockies_pitchers
    elif tkvar2.get()=='Detroit Tigers':
        hitters_list2=tigers_hitters
        pitchers_list2=tigers_pitchers
    elif tkvar2.get()=='Houston Astros':
        hitters_list2=astros_hitters
        pitchers_list2=astros_pitchers
    elif tkvar2.get()=='Kansas City Royals':
        hitters_list2=royals_hitters
        pitchers_list2=royals_pitchers
    elif tkvar2.get()=='Los Angeles Angels':
        hitters_list2=angels_hitters
        pitchers_list2=angels_pitchers
    elif tkvar2.get()=='Los Angeles Dodgers':
        hitters_list2=dodgers_hitters
        pitchers_list2=dodgers_pitchers
    elif tkvar2.get()=='Miami Marlins':
        hitters_list2=marlins_hitters
        pitchers_list2=marlins_pitchers
    elif tkvar2.get()=='Milwaukee Brewers':
        hitters_list2=brewers_hitters
        pitchers_list2=brewers_pitchers
    elif tkvar2.get()=='Minnesota Twins':
        hitters_list2=twins_hitters
        pitchers_list2=twins_pitchers
    elif tkvar2.get()=='New York Mets':
        hitters_list2=mets_hitters
        pitchers_list2=mets_pitchers
    elif tkvar2.get()=='New York Yankees':
        hitters_list2=yankees_hitters
        pitchers_list2=yankees_pitchers
    elif tkvar2.get()=='Oakland Athletics':
        hitters_list2=athletics_hitters
        pitchers_list2=athletics_pitchers
    elif tkvar2.get()=='Philadelphia Phillies':
        hitters_list2=phillies_hitters
        pitchers_list2=phillies_pitchers
    elif tkvar2.get()=='Pittsburgh Pirates':
        hitters_list2=pirates_hitters
        pitchers_list2=pirates_pitchers
    elif tkvar2.get()=='San Diego Padres':
        hitters_list2=padres_hitters
        pitchers_list2=padres_hitters
    elif tkvar2.get()=='San Francisco Giants':
        hitters_list2=giants_hitters
        pitchers_list2=giants_pitchers
    elif tkvar2.get()=='Seattle Mariners':
        hitters_list2=mariners_hitters
        pitchers_list2=mariners_pitchers
    elif tkvar2.get()=='St. Louis Cardinals':
        hitters_list2=cardinals_hitters
        pitchers_list2=cardinals_pitchers
    elif tkvar2.get()=='Tampa Bay Rays':
        hitters_list2=rays_hitters
        pitchers_list2=rays_pitchers
    elif tkvar2.get()=='Texas Rangers':
        hitters_list2=rangers_hitters
        pitchers_list2=rangers_pitchers
    elif tkvar2.get()=='Toronto Blue Jays':
        hitters_list2=bluejays_hitters
        pitchers_list2=bluejays_pitchers
    elif tkvar2.get()=='Washington Nationals':
        hitters_list2=nationals_hitters
        pitchers_list2=nationals_pitchers
        

def calculate_percentage():
    root.title(100)
# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)


# Create a Tkinter variable
tkvar1 = StringVar(root)
tkvar2=StringVar(root)
tkvar3 = StringVar(root)
tkvar4=StringVar(root)
tkvar5 = StringVar(root)
tkvar6=StringVar(root)
tkvar7 = StringVar(root)
tkvar8=StringVar(root)
tkvar9 = StringVar(root)
tkvar10=StringVar(root)
tkvar11 = StringVar(root)
tkvar12=StringVar(root)
tkvar13 = StringVar(root)
tkvar14=StringVar(root)
tkvar15 = StringVar(root)
tkvar16=StringVar(root)
tkvar17 = StringVar(root)
tkvar18=StringVar(root)
tkvar19 = StringVar(root)
tkvar20=StringVar(root)
tkvar21 = StringVar(root)
tkvar22=StringVar(root)





# Dictionary with options
MLBteams1 = {'Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox', 'Chicago Cubs', 'Chicago White Sox', 'Cincinnati Reds', 'Cleveland Indians', 'Colorado Rockies', 'Detroit Tigers', 'Houston Astros', 'Kansas City Royals', 'Los Angeles Angels', 'Los Angeles Dodgers', 'Miami Marlins', 'Milwaukee Brewers', 'Minnesota Twins', 'New York Mets', 'New York Yankees', 'Oakland Athletics', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 'San Francisco Giants', 'Seattle Mariners', 'St. Louis Cardinals', 'Tampa Bay Rays', 'Texas Rangers', 'Toronto Blue Jays', 'Washington Nationals'}
MLBteams2={'Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox', 'Chicago Cubs', 'Chicago White Sox', 'Cincinnati Reds', 'Cleveland Indians', 'Colorado Rockies', 'Detroit Tigers', 'Houston Astros', 'Kansas City Royals', 'Los Angeles Angels', 'Los Angeles Dodgers', 'Miami Marlins', 'Milwaukee Brewers', 'Minnesota Twins', 'New York Mets', 'New York Yankees', 'Oakland Athletics', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 'San Francisco Giants', 'Seattle Mariners', 'St. Louis Cardinals', 'Tampa Bay Rays', 'Texas Rangers', 'Toronto Blue Jays', 'Washington Nationals'}
tkvar1.set('Arizona Diamondbacks') # set the default option
tkvar2.set('Arizona Diamondbacks')
bluejays_hitters={'Danny Jensen', 'Reese McGuire', 'Travis Shaw', 'Cavan Biggio', 'Bo Bichette', 'Vladmir Guerrero Jr.', 'Brandon Drury', 'Rowdy Tellez', 'Teoscar Hernandez', 'Randal Grichuk', 'Lourdes Gurriel Jr.', 'Derek Fisher', 'Billy McKinney', 'Hyun-Jin Ryu', 'Tanner Roark', 'Matt Shoemaker', 'Chase Anderson', 'Shun Yamaguchi', 'Other'}
bluejays_pitchers={'Hyun-Jin Ryu', 'Tanner Roark', 'Matt Shoemaker', 'Chase Anderson', 'Shun Yamaguchi', 'Other'}
orioles_hitters={'Pedro Severino', 'Chance Sisco', 'Chris Davis', 'Hanser Alberto', 'Jose Iglesias', 'Rio Ruiz', 'Renato Nunez', 'Stevie Wilkerson', 'Richard Urena', 'Trey Mancini', 'Austin Hays', 'Anthony Santander', 'Dwight Smith Jr.', 'John Means', 'Alex Cobb', 'Kohl Stewart', 'Asher Wojciechowski', 'Keegan Akin', 'Other'}
orioles_pitchers={'John Means', 'Alex Cobb', 'Kohl Stewart', 'Asher Wojciechowski', 'Keegan Akin', 'Other'}
rays_hitters={'Mike Zunino', 'Ji-Man Choi', 'Jose Martinez', 'Brandon Lowe', 'Joey Wendle', 'Willy Adames', 'Yandy Diaz', 'Kevin Kiermaier', 'Austin Meadows', 'Hunter Renfroe', 'Yoshitomo Tsutsugo', 'Randy Arozarena', 'Michael Perez', 'Blake Snell', 'Tyler Glasnow', 'Charlie Morton', 'Ryan Yarbrough', 'Yonny Chirinos', 'Other'}
rays_pitchers={'Blake Snell', 'Tyler Glasnow', 'Charlie Morton', 'Ryan Yarbrough', 'Yonny Chirinos', 'Other'}
redsox_hitters={'Christian Vazquez', 'Kevin Plawecki', 'Michael Chavis', 'Jose Peraza', 'Xander Bogaerts', 'Rafael Devers', 'Andrew Benintendi', 'Jackie Bradley Jr.', 'J.D. Martinez', 'Bobby Dalbec', 'Marco Hernandez', 'Jonathan Arauz', 'Chris Sale', 'Eduardo Rodriguez', 'Nathan Eovaldi', 'Martin Perez', 'Other'}
redsox_pitchers={'Chris Sale', 'Eduardo Rodriguez', 'Nathan Eovaldi', 'Martin Perez', 'Other'}
yankees_hitters={'Gary Sanchez', 'Luke Voit', 'DJ LeMahieu', 'Gleyber Torres', 'Gio Urshela', 'Brett Gardner', 'Aaron Judge', 'Giancarlo Stanton', 'Kyle Higashioka', 'Mike Ford', 'Mike Tauchman', 'Clint Frazier', 'Miguel Andujar', 'Gerrit Cole', 'Masahiro Tanaka', 'James Paxton', 'Luis Severino', 'Domingo German', 'J.A. Happ', 'Other'}
yankees_pitchers={'Gerrit Cole', 'Masahiro Tanaka', 'James Paxton', 'Luis Severino', 'Domingo German', 'J.A. Happ', 'Other'}
indians_hitters={'Roberto Perez', 'Carlos Santana', 'Cesar Hernandez', 'Francisco Lindor', 'Jose Ramirez', 'Oscar Mercado', 'Franmil Reyes', 'Jake Bauers', 'Yu Chang', 'Mike Freeman', 'Sandy Leon', 'Greg Allen', 'Jordan Luplow', 'Carlos Carrasco', 'Mike Clevinger', 'Shane Bieber', 'Zach Plesac', 'Aaron Civale', 'Other'}
indians_pitchers={'Carlos Carrasco', 'Mike Clevinger', 'Shane Bieber', 'Zach Plesac', 'Aaron Civale', 'Other'}
royals_hitters={'Salvador Perez', "Ryan O'Hearn", 'Nicky Lopez', 'Adalberto Mondesi', 'Maikel Franco', 'Hunter Dozier', 'Humberto Arteaga', 'Matt Reynolds', 'Whit Merrifield', 'Jorge Soler', 'Bubba Starling', 'Brett Phillips', 'Alex Gordon', 'Brad Keller', 'Danny Duffy', 'Jakob Junis', 'Mike Montgomery', 'Glenn Sparkman', 'Other'}
royals_pitchers={'Brad Keller', 'Danny Duffy', 'Jakob Junis', 'Mike Montgomery', 'Glenn Sparkman', 'Other'}
tigers_hitters={'Austin Romine', 'Grayson Greiner', 'C.J. Cron', 'Jonathan Schoop', 'Niko Goodrum', 'Dawel Lugo' 'Jeimer Candelario', 'Harold Castro', 'Willi Castro', 'Jacoby Jones', 'Christin Stewart', 'Victor Reyes', 'Miguel Cabrera', 'Matthew Boyd', 'Jordan Zimmermann', 'Spencer Turnbull', 'Ivan Nova', 'Daniel Norris', 'Other'}
tigers_pitchers={'Matthew Boyd', 'Jordan Zimmermann', 'Spencer Turnbull', 'Ivan Nova', 'Daniel Norris', 'Other'}
twins_hitters={'Mitch Garver', 'Alex Avila', 'Willians Astudillo', 'Miguel Sano', 'Marwin Gonzalez', 'Luis Arraez', 'Ehire Adrianza', 'Jorge Polanco', 'Josh Donaldson', 'Nelson Cruz', 'Max Kepler', 'Byron Buxton', 'Eddie Rosario', 'Jose Berrios', 'Jake Odorizzi', 'Homer Bailey', 'Rich Hill', 'Michael Pineda', 'Randy Dobnak', 'Devin Smeltzer', 'Kenta Maeda', 'Other'}
twins_pitchers={'Jose Berrios', 'Jake Odorizzi', 'Homer Bailey', 'Rich Hill', 'Michael Pineda', 'Randy Dobnak', 'Devin Smeltzer', 'Kenta Maeda', 'Other'}
whitesox_hitters={'Yasmani Grandal', 'James McCann', 'Jose Abreu', 'Leury Garcia', 'Nick Madrigal', 'Tim Anderson', 'Yoan Moncada', 'Eloy Jimenez', 'Luis Robert', 'Nomar Mazara', 'Edwin Encarnacion', 'Zack Collins', 'Danny Mendick', 'Lucas Giolito', 'Dallas Keuchel', 'Gio Gonzalez', 'Dylan Cease', 'Reynaldo Lopez', 'Other'}
whitesox_pitchers={'Lucas Giolito', 'Dallas Keuchel', 'Gio Gonzalez', 'Dylan Cease', 'Reynaldo Lopez', 'Other'}
angels_hitters={'Max Stassi', 'Jason Castro', 'Albert Pujols', 'Tommy La Stella', 'David Fletcher', 'Andrelton Simmons', 'Anthony Rendon', 'Juston Upton', 'Mike Trout', 'Brian Goodwin', 'Jo Adell', 'Michael Hermosilllo', 'Shohei Ohtani', 'Andrew Heaney', 'Griffin Canning', 'Dylan Bundy', 'Julio Teheran', 'Other'} 
angels_pitchers={ 'Shohei Ohtani', 'Andrew Heaney', 'Griffin Canning', 'Dylan Bundy', 'Julio Teheran', 'Other'}
astros_hitters={'Martin Maldonado', 'Dustin Garneau', 'Yuli Gurriel', 'Jose Altuve', 'Carlos Correa', 'Alex Bregman', 'Aledmys Diaz', 'Michael Brantley', 'George Springer', 'Josh Reddick', 'Kyle Tucker', 'Yordan Alvarez', 'Garrett Stubbs', 'Justin Verlander', 'Zack Grienke', 'Lance McCullers Jr.', 'Jose Urquidy', 'Other'}
astros_pitchers={'Justin Verlander', 'Zack Grienke', 'Lance McCullers Jr.', 'Jose Urquidy', 'Other'}
athletics_hitters={'Sean Murphy', 'Matt Olson', 'Franklin Barreto', 'Jorge Mateo', 'Marcus Semien', 'Matt Chapman', 'Chad Pinder', 'Ramon Laureano', 'Mark Canha', 'Stephen Piscotty', 'Robbie Grossman', 'Khris Davis', 'Vimeal Mchin', 'Sean Manaea', 'Frankie Montas', 'Jesus Luzardo', 'Mike Fiers', 'Chris Bassitt', 'Other'}
athletics_pitchers={'Sean Manaea', 'Frankie Montas', 'Jesus Luzardo', 'Mike Fiers', 'Chris Bassitt', 'Other'}
mariners_hitters={'Tom Murphy', 'Austin Nola', 'Evan White', 'Shed Long', 'Dee Gordon', 'J.P. Crawford', 'Kyle Seager', 'Daniel Vogelbach', 'Dylan Moore', 'Mitch Haniger', 'Mallex Smith', 'Kyle Lewis', 'Jake Fraley', 'Marco Gonzales', 'Yusei Kikuchi', 'Kendall Graveman', 'Justus Sheffield', 'Justin Dunn', 'Other'}
mariners_pitchers={'Marco Gonzales', 'Yusei Kikuchi', 'Kendall Graveman', 'Justus Sheffield', 'Justin Dunn', 'Other'}
rangers_hitters={'Robinson Chirinos', 'Jeff Mathis', 'Ronald guzman', 'Rougned Odor', 'Elvis Andrus', 'Todd frazier', 'Willie Calhoun', 'Danny Santana', 'Joey Gallo', 'Scott Heineman', 'Shin-Soo Choo', 'Isiah Kiner-Falefa', 'Sam Travis', 'Mike Minor', 'Lance Lynn', 'Corey Kluber', 'Kyle Gibson', 'Jordan Lyles', 'Other'}
rangers_pitchers={'Mike Minor', 'Lance Lynn', 'Corey Kluber', 'Kyle Gibson', 'Jordan Lyles', 'Other'}
braves_hitters={"Travis d'Arnaud", 'Tyler Flowers', 'Freddie Freeman', 'Ozzie Albies', 'Dansby Swanson', 'Johan Camargo', 'Charlie Culberson', 'Adeiny Hechavarria', 'Ronald Acuna Jr.', 'Ender Inciarte', 'Marcell Ozuna', 'Nick Markakis', 'Adam Duvall', 'Mike Soroka', 'Mike Foltynewicz', 'Max Fried', 'Cole Hamels', 'Other'}
braves_pitchers={'Mike Soroka', 'Mike Foltynewicz', 'Max Fried', 'Cole Hamels', 'Other'}
marlins_hitters={'Jorge Alfaro', 'Francisco Cervelli', 'Jesus Aguilar', 'Garrett Cooper', 'Isan Diaz', 'Miguel Rojas', 'Jonathan Villar', 'Corey Dickerson', 'Brian Anderson', 'Harold Ramirez', 'Lewis Brinson', 'Magneuris Sierra', 'Jon Berti', 'Sandy Alcantara', 'Caleb Smith', 'Pablo Lopez', 'Jordan Yamamoto', 'Elieser Hernandez', 'Other'}
marlins_pitchers={'Sandy Alcantara', 'Caleb Smith', 'Pablo Lopez', 'Jordan Yamamoto', 'Elieser Hernandez', 'Other'}
mets_hitters={'Wilson Ramos', 'Pete Alonso', 'Dominic Smith', 'Robinson Cano', 'Amed Rasario', 'Jeff McNeil', 'Michael Conforto', 'Brandon Nimmo', 'J.D. Davis', 'Jake Marisnick', 'Yoenis Cespedes', 'Jed Lowrie', 'Jacob deGrom', 'Noah Syndergaard', 'Marcus Stroman' 'Michael Wacha', 'Rick Porcello', 'Steven Matz', 'Other'}
mets_pitchers={'Jacob deGrom', 'Noah Syndergaard', 'Marcus Stroman' 'Michael Wacha', 'Rick Porcello', 'Steven Matz', 'Other'}
nationals_hitters={'Kurt Suzuki', 'Yan Gomes', 'Eric Thames', 'Howie Kendrick', 'Ryan Zimmerman', 'Starlin Castro', 'Trea Turner', 'Asdrubal Cabrera', 'Juan Soto', 'Victor robles', 'Adam Eaton', 'Michael Taylor', 'Carter Kieboom', 'Max Scherzer', 'Stephen Strasburg', 'Patrick Corbin', 'Anibal Sanchez' , 'Other'}
nationals_pitchers={'Max Scherzer', 'Stephen Strasburg', 'Patrick Corbin', 'Anibal Sanchez' , 'Other'}
phillies_hitters={'J.T. Realmuto', 'Andrew Knapp', 'Rhys Hoskins', 'Jean Segura', 'Didi Gregorious', 'Scott Kingery', 'Josh Harrison', 'Phil Gosselin', 'Andrew McCutchen', 'Adam Haseley', 'Bryce Harper', 'Jay Bruce', 'Roman Quinn', 'Aaron Nola', 'Zack Wheeler', 'Jake Arrieta', 'Zach Eflin', 'Vince Velasquez', 'Other'}
phillies_pitchers={ 'Aaron Nola', 'Zack Wheeler', 'Jake Arrieta', 'Zach Eflin', 'Vince Velasquez', 'Other'}
brewers_hitters={'Omar Narvaez', 'Manny Pina', 'Justin Smoak', 'Ryan Braun', 'Keston Hiura', 'Orlando Arcia', 'Eric Sogard', 'Jedd Gyorko', 'Avisail Garcia', 'Lorenzo Cain', 'Christian Yelich', 'Ben Gamel', 'Luis Urias', 'Brandon Woodruff', 'Adrian Houser', 'Brett Anderson', 'Josh Lindblom', 'Eric Lauer', 'Other'}
brewers_pitchers={'Brandon Woodruff', 'Adrian Houser', 'Brett Anderson', 'Josh Lindblom', 'Eric Lauer', 'Other'}
cardinals_hitters={'Yadier Molina', 'Paul Goldschmidt', 'Kolten Wong', 'Paul DeJong', 'Matt Carpenter', 'Tommy Edman', 'Dexter Fowler', 'Harrison Bader', 'Lane Thomas', 'Dylan Carlson', "Tyler O'Neill", 'Andrew Knizner', 'Justin Williams', 'Jack Flaherty', 'Dakota Hudson', 'Miles Mikolas', 'Adam Wainwright', 'Other'}
cardinals_pitchers={'Jack Flaherty', 'Dakota Hudson', 'Miles Mikolas', 'Adam Wainwright', 'Other'}
cubs_hitters={'Victor Caratini', 'Willson Conteras', 'Anthony Rizzo', 'David Bote', 'Nico Hoerner', 'Javier Baez', 'Kris Bryant', 'Jason Heyward', 'Kyle Schwarber', 'Daniel Descalso', 'Albert Almora Jr.', 'Ian Happ', 'Robel Garcia', 'Yu Darvish', 'Kyle Hendricks', 'Jon Lester', 'Jose Quintana', 'Other'}
cubs_pitchers={'Yu Darvish', 'Kyle Hendricks', 'Jon Lester', 'Jose Quintana', 'Other'}
pirates_hitters={'Jacob Stallings', 'Luke Maile', 'Josh Bell', 'Adam Frazier', 'Kevin Newman', 'Cole Tucker', 'Colin Moran', 'Erik Gonzalez', 'Bryan reynolds', 'Gregory Polanco', 'Guillermo Heredia', 'Jason Martin', 'Jose Osuna', 'Joe Musgrove', 'Trevor Williams', 'Chris Archer', 'Mitch Keller', 'Steven Brault', 'Other'}
pirates_pitchers={'Trevor Williams', 'Chris Archer', 'Mitch Keller', 'Steven Brault', 'Other'}
reds_hitters={'Tucker Barnhart', 'Curt Casali', 'Joey Votto', 'Mike Moustakas', 'Freddy Galvis', 'Eugenio Suarez', 'Kyle Farmer', 'Nick Castellanos', 'Shogo Akiyama', 'Alex Blandino', 'Aristides Aquino', 'Nick Senzel', 'Jesse Winker', 'Michael Lorenzen', 'Luis Castillo', 'Sonny Gray', 'Trevor Bauer', 'Anthony DeSclafani', 'Wade Miley', 'Other'}
reds_pitchers={'Luis Castillo', 'Sonny Gray', 'Trevor Bauer', 'Anthony DeSclafani', 'Wade Miley', 'Other'}
diamondbacks_hitters={'Carson Kelly', 'Stephen Vogt', 'Christian Walker', 'Jake Lamb', 'Ketel Marte', 'Eduardo Escobar', 'Nick Ahmed', 'David Peralta', 'Kole Calhoun', 'Josh Rojas', 'Andy Young', 'Kevin Cron', 'Ildemaro Vargas', 'Madison Bumgarner', 'Robbie Ray', 'Mike Leake', 'Luke Weaver', 'Zac Gallen', 'Other'}
diamondbacks_pitchers={'Madison Bumgarner', 'Robbie Ray', 'Mike Leake', 'Luke Weaver', 'Zac Gallen', 'Other'}
dodgers_hitters={'Mookie Betts', 'Will Smith', 'Enrique Hernandez', 'Max Muncy', 'Gavin Lux', 'Corey Seager', 'Justin Turner', 'Austin Barnes', 'Cody Bellinger', 'Joc Pederson', 'A.J. Pollock', 'Chris Taylor', 'Kyle Garlick', 'Walker Buehler', 'Clayton Kershaw', 'Alex Wood', 'Jimmy Nelson', 'Julio Urias', 'Ross Stripling', 'Other'}
dodgers_pitchers={'Walker Buehler', 'Clayton Kershaw', 'Alex Wood', 'Jimmy Nelson', 'Julio Urias', 'Ross Stripling', 'David Price', 'Other'}
giants_hitters={'Buster Posey', 'Aramis Garcia', 'Brandon Belt', 'Mauricio Dubon', 'Brandon Crawford', 'Evan Longoria', 'Mike Yastremski', 'Alex Dickerson', 'Steven Duggar', 'Jaylin Davis', 'Chris Shaw', 'Kean Wong', 'Donovan Solano', 'Johnny Cueto', 'Jeff Samardzija', 'Kevin Gausman', 'Drew Smyly', 'Other'}
giants_pitchers={'Johnny Cueto', 'Jeff Samardzija', 'Kevin Gausman', 'Drew Smyly', 'Other'}
padres_hitters={'Francisco Mejia', 'Austin Hedges', 'Eric Hosmer', 'Jurickson Profar', 'Fernando Tatis Jr.', 'Manny Machado', 'Tommy Pham', 'Wil Myers', 'Trent Grisham', 'Manuel Margot', 'Josh Naylor', 'Jake Cronenworth', 'Ty France', 'Chris Paddack', 'Garrett Richards', 'Zach Davies', 'Dinelson Lamet', 'Joey Lucchesi', 'Other'}
padres_pitchers={'Chris Paddack', 'Garrett Richards', 'Zach Davies', 'Dinelson Lamet', 'Joey Lucchesi', 'Other'}
rockies_hitters={'Tony Wolters', 'Daniel Murphy', 'Ryan McMahon', 'Garret Hampson', 'Trevor Story', 'Nolan Arenado', 'Brendan Rodgers', 'Chris Owings', 'Raimel Tapia', 'David Dahl', 'Charlie Blackmon', 'Ian Desmond', 'Sam Hilliard', 'German Marquez', 'Jon Gray', 'Kyle Freeland', 'Antonio Senzatela', 'Other'}
rockies_pitchers={'German Marquez', 'Jon Gray', 'Kyle Freeland', 'Antonio Senzatela', 'Other'}
popupMenu = OptionMenu(mainframe, tkvar1, *MLBteams1)
Label(mainframe, text="Road Team:").grid(row = 0, column = 0)
popupMenu.grid(row = 0, column =1)
Label(mainframe, text="Home Team:").grid(row=0, column=2)
popupMenu2=OptionMenu(mainframe,tkvar2,*MLBteams2)
popupMenu2.grid(row=0, column=3)
Label(mainframe,text="Lineups:").grid(row=1, column=0)
Label(mainframe,text="Primary Pitcherz").grid(row=10, column=0)


if tkvar1.get()=='Arizona Diamondbacks':
    hitters_list1=diamondbacks_hitters
    pitchers_list1=diamondbacks_pitchers
elif tkvar1.get()=='Atlanta Braves':
    hitters_list1=braves_hitters
    pitchers_list1=braves_pitchers
elif tkvar1.get()=='Baltimore Orioles':
    hitters_list1=orioles_hitters
    pitchers_list1=orioles_pitchers
elif tkvar1.get()=='Boston Red Sox':
    hitters_list1=redsox_hitters
    pitchers_list1=redsox_pitchers
elif tkvar1.get()=='Chicago Cubs':
    hitters_list1=cubs_hitters
    pitchers_list1=cubs_pitchers
elif tkvar1.get()=='Chicago White Sox':
    hitters_list1=whitesox_hitters
    pitchers_list1=whitesox_pitchers
elif tkvar1.get()=='Cincinnati Reds':
    hitters_list1=reds_hitters
    pitchers_list1=reds_pitchers
elif tkvar1.get()=='Cleveland Indians':
    hitters_list1=indians_hitters
    pitchers_list1=indians_pitchers
elif tkvar1.get()=='Colorado Rockies':
    hitters_list1=rockies_hitters
    pitchers_list1=rockies_pitchers
elif tkvar1.get()=='Detroit Tigers':
    hitters_list1=tigers_hitters
    pitchers_list1=tigers_pitchers
elif tkvar1.get()=='Houston Astros':
    hitters_list1=astros_hitters
    pitchers_list1=astros_pitchers
elif tkvar1.get()=='Kansas City Royals':
    hitters_list1=royals_hitters
    pitchers_list1=royals_pitchers
elif tkvar1.get()=='Los Angeles Angels':
    hitters_list1=angels_hitters
    pitchers_list1=angels_pitchers
elif tkvar1.get()=='Los Angeles Dodgers':
    hitters_list1=dodgers_hitters
    pitchers_list1=dodgers_pitchers
elif tkvar1.get()=='Miami Marlins':
    hitters_list1=marlins_hitters
    pitchers_list1=marlins_pitchers
elif tkvar1.get()=='Milwaukee Brewers':
    hitters_list1=brewers_hitters
    pitchers_list1=brewers_pitchers
elif tkvar1.get()=='Minnesota Twins':
    hitters_list1=twins_hitters
    pitchers_list1=twins_pitchers
elif tkvar1.get()=='New York Mets':
    hitters_list1=mets_hitters
    pitchers_list1=mets_pitchers
elif tkvar1.get()=='New York Yankees':
    hitters_list1=yankees_hitters
    pitchers_list1=yankees_pitchers
elif tkvar1.get()=='Oakland Athletics':
    hitters_list1=athletics_hitters
    pitchers_list1=athletics_pitchers
elif tkvar1.get()=='Philadelphia Phillies':
    hitters_list1=phillies_hitters
    pitchers_list1=phillies_pitchers
elif tkvar1.get()=='Pittsburgh Pirates':
    hitters_list1=pirates_hitters
    pitchers_list1=pirates_pitchers
elif tkvar1.get()=='San Diego Padres':
    hitters_list1=padres_hitters
    pitchers_list1=padres_pitchers
elif tkvar1.get()=='San Francisco Giants':
    hitters_list1=giants_hitters
    pitchers_list1=giants_pitchers
elif tkvar1.get()=='Seattle Mariners':
    hitters_list1=mariners_hitters
    pitchers_list1=mariners_pitchers
elif tkvar1.get()=='St. Louis Cardinals':
    hitters_list1=cardinals_hitters
    pitchers_list1=cardinals_pitchers
elif tkvar1.get()=='Tampa Bay Rays':
    hitters_list1=rays_hitters
    pitchers_list1=rays_pitchers
elif tkvar1.get()=='Texas Rangers':
    hitters_list1=rangers_hitters
    pitchers_list1=rangers_pitchers
elif tkvar1.get()=='Toronto Blue Jays':
    hitters_list1=bluejays_hitters
    pitchers_list1=bluejays_pitchers
elif tkvar1.get()=='Washington Nationals':
    hitters_list1=nationals_hitters
    pitchers_list1=nationals_pitchers

if tkvar2.get()=='Arizona Diamondbacks':
    hitters_list2=diamondbacks_hitters
    pitchers_list2=diamondbacks_pitchers
elif tkvar2.get()=='Atlanta Braves':
    hitters_list2=braves_hitters
    pitchers_list2=braves_pitchers
elif tkvar2.get()=='Baltimore Orioles':
    hitters_list2=orioles_hitters
    pitchers_list2=orioles_pitchers
elif tkvar2.get()=='Boston Red Sox':
    hitters_list2=redsox_hitters
    pitchers_list2=redsox_pitchers
elif tkvar2.get()=='Chicago Cubs':
    hitters_list2=cubs_hitters
    pitchers_list2=cubs_pitchers
elif tkvar2.get()=='Chicago White Sox':
    hitters_list2=whitesox_hitters
    pitchers_list2=whitesox_pitchers
elif tkvar2.get()=='Cincinnati Reds':
    hitters_list2=reds_hitters
    pitchers_list2=reds_pitchers
elif tkvar2.get()=='Cleveland Indians':
    hitters_list2=indians_hitters
    pitchers_list2=indians_pitchers
elif tkvar2.get()=='Colorado Rockies':
    hitters_list2=rockies_hitters
    pitchers_list2=rockies_pitchers
elif tkvar2.get()=='Detroit Tigers':
    hitters_list2=tigers_hitters
    pitchers_list2=tigers_pitchers
elif tkvar2.get()=='Houston Astros':
    hitters_list2=astros_hitters
    pitchers_list2=astros_pitchers
elif tkvar2.get()=='Kansas City Royals':
    hitters_list2=royals_hitters
    pitchers_list2=royals_pitchers
elif tkvar2.get()=='Los Angeles Angels':
    hitters_list2=angels_hitters
    pitchers_list2=angels_pitchers
elif tkvar2.get()=='Los Angeles Dodgers':
    hitters_list2=dodgers_hitters
    pitchers_list2=dodgers_pitchers
elif tkvar2.get()=='Miami Marlins':
    hitters_list2=marlins_hitters
    pitchers_list2=marlins_pitchers
elif tkvar2.get()=='Milwaukee Brewers':
    hitters_list2=brewers_hitters
    pitchers_list2=brewers_pitchers
elif tkvar2.get()=='Minnesota Twins':
    hitters_list2=twins_hitters
    pitchers_list2=twins_pitchers
elif tkvar2.get()=='New York Mets':
    hitters_list2=mets_hitters
    pitchers_list2=mets_pitchers
elif tkvar2.get()=='New York Yankees':
    hitters_list2=yankees_hitters
    pitchers_list2=yankees_pitchers
elif tkvar2.get()=='Oakland Athletics':
    hitters_list2=athletics_hitters
    pitchers_list2=athletics_pitchers
elif tkvar2.get()=='Philadelphia Phillies':
    hitters_list2=phillies_hitters
    pitchers_list2=phillies_pitchers
elif tkvar2.get()=='Pittsburgh Pirates':
    hitters_list2=pirates_hitters
    pitchers_list2=pirates_pitchers
elif tkvar2.get()=='San Diego Padres':
    hitters_list2=padres_hitters
    pitchers_list2=padres_hitters
elif tkvar2.get()=='San Francisco Giants':
    hitters_list2=giants_hitters
    pitchers_list2=giants_pitchers
elif tkvar2.get()=='Seattle Mariners':
    hitters_list2=mariners_hitters
    pitchers_list2=mariners_pitchers
elif tkvar2.get()=='St. Louis Cardinals':
    hitters_list2=cardinals_hitters
    pitchers_list2=cardinals_pitchers
elif tkvar2.get()=='Tampa Bay Rays':
    hitters_list2=rays_hitters
    pitchers_list2=rays_pitchers
elif tkvar2.get()=='Texas Rangers':
    hitters_list2=rangers_hitters
    pitchers_list2=rangers_pitchers
elif tkvar2.get()=='Toronto Blue Jays':
    hitters_list2=bluejays_hitters
    pitchers_list2=bluejays_pitchers
elif tkvar2.get()=='Washington Nationals':
    hitters_list2=nationals_hitters
    pitchers_list2=nationals_pitchers



batter1roadteam=OptionMenu(mainframe,tkvar3,*hitters_list1)
batter1roadteam.grid(row=1, column=1)
batter2roadteam=OptionMenu(mainframe,tkvar4,*hitters_list1)
batter2roadteam.grid(row=2, column=1)
batter3roadteam=OptionMenu(mainframe,tkvar5,*hitters_list1)
batter3roadteam.grid(row=3, column=1)
batter4roadteam=OptionMenu(mainframe,tkvar6,*hitters_list1)
batter4roadteam.grid(row=4, column=1)
batter5roadteam=OptionMenu(mainframe,tkvar7,*hitters_list1)
batter5roadteam.grid(row=5, column=1)
batter6roadteam=OptionMenu(mainframe,tkvar8,*hitters_list1)
batter6roadteam.grid(row=6, column=1)
batter7roadteam=OptionMenu(mainframe,tkvar9,*hitters_list1)
batter7roadteam.grid(row=7, column=1)
batter8roadteam=OptionMenu(mainframe,tkvar10,*hitters_list1)
batter8roadteam.grid(row=8, column=1)
batter9roadteam=OptionMenu(mainframe,tkvar11,*hitters_list1)
batter9roadteam.grid(row=9, column=1)
primarypitcherroadteam=OptionMenu(mainframe,tkvar12,*pitchers_list1)
primarypitcherroadteam.grid(row=10, column=1)
batter1hometeam=OptionMenu(mainframe,tkvar13,*hitters_list2)
batter1hometeam.grid(row=1, column=3)
batter2hometeam=OptionMenu(mainframe,tkvar14,*hitters_list2)
batter2hometeam.grid(row=2, column=3)
batter3hometeam=OptionMenu(mainframe,tkvar15,*hitters_list2)
batter3hometeam.grid(row=3, column=3)
batter4hometeam=OptionMenu(mainframe,tkvar16,*hitters_list2)
batter4hometeam.grid(row=4, column=3)
batter5hometeam=OptionMenu(mainframe,tkvar17,*hitters_list2)
batter5hometeam.grid(row=5, column=3)
batter6hometeam=OptionMenu(mainframe,tkvar18,*hitters_list2)
batter6hometeam.grid(row=6, column=3)
batter7hometeam=OptionMenu(mainframe,tkvar19,*hitters_list2)
batter7hometeam.grid(row=7, column=3)
batter8hometeam=OptionMenu(mainframe,tkvar20,*hitters_list2)
batter8hometeam.grid(row=8, column=3)
batter9hometeam=OptionMenu(mainframe,tkvar21,*hitters_list2)
batter9hometeam.grid(row=9, column=3)
primarypitcherhometeam=OptionMenu(mainframe,tkvar22,*pitchers_list2)
primarypitcherhometeam.grid(row=10, column=3)
b=Button(mainframe,text="Check Teams Selected", command=get_players)
c=Button(mainframe,text="Calculate Percentage", command=calculate_percentage)
b.grid(row=11, column=1)
c.grid(row=11, column=3)

while picking:
    if tkvar1.get()=='Arizona Diamondbacks':
        hitters_list1=diamondbacks_hitters
        pitchers_list1=diamondbacks_pitchers
    elif tkvar1.get()=='Atlanta Braves':
        hitters_list1=braves_hitters
        pitchers_list1=braves_pitchers
    elif tkvar1.get()=='Baltimore Orioles':
        hitters_list1=orioles_hitters
        pitchers_list1=orioles_pitchers
    elif tkvar1.get()=='Boston Red Sox':
        hitters_list1=redsox_hitters
        pitchers_list1=redsox_pitchers
    elif tkvar1.get()=='Chicago Cubs':
        hitters_list1=cubs_hitters
        pitchers_list1=cubs_pitchers
    elif tkvar1.get()=='Chicago White Sox':
        hitters_list1=whitesox_hitters
        pitchers_list1=whitesox_pitchers
    elif tkvar1.get()=='Cincinnati Reds':
        hitters_list1=reds_hitters
        pitchers_list1=reds_pitchers
    elif tkvar1.get()=='Cleveland Indians':
        hitters_list1=indians_hitters
        pitchers_list1=indians_pitchers
    elif tkvar1.get()=='Colorado Rockies':
        hitters_list1=rockies_hitters
        pitchers_list1=rockies_pitchers
    elif tkvar1.get()=='Detroit Tigers':
        hitters_list1=tigers_hitters
        pitchers_list1=tigers_pitchers
    elif tkvar1.get()=='Houston Astros':
        hitters_list1=astros_hitters
        pitchers_list1=astros_pitchers
    elif tkvar1.get()=='Kansas City Royals':
        hitters_list1=royals_hitters
        pitchers_list1=royals_pitchers
    elif tkvar1.get()=='Los Angeles Angels':
        hitters_list1=angels_hitters
        pitchers_list1=angels_pitchers
    elif tkvar1.get()=='Los Angeles Dodgers':
        hitters_list1=dodgers_hitters
        pitchers_list1=dodgers_pitchers
    elif tkvar1.get()=='Miami Marlins':
        hitters_list1=marlins_hitters
        pitchers_list1=marlins_pitchers
    elif tkvar1.get()=='Milwaukee Brewers':
        hitters_list1=brewers_hitters
        pitchers_list1=brewers_pitchers
    elif tkvar1.get()=='Minnesota Twins':
        hitters_list1=twins_hitters
        pitchers_list1=twins_pitchers
    elif tkvar1.get()=='New York Mets':
        hitters_list1=mets_hitters
        pitchers_list1=mets_pitchers
    elif tkvar1.get()=='New York Yankees':
        hitters_list1=yankees_hitters
        pitchers_list1=yankees_pitchers
    elif tkvar1.get()=='Oakland Athletics':
        hitters_list1=athletics_hitters
        pitchers_list1=athletics_pitchers
    elif tkvar1.get()=='Philadelphia Phillies':
        hitters_list1=phillies_hitters
        pitchers_list1=phillies_pitchers
    elif tkvar1.get()=='Pittsburgh Pirates':
        hitters_list1=pirates_hitters
        pitchers_list1=pirates_pitchers
    elif tkvar1.get()=='San Diego Padres':
        hitters_list1=padres_hitters
        pitchers_list1=padres_pitchers
    elif tkvar1.get()=='San Francisco Giants':
        hitters_list1=giants_hitters
        pitchers_list1=giants_pitchers
    elif tkvar1.get()=='Seattle Mariners':
        hitters_list1=mariners_hitters
        pitchers_list1=mariners_pitchers
    elif tkvar1.get()=='St. Louis Cardinals':
        hitters_list1=cardinals_hitters
        pitchers_list1=cardinals_pitchers
    elif tkvar1.get()=='Tampa Bay Rays':
        hitters_list1=rays_hitters
        pitchers_list1=rays_pitchers
    elif tkvar1.get()=='Texas Rangers':
        hitters_list1=rangers_hitters
        pitchers_list1=rangers_pitchers
    elif tkvar1.get()=='Toronto Blue Jays':
        hitters_list1=bluejays_hitters
        pitchers_list1=bluejays_pitchers
    elif tkvar1.get()=='Washington Nationals':
        hitters_list1=nationals_hitters
        pitchers_list1=nationals_pitchers

    if tkvar2.get()=='Arizona Diamondbacks':
        hitters_list2=diamondbacks_hitters
        pitchers_list2=diamondbacks_pitchers
    elif tkvar2.get()=='Atlanta Braves':
        hitters_list2=braves_hitters
        pitchers_list2=braves_pitchers
    elif tkvar2.get()=='Baltimore Orioles':
        hitters_list2=orioles_hitters
        pitchers_list2=orioles_pitchers
    elif tkvar2.get()=='Boston Red Sox':
        hitters_list2=redsox_hitters
        pitchers_list2=redsox_pitchers
    elif tkvar2.get()=='Chicago Cubs':
        hitters_list2=cubs_hitters
        pitchers_list2=cubs_pitchers
    elif tkvar2.get()=='Chicago White Sox':
        hitters_list2=whitesox_hitters
        pitchers_list2=whitesox_pitchers
    elif tkvar2.get()=='Cincinnati Reds':
        hitters_list2=reds_hitters
        pitchers_list2=reds_pitchers
    elif tkvar2.get()=='Cleveland Indians':
        hitters_list2=indians_hitters
        pitchers_list2=indians_pitchers
    elif tkvar2.get()=='Colorado Rockies':
        hitters_list2=rockies_hitters
        pitchers_list2=rockies_pitchers
    elif tkvar2.get()=='Detroit Tigers':
        hitters_list2=tigers_hitters
        pitchers_list2=tigers_pitchers
    elif tkvar2.get()=='Houston Astros':
        hitters_list2=astros_hitters
        pitchers_list2=astros_pitchers
    elif tkvar2.get()=='Kansas City Royals':
        hitters_list2=royals_hitters
        pitchers_list2=royals_pitchers
    elif tkvar2.get()=='Los Angeles Angels':
        hitters_list2=angels_hitters
        pitchers_list2=angels_pitchers
    elif tkvar2.get()=='Los Angeles Dodgers':
        hitters_list2=dodgers_hitters
        pitchers_list2=dodgers_pitchers
    elif tkvar2.get()=='Miami Marlins':
        hitters_list2=marlins_hitters
        pitchers_list2=marlins_pitchers
    elif tkvar2.get()=='Milwaukee Brewers':
        hitters_list2=brewers_hitters
        pitchers_list2=brewers_pitchers
    elif tkvar2.get()=='Minnesota Twins':
        hitters_list2=twins_hitters
        pitchers_list2=twins_pitchers
    elif tkvar2.get()=='New York Mets':
        hitters_list2=mets_hitters
        pitchers_list2=mets_pitchers
    elif tkvar2.get()=='New York Yankees':
        hitters_list2=yankees_hitters
        pitchers_list2=yankees_pitchers
    elif tkvar2.get()=='Oakland Athletics':
        hitters_list2=athletics_hitters
        pitchers_list2=athletics_pitchers
    elif tkvar2.get()=='Philadelphia Phillies':
        hitters_list2=phillies_hitters
        pitchers_list2=phillies_pitchers
    elif tkvar2.get()=='Pittsburgh Pirates':
        hitters_list2=pirates_hitters
        pitchers_list2=pirates_pitchers
    elif tkvar2.get()=='San Diego Padres':
        hitters_list2=padres_hitters
        pitchers_list2=padres_hitters
    elif tkvar2.get()=='San Francisco Giants':
        hitters_list2=giants_hitters
        pitchers_list2=giants_pitchers
    elif tkvar2.get()=='Seattle Mariners':
        hitters_list2=mariners_hitters
        pitchers_list2=mariners_pitchers
    elif tkvar2.get()=='St. Louis Cardinals':
        hitters_list2=cardinals_hitters
        pitchers_list2=cardinals_pitchers
    elif tkvar2.get()=='Tampa Bay Rays':
        hitters_list2=rays_hitters
        pitchers_list2=rays_pitchers
    elif tkvar2.get()=='Texas Rangers':
        hitters_list2=rangers_hitters
        pitchers_list2=rangers_pitchers
    elif tkvar2.get()=='Toronto Blue Jays':
        hitters_list2=bluejays_hitters
        pitchers_list2=bluejays_pitchers
    elif tkvar2.get()=='Washington Nationals':
        hitters_list2=nationals_hitters
        pitchers_list2=nationals_pitchers
 

# on change dropdown value
mainframe.update()

def change():

# link function to change dropdown
    tkvar1.trace('w', change_dropdown)
    tkvar2.trace('w', change_dropdown)
    tkvar3.trace('w', change_dropdown)
    tkvar4.trace('w', change_dropdown)
    tkvar5.trace('w', change_dropdown)
    tkvar6.trace('w', change_dropdown)
    tkvar7.trace('w', change_dropdown)
    tkvar8.trace('w', change_dropdown)
    tkvar9.trace('w', change_dropdown)
    tkvar10.trace('w', change_dropdown)
    tkvar11.trace('w', change_dropdown)
    tkvar12.trace('w', change_dropdown)
    tkvar13.trace('w', change_dropdown)
    tkvar14.trace('w', change_dropdown)
    tkvar15.trace('w', change_dropdown)
    tkvar16.trace('w', change_dropdown)
    tkvar17.trace('w', change_dropdown)
    tkvar18.trace('w', change_dropdown)
    tkvar19.trace('w', change_dropdown)
    tkvar20.trace('w', change_dropdown)
    tkvar21.trace('w', change_dropdown)
    tkvar22.trace('w', change_dropdown)

root.mainloop()
