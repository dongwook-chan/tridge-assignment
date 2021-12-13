# Calendar Problem
Convert numbers from base 10 integers to base N strings and back again.  

## Usage and Examples
Example to convert 10 to binary and '1010' back to decimal  
```bash
(env) $ cd 2-base-converter
(env) $ python3 transformer.py --digits '01' --from_decimal 10  --to_decimal '1010'
```
| keyword | required | type |
| :-: | :-: | :-: |
| digits | True | str |
| from_decimal | False | int |
| to_decimal | False | str |