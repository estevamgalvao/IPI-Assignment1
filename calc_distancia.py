#[Sudoeste, Sul, Sudeste] =  [(x-1;y+1), (x;y+1), (x+1;y+1)]  =  [0,1,2]
#[Oeste ,  Centro  , Leste]  =  [(x-1;y)  , (x;y)  , (x+1;y)  ]  =  [3,x,4]
#[Noroeste , Norte , Nordeste]  =  [(x-1;y-1), (x;y-1), (x+1;y-1)]  =  [5,6,7]

# Atribuo nomes de direções para facilitar no entendimento
# Atribuo os nomes invertidos pois as coordenadas da matriz da imagem crescem de cima pra baixo

def calc_distancia(atualX, atualY, destinoX, destinoY):
  listDistancias = [0,0,0,0,0,0,0,0]

  sudoeste = (((destinoX - (atualX-1))**2)
                       +((destinoY - (atualY+1))**2))**(1/2)

  sul = (((destinoX - (atualX))**2)
                       +((destinoY - (atualY+1))**2))**(1/2)

  sudeste = (((destinoX - (atualX+1))**2)
                       +((destinoY - (atualY+1))**2))**(1/2)

  oeste = (((destinoX - (atualX-1))**2)
                       +((destinoY - (atualY))**2))**(1/2)

  leste = (((destinoX - (atualX+1))**2)
                       +((destinoY - (atualY))**2))**(1/2)

  noroeste = (((destinoX - (atualX-1))**2)
                       +((destinoY - (atualY-1))**2))**(1/2)

  norte = (((destinoX - (atualX))**2)
                       +((destinoY - (atualY-1))**2))**(1/2)

  nordeste = (((destinoX - (atualX+1))**2)
                       +((destinoY - (atualY-1))**2))**(1/2)

  listDistancias[0] = [sudoeste, atualX-1, atualY+1]
  listDistancias[1] = [sul, atualX, atualY+1]
  listDistancias[2] = [sudeste, atualX+1, atualY+1]
  listDistancias[3] = [oeste, atualX-1, atualY]
  listDistancias[4] = [leste, atualX+1, atualY]
  listDistancias[5] = [noroeste, atualX-1, atualY-1]
  listDistancias[6] = [norte, atualX, atualY-1]
  listDistancias[7] = [nordeste, atualX+1, atualY-1]

  return listDistancias
