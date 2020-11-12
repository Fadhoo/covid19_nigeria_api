# Covid19 Nigeria Data API

This API provides data about covid19 in Nigeria from the NCDC website.

---
### Usage
Visit the API's dashboard at: https://covid19-nigeria-api.herokuapp.com/ncdc_data/home/
to realtime data.

#### Request
**GET**
https://covid19-nigeria-api.herokuapp.com/ncdc_data/

#### Response
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "today": {
            "samples_tested": "687,952",
            "confirmed_cases": "64,184",
            "active_cases": "2,957",
            "discharged_cases": "60,069",
            "deaths": "1,158"
        }
    },
    {
        "last_month": {
            "samples_tested": "625,510",
            "confirmed_cases": "62,691",
            "active_cases": "3,117",
            "discharged_cases": "58,430",
            "deaths": "1,144"
        }
    }
]
___
### Contributors
- Fadipe Al-Ameen O. <fadipetomi00@gmail.com>
