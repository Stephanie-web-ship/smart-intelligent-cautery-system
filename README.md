
# Overview

The Smart Intelligent Cautery System (SICS) is a web-based simulation designed to improve temperature monitoring and control during electrosurgical procedures.
Conventional cautery systems mainly operate based on fixed power settings, which can lead to excessive heating, tissue damage, carbonization, and increased surgical smoke generation. This project introduces a temperature-based control approach that focuses on maintaining safe thermal conditions.
The system simulates real-time temperature variation and uses predefined thermal parameters to monitor cautery behavior.

---

# Features

- Selection of different tissue types and biological materials
- Displays thermal parameters:
  - Minimum Effective Temperature (MET)
  - Safe Operating Zone (SOZ)
  - Threshold Temperature
- Real-time temperature vs time graph visualization
- Rule-based crisp logic control mechanism
- Threshold detection and temperature regulation simulation
- Cooling phase simulation after procedure completion

---

# Working Principle

The system works using a closed-loop temperature monitoring concept.
In a real-time implementation, a thermocouple placed near the cautery electrode tip can collect temperature readings. These readings can be used as feedback to adjust the output power and maintain temperature within safe operating limits.
The current simulation uses crisp logic, where predefined threshold values determine system response.

Example:

- If temperature approaches threshold → Reduce power
- If temperature remains in SOZ → Continue operation
- If temperature goes below the MRT → Increase power

---

# Technologies Used

- Python
- Flask Framework
- HTML
- CSS
- JavaScript
- Chart.js

---
