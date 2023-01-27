# JS_projekt

Tematem projektu było zaimplementowanie automatu przechowującego informacje o znajdujących się w nim monetach (1, 2, 5, 10, 20, 50gr, 1, 2, 5zł) oraz o towarach –przedmiotach o numerach od 30 do 50), każdy o określonej cenie w określonej liczbie (domyślnie po 5 sztuk każdego towaru).

Automat wyposażony jest w: 
* okno z przyciskami pozwalającymi na wrzucanie monet, 
* pole wyświetlające kwotę wrzuconych monet, 
* pole wyświetlające wpisane numery towaru, 
* pole wyświetlające hasła akcji,
* przycisk przerywający transakcję (wyrzuca wrzucone monety), 
* przyciski 0-9 pozwalające wpisać numer wybranego towaru, 
* przycisk czyszczący wpisany numer,
* przycisk zatwierdzający wybranie konkretnego numeru towaru.


## Funkcjonalność

Po wybraniu poprawnego numeru towaru: Jeśli wrzucono za mało monet, wyskakuje okno z informacją o cenie towaru oraz (jeśli towar się skończył) o jego braku w automacie. Jeśli wrzucono monety, których wartość jest większa lub równa cenie wybranego towaru, automat sprawdza czy towar jest dostępny i czy może wydać resztę. 

W momencie, gdy automat nie jest w stanie wydać resztę informuje o przyjmowaniu tylko odliczonej kwoty. Następuje zwrot wcześniej wrzuconych pieniędzy.

Gdy automat jest w stanie wydać resztę, pokazuje wydaną kwotę na wyświetlaczu, odejmuje towar z listy dostępnych produktów oraz dodaje do sumy pieniędzy otrzymaną w wyniku zakupu kwotę.
