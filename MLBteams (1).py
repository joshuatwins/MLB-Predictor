from tkinter import *

root = Tk()
root.title("MLB Prediction program")

teams=['Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox', 'Chicago Cubs', 'Chicago White Sox', 'Cincinnati Reds', 'Cleveland Indians', 'Colorado Rockies', 'Detroit Tigers', 'Houston Astros', 'Kansas City Royals',
       'Los Angeles Angels', 'Los Angeles Dodgers', 'Miami Marlins', 'Milwaukee Brewers', 'Minnesota Twins', 'New York Mets', 'New York Yankees', 'Oakland Athletics', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 'San Francisco Giants',
       'Seattle Mariners', 'St. Louis Cardinals', 'Tampa Bay Rays', 'Texas Rangers', 'Toronto Blue Jays', 'Washington Nationals']

def get_players():
    pass

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

def set_up_road(null="arg"):
    hitters_list1=hitters[tkvar1.get()]
    pitchers_list1=pitchers[tkvar1.get()]
    try:
        batter1roadteam.destroy()
        batter2roadteam.destroy()
        batter3roadteam.destroy()
        batter4roadteam.destroy()
        batter5roadteam.destroy()
        batter6roadteam.destroy()
        batter7roadteam.destroy()
        batter8roadteam.destroy()
        batter9roadteam.destroy()
        primarypitcherroadteam.destory()
    except:
        pass
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
def set_up_home(null="arg"):
    hitters_list2=hitters[tkvar2.get()]
    pitchers_list2=pitchers[tkvar2.get()]
    try:
        batter1hometeam.destory()
        batter2hometeam.destory()
        batter3hometeam.destory()
        batter4hometeam.destory()
        batter5hometeam.destory()
        batter6hometeam.destory()
        batter7hometeam.destory()
        batter8hometeam.destory()
        batter9hometeam.destory()
        primarypitcherhometeam.destroy()
    except:
        pass
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

# Dictionary with options
MLBteams1 = {'Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox', 'Chicago Cubs', 'Chicago White Sox', 'Cincinnati Reds', 'Cleveland Indians', 'Colorado Rockies', 'Detroit Tigers', 'Houston Astros', 'Kansas City Royals', 'Los Angeles Angels', 'Los Angeles Dodgers', 'Miami Marlins', 'Milwaukee Brewers', 'Minnesota Twins', 'New York Mets', 'New York Yankees', 'Oakland Athletics', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 'San Francisco Giants', 'Seattle Mariners', 'St. Louis Cardinals', 'Tampa Bay Rays', 'Texas Rangers', 'Toronto Blue Jays', 'Washington Nationals'}
MLBteams2={'Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox', 'Chicago Cubs', 'Chicago White Sox', 'Cincinnati Reds', 'Cleveland Indians', 'Colorado Rockies', 'Detroit Tigers', 'Houston Astros', 'Kansas City Royals', 'Los Angeles Angels', 'Los Angeles Dodgers', 'Miami Marlins', 'Milwaukee Brewers', 'Minnesota Twins', 'New York Mets', 'New York Yankees', 'Oakland Athletics', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 'San Francisco Giants', 'Seattle Mariners', 'St. Louis Cardinals', 'Tampa Bay Rays', 'Texas Rangers', 'Toronto Blue Jays', 'Washington Nationals'}
tkvar1.set('Arizona Diamondbacks') # set the default option
tkvar2.set('Arizona Diamondbacks')
hitters={'Arizona Diamondbacks':{'Carson Kelly', 'Stephen Vogt', 'Christian Walker', 'Jake Lamb', 'Ketel Marte', 'Eduardo Escobar', 'Nick Ahmed', 'David Peralta', 'Kole Calhoun', 'Josh Rojas', 'Andy Young', 'Kevin Cron', 'Ildemaro Vargas', 'Madison Bumgarner', 'Robbie Ray', 'Mike Leake', 'Luke Weaver', 'Zac Gallen', 'Other'},
         'Atlanta Braves':{"Travis d'Arnaud", 'Tyler Flowers', 'Freddie Freeman', 'Ozzie Albies', 'Dansby Swanson', 'Johan Camargo', 'Charlie Culberson', 'Adeiny Hechavarria', 'Ronald Acuna Jr.', 'Ender Inciarte', 'Marcell Ozuna', 'Nick Markakis', 'Adam Duvall', 'Mike Soroka', 'Mike Foltynewicz', 'Max Fried', 'Cole Hamels', 'Other'},
         'Baltimore Orioles':{'Pedro Severino', 'Chance Sisco', 'Chris Davis', 'Hanser Alberto', 'Jose Iglesias', 'Rio Ruiz', 'Renato Nunez', 'Stevie Wilkerson', 'Richard Urena', 'Trey Mancini', 'Austin Hays', 'Anthony Santander', 'Dwight Smith Jr.', 'John Means', 'Alex Cobb', 'Kohl Stewart', 'Asher Wojciechowski', 'Keegan Akin', 'Other'},
         'Boston Red Sox':{'Christian Vazquez', 'Kevin Plawecki', 'Michael Chavis', 'Jose Peraza', 'Xander Bogaerts', 'Rafael Devers', 'Andrew Benintendi', 'Jackie Bradley Jr.', 'J.D. Martinez', 'Bobby Dalbec', 'Marco Hernandez', 'Jonathan Arauz', 'Chris Sale', 'Eduardo Rodriguez', 'Nathan Eovaldi', 'Martin Perez', 'Other'},
         'Chicago Cubs':{'Victor Caratini', 'Willson Conteras', 'Anthony Rizzo', 'David Bote', 'Nico Hoerner', 'Javier Baez', 'Kris Bryant', 'Jason Heyward', 'Kyle Schwarber', 'Daniel Descalso', 'Albert Almora Jr.', 'Ian Happ', 'Robel Garcia', 'Yu Darvish', 'Kyle Hendricks', 'Jon Lester', 'Jose Quintana', 'Other'},
         'Chicago White Sox':{'Yasmani Grandal', 'James McCann', 'Jose Abreu', 'Leury Garcia', 'Nick Madrigal', 'Tim Anderson', 'Yoan Moncada', 'Eloy Jimenez', 'Luis Robert', 'Nomar Mazara', 'Edwin Encarnacion', 'Zack Collins', 'Danny Mendick', 'Lucas Giolito', 'Dallas Keuchel', 'Gio Gonzalez', 'Dylan Cease', 'Reynaldo Lopez', 'Other'},
         'Cincinnati Reds':{'Tucker Barnhart', 'Curt Casali', 'Joey Votto', 'Mike Moustakas', 'Freddy Galvis', 'Eugenio Suarez', 'Kyle Farmer', 'Nick Castellanos', 'Shogo Akiyama', 'Alex Blandino', 'Aristides Aquino', 'Nick Senzel', 'Jesse Winker', 'Michael Lorenzen', 'Luis Castillo', 'Sonny Gray', 'Trevor Bauer', 'Anthony DeSclafani', 'Wade Miley', 'Other'},
         'Cleveland Indians':{'Roberto Perez', 'Carlos Santana', 'Cesar Hernandez', 'Francisco Lindor', 'Jose Ramirez', 'Oscar Mercado', 'Franmil Reyes', 'Jake Bauers', 'Yu Chang', 'Mike Freeman', 'Sandy Leon', 'Greg Allen', 'Jordan Luplow', 'Carlos Carrasco', 'Mike Clevinger', 'Shane Bieber', 'Zach Plesac', 'Aaron Civale', 'Other'},
         'Colorado Rockies':{'Tony Wolters', 'Daniel Murphy', 'Ryan McMahon', 'Garret Hampson', 'Trevor Story', 'Nolan Arenado', 'Brendan Rodgers', 'Chris Owings', 'Raimel Tapia', 'David Dahl', 'Charlie Blackmon', 'Ian Desmond', 'Sam Hilliard', 'German Marquez', 'Jon Gray', 'Kyle Freeland', 'Antonio Senzatela', 'Other'},
         'Detroit Tigers':{'Austin Romine', 'Grayson Greiner', 'C.J. Cron', 'Jonathan Schoop', 'Niko Goodrum', 'Dawel Lugo' 'Jeimer Candelario', 'Harold Castro', 'Willi Castro', 'Jacoby Jones', 'Christin Stewart', 'Victor Reyes', 'Miguel Cabrera', 'Matthew Boyd', 'Jordan Zimmermann', 'Spencer Turnbull', 'Ivan Nova', 'Daniel Norris', 'Other'},
         'Houston Astros':{'Martin Maldonado', 'Dustin Garneau', 'Yuli Gurriel', 'Jose Altuve', 'Carlos Correa', 'Alex Bregman', 'Aledmys Diaz', 'Michael Brantley', 'George Springer', 'Josh Reddick', 'Kyle Tucker', 'Yordan Alvarez', 'Garrett Stubbs', 'Justin Verlander', 'Zack Grienke', 'Lance McCullers Jr.', 'Jose Urquidy', 'Other'},
         'Kansas City Royals':{'Salvador Perez', "Ryan O'Hearn", 'Nicky Lopez', 'Adalberto Mondesi', 'Maikel Franco', 'Hunter Dozier', 'Humberto Arteaga', 'Matt Reynolds', 'Whit Merrifield', 'Jorge Soler', 'Bubba Starling', 'Brett Phillips', 'Alex Gordon', 'Brad Keller', 'Danny Duffy', 'Jakob Junis', 'Mike Montgomery', 'Glenn Sparkman', 'Other'},
         'Los Angeles Angels':{'Max Stassi', 'Jason Castro', 'Albert Pujols', 'Tommy La Stella', 'David Fletcher', 'Andrelton Simmons', 'Anthony Rendon', 'Juston Upton', 'Mike Trout', 'Brian Goodwin', 'Jo Adell', 'Michael Hermosilllo', 'Shohei Ohtani', 'Andrew Heaney', 'Griffin Canning', 'Dylan Bundy', 'Julio Teheran', 'Other'},
         'Los Angeles Dodgers':{'Mookie Betts', 'Will Smith', 'Enrique Hernandez', 'Max Muncy', 'Gavin Lux', 'Corey Seager', 'Justin Turner', 'Austin Barnes', 'Cody Bellinger', 'Joc Pederson', 'A.J. Pollock', 'Chris Taylor', 'Kyle Garlick', 'Walker Buehler', 'Clayton Kershaw', 'Alex Wood', 'Jimmy Nelson', 'Julio Urias', 'Ross Stripling', 'Other'},
         'Miami Marlins':{'Jorge Alfaro', 'Francisco Cervelli', 'Jesus Aguilar', 'Garrett Cooper', 'Isan Diaz', 'Miguel Rojas', 'Jonathan Villar', 'Corey Dickerson', 'Brian Anderson', 'Harold Ramirez', 'Lewis Brinson', 'Magneuris Sierra', 'Jon Berti', 'Sandy Alcantara', 'Caleb Smith', 'Pablo Lopez', 'Jordan Yamamoto', 'Elieser Hernandez', 'Other'},
         'Milwaukee Brewers':{'Omar Narvaez', 'Manny Pina', 'Justin Smoak', 'Ryan Braun', 'Keston Hiura', 'Orlando Arcia', 'Eric Sogard', 'Jedd Gyorko', 'Avisail Garcia', 'Lorenzo Cain', 'Christian Yelich', 'Ben Gamel', 'Luis Urias', 'Brandon Woodruff', 'Adrian Houser', 'Brett Anderson', 'Josh Lindblom', 'Eric Lauer', 'Other'},
         'Minnesota Twins':{'Mitch Garver', 'Alex Avila', 'Willians Astudillo', 'Miguel Sano', 'Marwin Gonzalez', 'Luis Arraez', 'Ehire Adrianza', 'Jorge Polanco', 'Josh Donaldson', 'Nelson Cruz', 'Max Kepler', 'Byron Buxton', 'Eddie Rosario', 'Jose Berrios', 'Jake Odorizzi', 'Homer Bailey', 'Rich Hill', 'Michael Pineda', 'Randy Dobnak', 'Devin Smeltzer', 'Kenta Maeda', 'Other'},
         'New York Mets':{'Wilson Ramos', 'Pete Alonso', 'Dominic Smith', 'Robinson Cano', 'Amed Rasario', 'Jeff McNeil', 'Michael Conforto', 'Brandon Nimmo', 'J.D. Davis', 'Jake Marisnick', 'Yoenis Cespedes', 'Jed Lowrie', 'Jacob deGrom', 'Noah Syndergaard', 'Marcus Stroman' 'Michael Wacha', 'Rick Porcello', 'Steven Matz', 'Other'},
         'New York Yankees':{'Gary Sanchez', 'Luke Voit', 'DJ LeMahieu', 'Gleyber Torres', 'Gio Urshela', 'Brett Gardner', 'Aaron Judge', 'Giancarlo Stanton', 'Kyle Higashioka', 'Mike Ford', 'Mike Tauchman', 'Clint Frazier', 'Miguel Andujar', 'Gerrit Cole', 'Masahiro Tanaka', 'James Paxton', 'Luis Severino', 'Domingo German', 'J.A. Happ', 'Other'},
         'Oakland Athletics':{'Sean Murphy', 'Matt Olson', 'Franklin Barreto', 'Jorge Mateo', 'Marcus Semien', 'Matt Chapman', 'Chad Pinder', 'Ramon Laureano', 'Mark Canha', 'Stephen Piscotty', 'Robbie Grossman', 'Khris Davis', 'Vimeal Mchin', 'Sean Manaea', 'Frankie Montas', 'Jesus Luzardo', 'Mike Fiers', 'Chris Bassitt', 'Other'},
         'Philadelphia Phillies':{'J.T. Realmuto', 'Andrew Knapp', 'Rhys Hoskins', 'Jean Segura', 'Didi Gregorious', 'Scott Kingery', 'Josh Harrison', 'Phil Gosselin', 'Andrew McCutchen', 'Adam Haseley', 'Bryce Harper', 'Jay Bruce', 'Roman Quinn', 'Aaron Nola', 'Zack Wheeler', 'Jake Arrieta', 'Zach Eflin', 'Vince Velasquez', 'Other'},
         'Pittsburgh Pirates':{'Jacob Stallings', 'Luke Maile', 'Josh Bell', 'Adam Frazier', 'Kevin Newman', 'Cole Tucker', 'Colin Moran', 'Erik Gonzalez', 'Bryan reynolds', 'Gregory Polanco', 'Guillermo Heredia', 'Jason Martin', 'Jose Osuna', 'Joe Musgrove', 'Trevor Williams', 'Chris Archer', 'Mitch Keller', 'Steven Brault', 'Other'},
         'San Diego Padres':{'Francisco Mejia', 'Austin Hedges', 'Eric Hosmer', 'Jurickson Profar', 'Fernando Tatis Jr.', 'Manny Machado', 'Tommy Pham', 'Wil Myers', 'Trent Grisham', 'Manuel Margot', 'Josh Naylor', 'Jake Cronenworth', 'Ty France', 'Chris Paddack', 'Garrett Richards', 'Zach Davies', 'Dinelson Lamet', 'Joey Lucchesi', 'Other'},
         'San Francisco Giants':{'Buster Posey', 'Aramis Garcia', 'Brandon Belt', 'Mauricio Dubon', 'Brandon Crawford', 'Evan Longoria', 'Mike Yastremski', 'Alex Dickerson', 'Steven Duggar', 'Jaylin Davis', 'Chris Shaw', 'Kean Wong', 'Donovan Solano', 'Johnny Cueto', 'Jeff Samardzija', 'Kevin Gausman', 'Drew Smyly', 'Other'},
         'Seattle Mariners':{'Tom Murphy', 'Austin Nola', 'Evan White', 'Shed Long', 'Dee Gordon', 'J.P. Crawford', 'Kyle Seager', 'Daniel Vogelbach', 'Dylan Moore', 'Mitch Haniger', 'Mallex Smith', 'Kyle Lewis', 'Jake Fraley', 'Marco Gonzales', 'Yusei Kikuchi', 'Kendall Graveman', 'Justus Sheffield', 'Justin Dunn', 'Other'},
         'St. Louis Cardinals':{'Yadier Molina', 'Paul Goldschmidt', 'Kolten Wong', 'Paul DeJong', 'Matt Carpenter', 'Tommy Edman', 'Dexter Fowler', 'Harrison Bader', 'Lane Thomas', 'Dylan Carlson', "Tyler O'Neill", 'Andrew Knizner', 'Justin Williams', 'Jack Flaherty', 'Dakota Hudson', 'Miles Mikolas', 'Adam Wainwright', 'Other'},
         'Tampa Bay Rays':{'Mike Zunino', 'Ji-Man Choi', 'Jose Martinez', 'Brandon Lowe', 'Joey Wendle', 'Willy Adames', 'Yandy Diaz', 'Kevin Kiermaier', 'Austin Meadows', 'Hunter Renfroe', 'Yoshitomo Tsutsugo', 'Randy Arozarena', 'Michael Perez', 'Blake Snell', 'Tyler Glasnow', 'Charlie Morton', 'Ryan Yarbrough', 'Yonny Chirinos', 'Other'},
         'Texas Rangers':{'Robinson Chirinos', 'Jeff Mathis', 'Ronald guzman', 'Rougned Odor', 'Elvis Andrus', 'Todd frazier', 'Willie Calhoun', 'Danny Santana', 'Joey Gallo', 'Scott Heineman', 'Shin-Soo Choo', 'Isiah Kiner-Falefa', 'Sam Travis', 'Mike Minor', 'Lance Lynn', 'Corey Kluber', 'Kyle Gibson', 'Jordan Lyles', 'Other'},
         'Toronto Blue Jays':{'Danny Jensen', 'Reese McGuire', 'Travis Shaw', 'Cavan Biggio', 'Bo Bichette', 'Vladmir Guerrero Jr.', 'Brandon Drury', 'Rowdy Tellez', 'Teoscar Hernandez', 'Randal Grichuk', 'Lourdes Gurriel Jr.', 'Derek Fisher', 'Billy McKinney', 'Hyun-Jin Ryu', 'Tanner Roark', 'Matt Shoemaker', 'Chase Anderson', 'Shun Yamaguchi', 'Other'},
         'Washington Nationals':{'Kurt Suzuki', 'Yan Gomes', 'Eric Thames', 'Howie Kendrick', 'Ryan Zimmerman', 'Starlin Castro', 'Trea Turner', 'Asdrubal Cabrera', 'Juan Soto', 'Victor robles', 'Adam Eaton', 'Michael Taylor', 'Carter Kieboom', 'Max Scherzer', 'Stephen Strasburg', 'Patrick Corbin', 'Anibal Sanchez' , 'Other'}}
pitchers={'Arizona Diamondbacks':{'Madison Bumgarner', 'Robbie Ray', 'Mike Leake', 'Luke Weaver', 'Zac Gallen', 'Other'},
         'Atlanta Braves':{'Mike Soroka', 'Mike Foltynewicz', 'Max Fried', 'Cole Hamels', 'Other'},
         'Baltimore Orioles':{'John Means', 'Alex Cobb', 'Kohl Stewart', 'Asher Wojciechowski', 'Keegan Akin', 'Other'},
         'Boston Red Sox':{'Chris Sale', 'Eduardo Rodriguez', 'Nathan Eovaldi', 'Martin Perez', 'Other'},
         'Chicago Cubs':{'Yu Darvish', 'Kyle Hendricks', 'Jon Lester', 'Jose Quintana', 'Other'},
         'Chicago White Sox':{'Lucas Giolito', 'Dallas Keuchel', 'Gio Gonzalez', 'Dylan Cease', 'Reynaldo Lopez', 'Other'},
         'Cincinnati Reds':{'Luis Castillo', 'Sonny Gray', 'Trevor Bauer', 'Anthony DeSclafani', 'Wade Miley', 'Other'},
         'Cleveland Indians':{'Carlos Carrasco', 'Mike Clevinger', 'Shane Bieber', 'Zach Plesac', 'Aaron Civale', 'Other'},
         'Colorado Rockies':{'German Marquez', 'Jon Gray', 'Kyle Freeland', 'Antonio Senzatela', 'Other'},
         'Detroit Tigers':{'Matthew Boyd', 'Jordan Zimmermann', 'Spencer Turnbull', 'Ivan Nova', 'Daniel Norris', 'Other'},
         'Houston Astros':{'Justin Verlander', 'Zack Grienke', 'Lance McCullers Jr.', 'Jose Urquidy', 'Other'},
         'Kansas City Royals':{'Brad Keller', 'Danny Duffy', 'Jakob Junis', 'Mike Montgomery', 'Glenn Sparkman', 'Other'},
         'Los Angeles Angels':{'Shohei Ohtani', 'Andrew Heaney', 'Griffin Canning', 'Dylan Bundy', 'Julio Teheran', 'Other'},
         'Los Angeles Dodgers':{'Walker Buehler', 'Clayton Kershaw', 'Alex Wood', 'Jimmy Nelson', 'Julio Urias', 'Ross Stripling', 'David Price', 'Other'},
         'Miami Marlins':{'Sandy Alcantara', 'Caleb Smith', 'Pablo Lopez', 'Jordan Yamamoto', 'Elieser Hernandez', 'Other'},
         'Milwaukee Brewers':{'Brandon Woodruff', 'Adrian Houser', 'Brett Anderson', 'Josh Lindblom', 'Eric Lauer', 'Other'},
         'Minnesota Twins':{'Jose Berrios', 'Jake Odorizzi', 'Homer Bailey', 'Rich Hill', 'Michael Pineda', 'Randy Dobnak', 'Devin Smeltzer', 'Kenta Maeda', 'Other'},
         'New York Mets':{'Jacob deGrom', 'Noah Syndergaard', 'Marcus Stroman' 'Michael Wacha', 'Rick Porcello', 'Steven Matz', 'Other'},
         'New York Yankees':{'Gerrit Cole', 'Masahiro Tanaka', 'James Paxton', 'Luis Severino', 'Domingo German', 'J.A. Happ', 'Other'},
         'Oakland Athletics':{'Sean Manaea', 'Frankie Montas', 'Jesus Luzardo', 'Mike Fiers', 'Chris Bassitt', 'Other'},
         'Philadelphia Phillies':{ 'Aaron Nola', 'Zack Wheeler', 'Jake Arrieta', 'Zach Eflin', 'Vince Velasquez', 'Other'},
         'Pittsburgh Pirates':{'Trevor Williams', 'Chris Archer', 'Mitch Keller', 'Steven Brault', 'Other'},
         'San Diego Padres':{'Chris Paddack', 'Garrett Richards', 'Zach Davies', 'Dinelson Lamet', 'Joey Lucchesi', 'Other'},
         'San Francisco Giants':{'Johnny Cueto', 'Jeff Samardzija', 'Kevin Gausman', 'Drew Smyly', 'Other'},
         'Seattle Mariners':{'Marco Gonzales', 'Yusei Kikuchi', 'Kendall Graveman', 'Justus Sheffield', 'Justin Dunn', 'Other'},
         'St. Louis Cardinals':{'Jack Flaherty', 'Dakota Hudson', 'Miles Mikolas', 'Adam Wainwright', 'Other'},
         'Tampa Bay Rays': {'Blake Snell', 'Tyler Glasnow', 'Charlie Morton', 'Ryan Yarbrough', 'Yonny Chirinos', 'Other'},
         'Texas Rangers':{'Mike Minor', 'Lance Lynn', 'Corey Kluber', 'Kyle Gibson', 'Jordan Lyles', 'Other'},
         'Toronto Blue Jays': {'Hyun-Jin Ryu', 'Tanner Roark', 'Matt Shoemaker', 'Chase Anderson', 'Shun Yamaguchi', 'Other'},
         'Washington Nationals':{'Max Scherzer', 'Stephen Strasburg', 'Patrick Corbin', 'Anibal Sanchez' , 'Other'}}

popupMenu = OptionMenu(mainframe, tkvar1, *MLBteams1, command=set_up_road)
Label(mainframe, text="Road Team:").grid(row = 0, column = 0)
popupMenu.grid(row = 0, column =1)
Label(mainframe, text="Home Team:").grid(row=0, column=2)
popupMenu2=OptionMenu(mainframe,tkvar2,*MLBteams2, command=set_up_home)
popupMenu2.grid(row=0, column=3)
Label(mainframe,text="Lineups:").grid(row=1, column=0)
Label(mainframe,text="Primary Pitcherz").grid(row=10, column=0)

hitters_list1=hitters[tkvar1.get()]
pitchers_list1=pitchers[tkvar1.get()]

hitters_list2=hitters[tkvar2.get()]
pitchers_list2=pitchers[tkvar2.get()]

set_up_home()
set_up_road()

b=Button(mainframe,text="Check Teams Selected", command=get_players)
c=Button(mainframe,text="Calculate Percentage", command=calculate_percentage)
b.grid(row=11, column=1)
c.grid(row=11, column=3)


# on change dropdown value
def stuff():
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
