# TGJU.org ✨ Unofficial API Documentation

> ⚡️ This guide documents findings from reverse engineering the [tgju.org](https://www.tgju.org/) API, providing live Iranian exchange rates, precious metals, and economic info.  
> 🚨 **Note:** This is not an official or public API. Use with caution regarding legal, ethical, and reliability concerns.

---

## ⚙️ Base API Endpoint

```http
GET https://call3.tgju.org/ajax.json?rev={sS6c6AGKSb5ba24j7ZZmhqj6ohg1z5qoIzCKE9nfC6jLfPOLLHFN7n27Po5J}
```

- `rev`: Appears to be a session, signature, or anti-scraping value. If changed, results or access may differ.
- The response is in **JSON** format.

---

## 📦 Example Response Structure

The API returns a JSON object with a primary key named `"current"`.  
Each entry under `"current"` is its own asset/currency object, keyed by the symbol or market code.

```json
{
  "current": {
    "zinc": {
      "p": "2575.6",
      "h": "2575.6",
      "l": "2575.6",
      "d": "0",
      "dp": 0,
      "dt": "",
      "t": "۷ تیر",
      "t_en": "28 Jun",
      "t-g": "۷ تیر",
      "ts": "2021-06-28 15:00:00"
    },
    "yemen@kwd-sell": {
      "p": "815.6168",
      "h": "815.6168",
      "l": "815.6168",
      "d": "0",
      "dp": 0,
      "dt": "",
      "t": "۲۱ اردیبهشت",
      "t_en": "11 May",
      "t-g": "۲۱ اردیبهشت",
      "ts": "2022-05-11 00:29:41"
    },
    "xrp-irr": {
      "p": "70000",
      "h": "70000",
      "l": "69000",
      "d": "0",
      "dp": 0,
      "dt": "",
      "t": "۲۱ آبان",
      "t_en": "11 Nov",
      "t-g": "۲۱ آبان",
      "ts": "2020-11-11 17:00:00"
    }
    // ... more currencies/assets
  }
}
```

---

## 🔑 Response Field Meaning

Each asset includes:

| Field   | Type     | Description                                   |
| ------- | -------- | --------------------------------------------- |
| `p`     | string   | Price                                         |
| `h`     | string   | Highest value                                 |
| `l`     | string   | Lowest value                                  |
| `d`     | string   | Change from previous                          |
| `dp`    | number   | Change percent                                |
| `dt`    | string   | Description or tag                            |
| `t`     | string   | Date (Persian calendar, Farsi)                |
| `t_en`  | string   | Date (Gregorian, English)                     |
| `t-g`   | string   | Date (Persian calendar, Farsi)                |
| `ts`    | string   | Timestamp, full date and time                 |

---

## 🏷️ Asset Codes & Markets

- Each key under `"current"` (e.g., `"zinc"`, `"xrp-irr"`, `"usd"`, `"yemen@kwd-sell"`) identifies a symbol, market, or asset.
- Codes often represent currency pairs, commodities, metals, or foreign exchanges.

---

## 📲 Authentication & Headers

- No authentication (token/cookie) usually required.
- For extended scraping or automation, mimicking browser headers (User-Agent, Referer) is recommended.

---

## 👉 Usage Example (Python)

```python
import requests

url = "https://call3.tgju.org/ajax.json?rev=sS6c6AGKSb5ba24j7ZZmhqj6ohg1z5qoIzCKE9nfC6jLfPOLLHFN7n27Po5J"
resp = requests.get(url)
data = resp.json()
print(data['current'])
```

---

## ⚠️ Notes & Caveats
- Data may change, API may block or rate-limit.
- Some asset symbols may update or be removed.
- Use at your own risk; respect tgju.ir terms of service.

---

## 📝 Contributed by
**ZoneRCM**  
Date: 2025-11-30
