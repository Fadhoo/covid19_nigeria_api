# Covid19 Nigeria Data API

This API provides data about covid19 in Nigeria.

---
### Usage

#### Request
**GET**
https://covid19-nigeria-api.herokuapp.com/ncdc_data/

#### Response
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "samples_tested": "363,331",
    "confirmed_cases": "49,895",
    "active_cases": "15,204",
    "discharged_cases": "33,710",
    "deaths": "981"
}

___
### Contributors
- Fadipe Al-Ameen O. <fadipetomi00@gmail.com>