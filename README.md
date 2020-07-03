# pyssword
A python-based password generator. It uses a master password and encodes it with a inserted text.

## Requirements
 - Python `v3.5+`

## Usage
Put pyssword.py somewhere in your project and then include it where needed

```python
import pyssword

generated = pyssword.generate("password", "modifier")
print(generated)
```
