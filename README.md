# water_flask
Water your home plants with raspberry, a relay and a water pump.

___
## Todo
### Software
- enables automatic deploy of code in raspberry at every pull/startup of the device
- enables the flask application to store the events and show them to the user
- The layout could look like
-- /home
-- /logs

in /home the user can turn on/off the pump

in /home the user can set an ON time for the pump, starting from now, after this time is expired the pump turns off

in /logs the user can see all the events (ON/OFF), sorted by date

### Hardware
- cut plastic tube and fit it to the plants
- setup a big tank of water (reservoir)
---

### Future features
- Enables a calendarized water schedule, the user can create an event on its calendar (google calendar), the raspberry source it and execute the watering for as long as it is asked.
- enables an always available water (from the main pipe) with a valve
