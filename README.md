# Edycja readme przez członków zespołu

## Gaba
Rotacja klocka w grze Tetris

Funkcja rotacji klocka w grze Tetris jest odpowiedzialna za obracanie aktualnie spadającego klocka w lewo wokół jego środka. Obrót klocka jest kluczowym elementem rozgrywki, ponieważ pozwala graczowi na lepsze dopasowanie klocka do istniejącej konfiguracji na planszy, co może prowadzić do wypełnienia linii i zdobycia punktów.
Implementacja rotacji

Poniższy fragment kodu przedstawia implementację funkcji rotacji klocka w grze Tetris:
'''python
def rotate(self, grid):
  self.erase_shape(grid)
  rotated_shape = []
  for x in range(len(self.shape[0])):
      new_row = []
      for y in range(len(self.shape)-1, -1, -1):
          new_row.append(self.shape[y][x])
      rotated_shape.append(new_row)
  
  right_side = self.x + len(rotated_shape[0])
  if right_side < len(grid[0]):
      self.shape = rotated_shape
      # update height and width
      self.height = len(self.shape)
      self.width = len(self.shape[0])
'''

## Bartek
Kolorystyka w grze TETRIS
Plansza gry Tetris składa się z czarnego lub ciemnego tła, które kontrastuje z kolorowymi klockami. Klocki w Tetrisie występują w różnych kolorach, zwykle są to jasne, intensywne barwy - czerwony, niebieski, zielony, żółty i fioletowy. 

Każdy klocek ma swój unikalny kolor, co ułatwia graczowi ich rozróżnienie podczas rozgrywki. Kontrast między jasnymi kolorami klocków a ciemnym tłem planszy zapewnia czytelność i przejrzystość gry, co jest ważne dla szybkiego podejmowania decyzji przez gracza.

Możliwość dostosowania kolorystyki według preferencji gracza. Można zmieniać kolory klocków, tła czy innych elementów graficznych, by pozwolić na spersonalizowanie wizualnego doświadczenia gry.

## Lidia

Grawitacja w grze TETRIS
* W różnych wersjach Tetrisa oraz grach opartych na tym schemacie istnieją co najmniej trzy algorytmy obsługujące spadanie elementów po usunięciu wiersza
Oryginalny algorytm: po usunięciu wiersza leżące ponad nim elementy spadają o poziom w dół (analogicznie w przypadku gdy usunięto za jednym razem większą liczbę wierszy), ale nie dalej, nawet jeśli jakaś kolumna elementów mogłaby spaść dalej.
* Popularny[potrzebny przypis] algorytm będący modyfikacją oryginalnego: po usunięciu wiersza kolumny elementów nad nim przesuwają się w dół (przy zachowaniu względnego położenia klocków w kolumnie) najniżej, jak jest to możliwe. O ile w oryginalnym algorytmie usunięcie wiersza (lub wierszy) nie pociągało za sobą kolejnych, tak w tym przypadku taka sytuacja może zajść (gdy np. element spadającej kolumny wypełni jedyne puste pole w wierszu niżej).
* Algorytm najbardziej odległy od oryginału, wykorzystywany w bardziej złożonych grach opartych na tym samym pomyśle co Tetris: usunięcie wiersza pociąga za sobą reorganizację zarówno elementów nad, jak i pod nim – wszystkie elementy, nie zachowując względnego położenia w kolumnach, przesuwają się w dół planszy tak, że wypełniają wszystkie luki powstałe pomiędzy nimi w trakcie gry. Podobnie jak w poprzednim przypadku, może to pociągnąć za sobą usunięcie kolejnych wierszy elementów.

Niektóre rodzaje bloków:
1. Tetrimino „I” – cztery elementy w jednym szeregu
2. Tetrimino „O” – cztery elementy połączone w kwadrat
3. Tetrimino „J” – trzy elementy w rzędzie i jeden dołączony do prawego elementu od spodu

Źródło: [wikipedia](https://pl.wikipedia.org/wiki/Tetris)

Fragment kodu z naszej implementacji gry:
```python
wn = turtle.Screen()
wn.title("tetris")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0) 
```

| Komenda | Opis |
| --- | --- |
| `turtle.forward(distance)` | Move the turtle forward by the specified distance, in the direction the turtle is headed. |
| `turtle.pendown()` | Pull the pen down – drawing when moving |

![piesek](animals/dog.jpg)

![na zdjeciu jest jez](animals/hedgehog.jpg)



## Patryk




# NI-project
Project for our IT tools classes

## Description

The main goal of our project is to create a simple game and learn IT tools in the process. We agreed on coding a tetris-like game in Python. As we are not very advanced in Python and have different levels of experience in programming, the technical part of the project will be mostly basic. We are not going to use advanced libraries; we will stick to the ones that we already have some experience with.

## Getting Started

### Dependencies

* Python 3
* Turtle library
* Windows 10

### Installing

* Install some python Ide: Pycharm, Visual Code, and run our code on it

### Executing program

* Run the main file of the program

## Help
<details>
  <summary>Solutions to some problems</summary>
  Write to us, we will be very happy to help you 😄
  
</details>



## Authors

Contributors names

- Patryk  
- Gaba  
- Lidia  
- Bartek  


## Other ideas

Slowing down the block: [Example](https://www.youtube.com/watch?v=dHeLjKB2DKc&ab_channel=okCobalt)

