# Data Structures and Algorithms Assessment

## Phase 3 Week 2 Compulsory Lab

## Stacks

### Question 1

Implement a function `is_balanced(expression)` that takes a string
containing parentheses, curly braces, and square brackets,and determines whether the expression is balanced.

*An expression is considered balanced if each opening bracket has a corresponding closing bracket in the correct order.*

```python
sample input:

expression1 = "([]{})"
expression2 = "([)]"

print(is_balanced(expression1)) 
print(is_balanced(expression2))

# True
# False
```

## Sequences (Lists/Tuples)

### Question 2

Write a function `remove_duplicates(sequence)` that takes a sequence (list or tuple) and returns a new sequence with duplicates removed while maintaining the original order of elements.

```python
sample input:

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]

result = remove_duplicates(input_sequence)

print(result) 

# [2, 3, 4, 5, 6, 7]
```

## Dictionaries

### Question 3

Implement a function `word_frequency(sentence)` that takes a sentence and returns a dictionary containing the frequency of each word in the sentence.

> Ignore punctuation and consider words in a case-insensitive manner.

```python
sample input:

sentence = "This is a test sentence? I'm sure this is a test sentence."

result = word_frequency(sentence) 

print(result) 

# {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2, "i'm": 1, 'sure': 1}
```

## Authors

- [Arshavine Waema](https://github.com/ArshavineRoy)
- [Helder Lucau](https://github.com/Helder-Lucau)
- [Grace Maina](https://github.com/njagiiii)
- [Victor Odambatafwa](https://github.com/VictorOdambatafwa22)
- [Edmond Wanyama](https://github.com/wanyama23)

## License

Licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
