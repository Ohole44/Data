City Air Pollution Data Extractor

This uses the [OpenWeather Air Pollution API](https://openweathermap.org/api/air-pollution) to fetch real-time air quality data for a specified location and saves it to an Excel file. You know....if you care about the air you breathe.

---

Features

- Retrieves current air pollution data using latitude and longitude
- Extracts key pollutants: CO, NO, NO₂, O₃, SO₂, NH₃, PM2.5, PM10
- Includes Air Quality Index (AQI) level
- Saves data to a clean Excel spreadsheet

---

Dependencies

requests- makes the http call to the API
pandas- structures data
openpyxl- Allows to save the data frame to an excel file
