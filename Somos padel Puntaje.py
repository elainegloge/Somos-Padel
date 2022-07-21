import pandas as pd 
players=pd.DataFrame([
    ['Player1' , 'Edgar Mondragon'],
    ['Player2' , 'Patricio Ramos'],
    ['Player3' , 'Andoni Garmendia'],
    ['Player4' , 'Jonathan Mondragon'],
    ['Player5' , 'Ivan Mondragon'],
    ['Player6' , 'Alberto Morales'],
    ['Player7' , 'Ramses Medina'],
    ['Player8' , 'Aldo Perez'],
    ['Player9' , 'Edson Neri'],
    ['Player10' , ""],
    ['Jugador1' , 'Lonardo Neri'],
    ['Jugador2' , 'David'],
    ['Jugador3' , 'Emmanuel'],
    ['Jugador4' ,  'Miguel'],
    ['Jugador5' , 'Ricardo'],
    ['Jugador6' , 'Isaac'],
    ['Jugador7' , 'Sebas Neri'],
    ['Jugador8' , 'Carlos'],
    ['Jugador9' , 'Oscar'],
    ['Jugador10' , ""]
])
players.columns=['Player','Name']
players['Puntaje']=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
list=pd.read_excel('Sales Prgramming.xlsx')
players.to_excel('Puntaje.xlsx',index=False)
#players['Puntaje']=list['Ganador'].apply(lamda x: +3 for )
#if list['Ganador'] = 1 :
  #  if list['Player 1'] = players[["Player"]] :
   #     players['Puntaje']=+3
    #players['Puntaje'].where(list['Player 1'] = players['Player']) = +3
    #players['Puntaje'].where(list['Player 2'] = players['Player']) = +3
    
#else :
 #   players['Puntaje'].where(list['Player 3'] = players['Player']) = +3
  #  players['Puntaje'].where(list['Player 4'] = players['Player']) = +3
