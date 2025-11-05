from main import clean_text

print("Test 1 dla **test**")
print(clean_text("**test**"))

print("\n" + "="*50 + "\n")

print("Test 2")
print(clean_text("""# Przewodnik po Pythonie dla początkujących
## Wprowadzenie
Python to **potężny** i *łatwy w nauce* język programowania. Jest idealny dla osób, które dopiero zaczynają swoją przygodę z kodowaniem.

## Podstawowe typy danych

### Liczby
Python obsługuje różne typy liczbowe:
- **Integers** (liczby całkowite): `42`, `-17`, `0`
- **Floats** (liczby zmiennoprzecinkowe): `3.14`, `-0.001`, `2.0`
- **Complex** (liczby zespolone): `3+4j`

### Stringi
Teksty w Pythonie można definiować na kilka sposobów:
```python
tekst1 = "Hello World"
tekst2 = 'Python jest super'
```

## Struktury kontrolne

### Pętla for
```python
for i in range(5):
    print(f"Iteracja numer {i}")
```

### Instrukcja if
Warunki pozwalają na *dynamiczne* podejmowanie decyzji:
```python
if wiek >= 18:
    print("Jesteś **pełnoletni**")
else:
    print("Jesteś *niepełnoletni*")
```

## Lista funkcji wbudowanych

1. `print()` - wyświetla tekst
2. `len()` - zwraca długość
3. `type()` - sprawdza typ danych
4. `input()` - pobiera dane od użytkownika
5. `range()` - generuje sekwencję liczb

## Tabela operatorów

| Operator | Znaczenie | Przykład |
|----------|-----------|----------|
| `+` | Dodawanie | `5 + 3 = 8` |
| `-` | Odejmowanie | `10 - 4 = 6` |
| `*` | Mnożenie | `3 * 7 = 21` |
| `/` | Dzielenie | `15 / 3 = 5.0` |
| `**` | Potęgowanie | `2 ** 3 = 8` |
## Linki i zasoby
- [Oficjalna dokumentacja](https://docs.python.org)
- [Python Tutorial](https://www.python.org/about/gettingstarted/)
- ***Stack Overflow*** - najlepsze forum dla programistów
## Podsumowanie
> Python to język, który ***łączy prostotę z mocą***. 
> Idealny do nauki i profesjonalnych projektów!
---
**Pamiętaj**: Praktyka czyni mistrza! 🐍
*Powodzenia w nauce programowania!*"""))