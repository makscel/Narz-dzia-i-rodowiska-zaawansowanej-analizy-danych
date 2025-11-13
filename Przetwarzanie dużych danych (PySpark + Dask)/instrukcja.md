# **PYSPARK**





Dla danych sms.csv:



Wyświetl podgląd 10 pierwszych wierszy.

Wyświetl następujące statystyki: 

liczba wszystkich wierszy,

procent przykładów z klas 0 i 1,

długość najkrótszego  i najdłuższego tekstu,

średnia długość tekstu.

Narysuj histogram długości tekstów.





Przygotuj dane sms.csv do modelowania:



Podziel je na część treningową (70% zbioru) i testową (30%), zachowując rozkład klas.

Usuń interpunkcję i cyfry.

Usuń słowa pojawiające się w pliku stopwords.txt

Stokenizuj dane.

Zastosuj HashingTF.

Wyświetl podgląd pierwszych 5 wierszy i pierwszych 5 kolumn zbioru treningowego.



Na przygotowanych wcześniej danych treningowych zbuduj model regresji logistycznej.



Oceń wytrenowany model na zbiorze testowym:

Wyświetl macierz pomyłek.

Podaj wartości następujących metryk: Accuracy, Sensitivity, Specificity.



Za pomocą wyznaczonego modelu oblicz prawdopodobieństwo przynależności do klasy 0/1 dla tekstów zbioru testowego i podaj:

Tekst o najwyższym szacowanym prawdopodobieństwie przypisania do klasy 0.

Tekst o najwyższym szacowanym prawdopodobieństwie przypisania do klasy 1.

Prawdopodobieństwo klasy 1 (spam) dla tekstu: "How many machine learning specialists does it take to change a light bulb? - Just one, but they require a million light bulbs to train properly".



# **DASK**



Dla danych sms.csv:



Wyświetl podgląd 10 pierwszych wierszy.

Wyświetl następujące statystyki: 

liczba wszystkich wierszy,

procent przykładów z klas 0 i 1,

długość najkrótszego  i najdłuższego tekstu,

średnia długość tekstu.

Narysuj histogram długości tekstów.





Przygotuj dane sms.csv do modelowania:



Podziel je na część treningową (70% zbioru) i testową (30%), zachowując rozkład klas.

Usuń interpunkcję i cyfry.

Usuń słowa pojawiające się w pliku stopwords.txt

Stokenizuj dane, zastosuj „hashing trick” i zamień teksty na wektory.

Wyświetl podgląd pierwszych 5 wierszy i pierwszych 5 kolumn zbioru treningowego.



Na przygotowanych wcześniej danych treningowych zbuduj model regresji logistycznej.



Oceń wytrenowany model na zbiorze testowym:

Wyświetl macierz pomyłek.

Podaj wartości następujących metryk: Accuracy, Sensitivity, Specificity.



Za pomocą wyznaczonego modelu oblicz prawdopodobieństwo przynależności do klasy 0/1 dla tekstów zbioru testowego i podaj:

Tekst o najwyższym szacowanym prawdopodobieństwie przypisania do klasy 0.

Tekst o najwyższym szacowanym prawdopodobieństwie przypisania do klasy 1.

Prawdopodobieństwo klasy 1 (spam) dla tekstu: "How many machine learning specialists does it take to change a light bulb? - Just one, but they require a million light bulbs to train properly".

