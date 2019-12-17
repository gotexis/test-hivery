# Paranuara Challenge

## envs

Sets database resource file, for example:

* `HIVERY_COMPANIES_JSON` = `d:/companies.json`
* `HIVERY_PEOPLE_JSON` = `~/ppl.json`


## testing

`python -m unittest tests`

## installing

`pip install git+https://github.com/gotexis/hivery.git`

## running

```python
from hivery.app import app
app.run()
```
