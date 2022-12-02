<b>Python-Matrix</b> (Petr Pelikán)
==================================

<b>Úvod</b> 
-----------
Tento soubor slouží jako dokumentace třídy Matice (Python-Matrix), školního projektu na cvičení Programování 1 (NPRG030).
Popisuje veškeré funkce, které třída umí, společně s jejich funkčností.

<b>Konstruktory</b>
-------------------
- Funkce, které vytvoří instanci třídy Matice. Každá z nich vytvoří se stejnými daty datově identickou matici, liší se pouze ve způsobu zadání informací.

- Každá z konstruktorů ohlásí chybu, pokud zjistí, že se ve všech řádcích neshoduje počet čísel.

- Třída obsahuje <b>čtyři</b> konstruktory, z čehož <b>tři</b> slouží k implementování do projektu s maticemi, jmenovitě

  - <b>Matrix.fromString( <i>inputString, rowSplitChar="@", colSplitChar="&" </i> )</b>

      <p>Konstruktor má jediný povinný parametr, vstupní řetězec. Řádky se oddělují defaultně pomocí at (@) symbolu,
      sloupce pomocí ampersand (&) symbolu, ovšem dají se nastavit v parametrech funkce.</p>

      <p>Konstruktor ohlásí chybu, pokud matice nebude čtvercová či obdélníková (ve dvou řádcích bude různý počet čísel).</p>

      ```python
      from MatrixClass import Matrix

      A = Matrix.fromString("2&3&4@3&4&5@4&5&6")
      print(A)
      ```

      Výstup:

      ```bash
      -- Matrix --
      | 2 3 4 |
      | 3 4 5 |
      | 4 5 6 |
      ```
  - <b>Matrix.from2DList( <i>2dList</i> )</b>

      <p>Konstruktor má jediný parametr, dvojrozměrný list.</p>

      ```python
      from MatrixClass import Matrix

      A = Matrix.from2DList([[6/3,7/4,4],[3,4/3,8/5],[5,7,85]])
      print(A)
      ```

      Výstup:

      ```bash
      -- Matrix --
      |  2  7/4  4  |
      |  3  4/3 8/5 |
      |  5   7  85  |
      ```
  - <b>Matrix.fromLists( <i>*lists</i> )</b>
      ```python
      from MatrixClass import Matrix

      A = Matrix.fromLists([6/3,7/4,4],[3,4/3,8/5],[5,7,85])
      print(A)
      ```

      Výstup:

      ```bash
      -- Matrix --
      |  2  7/4  4  |
      |  3  4/3 8/5 |
      |  5   7  85  |
      ```

- a poslední <b>čtvrtý</b> interaktivní konstruktor slouží spíše na debugování a testy. Konstruktor čte v reálném čase ze vstupu od uživatele.
    - <b>Matrix.fromInput( )</b>
  
        ```python
        from MatrixClass import Matrix

        A = Matrix.fromInput()
        ``` 
 


<b>Pretty-print</b>
-------------------
  - Funkce sloužící k výpisu dat z instance Matice v uživatelsky přívětivé podobě, oproti výpisu samotných dat uložených v instanci.
  -   <b>print( <i>matrixInstance</i> )</b>

```python
from MatrixClass import Matrix

A = Matrix.from2DList([[2,3,4],[3,4,5],[4,5,6]])

print("výpis raw dat:")
print(A.matrix)

print()
print("---")
print()

print("Pretty-print matice:")
print(A)

```
Výstup:

```bash
výpis raw dat:
[[Fraction(2, 1), Fraction(3, 1), Fraction(4, 1)], [Fraction(3, 1), Fraction(4, 1), Fraction(5, 1)], [Fraction(4, 1), Fraction(5, 1), Fraction(6, 1)]]

---

Pretty-print matice:
-- Matrix --
| 2 3 4 |
| 3 4 5 |
| 4 5 6 |
```

<b>Matematické funkce</b>
-------------------------
- Ve třídě Matrix jsou implementovány funkce k základním operacím s maticemi.
- Instance třídy Matrix je <b>immutable</b>(neměnná) -> čísla uložená v instanci není možné přenastavit.

- <b>Porovnání</b>
  - Pro zjištění rovnosti dvou matic užívá třída <b>( == )</b>, porovnávání (<,>,<=,>=) pro matice není definováno.
  ```python
    from MatrixClass import Matrix

    a = Matrix.from2DList([[2,3],[3,4]])
    b = Matrix.fromString([[4,6],[5,7]])

    print(a == b)
    ```
    Výstup:
    ```bash
    False
    ```


- <b>Sčítání</b>
  - Pro sečtení dvou matic užívá třída <b>znak (+)</b>
  ```python
    from MatrixClass import Matrix

    a = Matrix.from2DList([[2,3],[3,4]])
    b = Matrix.fromString([[4,6],[5,7]])

    abSum = a + b
    print(abSum)
    ```
    Výstup:
    ```bash
    -- Matrix --
    | 6  9  |
    | 8  11 |
    ```

- <b>Násobení</b>
  - Pro vynásobení matice konstantou nebo vynásobení dvou matic užívá třída <b>znak ( * )</b>
  ```python
    from MatrixClass import Matrix

    a = Matrix.from2DList([[2,3],[3,4]])
    b = Matrix.from2DList([[4,6],[5,7]])
    const = 5

    aTimesConst = a * const
    abProd = a * b
    baProd = b * a

    print("Constant multiplication: ")
    print(aTimesConst)
    print("________")

    print("Product of both matrices: ")
    print(abProd)
    print("________")

    print("Product of both matrices in switched order: ")
    print(baProd)
    ```
    Výstup:
    ```
    Constant multiplication: 
    -- Matrix --
    | 10 15 |
    | 15 20 |
    ________
    Product of both matrices: 
    -- Matrix --
    | 23 33 |
    | 32 46 |
    ________
    Product of both matrices in switched order: 
    -- Matrix --
    | 26 36 |
    | 31 43 |
    ```






