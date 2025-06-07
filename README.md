# gpt-2

This repository contains simple utilities. The `currency_converter.py` script
provides real-time currency conversion between Russian rubles (RUB), euros
(EUR), US dollars (USD), and Kazakhstani tenge (KZT). It fetches current rates
from the [exchangerate.host](https://exchangerate.host) API.

## Usage

Run the script with Python and follow the prompts:

```bash
python currency_converter.py
```

You'll be asked for the amount, the source currency, and the target currency.
The script outputs the converted amount using the latest available exchange
rate.
