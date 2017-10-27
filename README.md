# Strategy Pattern
Sample problem featuring the strategy pattern.

## Task 1 - Reduce prices
Welcome to Pizza<sup>2</sup>! Pizza<sup>2</sup> makes round pizzas for now. See for yourself by running the following command:

```
python __main__.py -s round -l 8
```
Pizza<sup>2</sup> wants to expand to making square pizzas since Chicago style is all the fad these days. Implement the strategy design pattern to calculate the amount of dough needed to make a square pizza.

### Previous output

```
The 8 inch, round pizza needs 4.4466919372480005 ounces of dough.
```

### Desired output

```
The 8 inch, square pizza needs 5.6617088 ounces of dough.
```

## Task 2 - Testing

Our test coverage is pretty terrible. See for yourself by running the following commands:

```
coverage run --source strategy -m unittest discover tests
coverage report -m
```

Increase this to 100%.
