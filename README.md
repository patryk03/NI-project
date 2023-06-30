# Edycja readme przez członków zespołu

## Gaba
MOC SPOWALNIANIA
Moc spowolnienia to specjalna umiejętność dostępna w grze Tetris, która pozwala graczu na tymczasowe zmniejszenie prędkości spadania klocków. Gdy moc spowolnienia zostanie zdobyta, gracze mogą aktywować ją w dowolnym momencie, aby uzyskać przewagę i lepiej kontrolować klocki.

Po aktywowaniu mocy klocki przez 5 sekund lecą 2 razy wolniej ułatwiając graczom ulożenie klocków w korzystny dla nich sposób.

Dlaczego tempo gry jest istotne:[YouTube] (https://www.youtube.com/watch?v=dHeLjKB2DKc&ab_channel=okCobalt)
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

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help
<details>
  <summary>Solutions to some problems</summary>
  Write to us, we will be very happy to help you 😄
  
</details>



## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

