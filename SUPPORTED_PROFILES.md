# Supported profiles
All profiles (should) correspond to the official [EEP](http://www.enocean-alliance.org/eep/) by EnOcean.

### RPS Telegram (0xF6)
##### RORG 0xF6 - FUNC 0x02 - TYPE 0x02 - Light and Blind Control - Application Style 2

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|R1      |Rocker 1st action                                 |enum    |0 - Button AI                                                         |
|        |                                                  |        |1 - Button AO                                                         |
|        |                                                  |        |2 - Button BI                                                         |
|        |                                                  |        |3 - Button BO                                                         |
|EB      |Energy bow                                        |enum    |0 - released                                                          |
|        |                                                  |        |1 - pressed                                                           |
|R2      |Rocker 2nd action                                 |enum    |0 - Button AI                                                         |
|        |                                                  |        |1 - Button AO                                                         |
|        |                                                  |        |2 - Button BI                                                         |
|        |                                                  |        |3 - Button BO                                                         |
|SA      |2nd action                                        |enum    |0 - No 2nd action                                                     |
|        |                                                  |        |1 - 2nd action valid                                                  |
|T21     |T21                                               |status  |                                                                      |
|NU      |NU                                                |status  |                                                                      |



##### RORG 0xF6 - FUNC 0x05 - TYPE 0x01 - Liquid Leakage Sensor (mechanic harvester)

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|WAS     |Water Sensor                                      |enum    |0-16 - not specified                                                  |
|        |                                                  |        |17 - Water detected                                                   |
|        |                                                  |        |18-255 - not specified                                                |
|T21     |T21                                               |status  |                                                                      |
|NU      |NU                                                |status  |                                                                      |



##### RORG 0xF6 - FUNC 0x10 - TYPE 0x00 - Window Handle

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|WIN     |Window handle                                     |enum    |12 - Moved from up to vertical                                        |
|        |                                                  |        |13 - Moved from vertical to up                                        |
|        |                                                  |        |14 - Moved from down to vertical                                      |
|        |                                                  |        |15 - Moved from vertical to down                                      |
|T21     |T21                                               |status  |                                                                      |
|NU      |NU                                                |status  |                                                                      |



##### RORG 0xF6 - FUNC 0xFF - TYPE 0x00 - Eltako FSB 14 State

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SHS     |Shutter State                                     |enum    |1 - Opening Shutter                                                   |
|        |                                                  |        |2 - Closing Shutter                                                   |
|        |                                                  |        |112 - Endposition Up                                                  |
|        |                                                  |        |80 - Endposition Down                                                 |
|T21     |T21                                               |status  |                                                                      |
|NU      |NU                                                |status  |                                                                      |


##### RORG 0xF6 - FUNC 0xFF - TYPE 0x01 - Eltako FSM61 Leakage Sensor

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|WAS     |Water Sensor                                      |enum    |0 - Water no longer detected                                          |
|        |                                                  |        |1-79 - not specified                                                  |
|        |                                                  |        |80 - Water detected                                                   |
|        |                                                  |        |81-255 - not specified                                                |
|T21     |T21                                               |status  |                                                                      |
|NU      |NU                                                |status  |                                                                      |



### 1BS Telegram (0xD5)
##### RORG 0xD5 - FUNC 0x00 - TYPE 0x01 - Single Input Contact

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CO      |Contact                                           |enum    |0 - open                                                              |
|        |                                                  |        |1 - closed                                                            |



### 4BS Telegram (0xA5)
##### RORG 0xA5 - FUNC 0x02 - TYPE 0x01 - Temperature Sensor Range -40°C to 0°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -40.0-0.0 °C                                              |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x02 - Temperature Sensor Range -30°C to +10°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -30.0-10.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x03 - Temperature Sensor Range -20°C to +20°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -20.0-20.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x04 - Temperature Sensor Range -10°C to +30°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -10.0-30.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x05 - Temperature Sensor Range 0°C to +40°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 0.0-40.0 °C                                               |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x06 - Temperature Sensor Range +10°C to +50°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 10.0-50.0 °C                                              |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x07 - Temperature Sensor Range +20°C to +60°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 20.0-60.0 °C                                              |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x08 - Temperature Sensor Range +30°C to +70°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 30.0-70.0 °C                                              |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x09 - Temperature Sensor Range +40°C to +80°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 40.0-80.0 °C                                              |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x0A - Temperature Sensor Range +50°C to +90°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 50.0-90.0 °C                                              |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x0B - Temperature Sensor Range +60°C to +100°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 60.0-100.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x10 - Temperature Sensor Range -60°C to +20°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -60.0-20.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x11 - Temperature Sensor Range -50°C to +30°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -50.0-30.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x12 - Temperature Sensor Range -40°C to +40°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -40.0-40.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x13 - Temperature Sensor Range -30°C to +50°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -30.0-50.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x14 - Temperature Sensor Range -20°C to +60°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -20.0-60.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x15 - Temperature Sensor Range -10°C to +70°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -10.0-70.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x16 - Temperature Sensor Range 0°C to +80°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 0.0-80.0 °C                                               |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x17 - Temperature Sensor Range +10°C to +90°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 10.0-90.0 °C                                              |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x18 - Temperature Sensor Range +20°C to +100°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 20.0-100.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x19 - Temperature Sensor Range +30°C to +110°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 30.0-110.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x1A - Temperature Sensor Range +40°C to +120°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 40.0-120.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x1B - Temperature Sensor Range +50°C to +130°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 50.0-130.0 °C                                             |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x20 - 10 Bit Temperature Sensor Range -10°C to +41.2°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |1023.0-0.0 ↔ -10.0-41.2 °C                                            |


##### RORG 0xA5 - FUNC 0x02 - TYPE 0x30 - 10 Bit Temperature Sensor Range -40°C to +62.3°C

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |1023.0-0.0 ↔ -40.0-62.3 °C                                            |



##### RORG 0xA5 - FUNC 0x04 - TYPE 0x01 - Range 0°C to +40°C and 0% to 100%

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-250.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature (linear)                              |value   |0.0-250.0 ↔ 0.0-40.0 °C                                               |
|TSN     |Availability of the Temperature Sensor            |enum    |0 - not available                                                     |
|        |                                                  |        |1 - available                                                         |


##### RORG 0xA5 - FUNC 0x04 - TYPE 0x03 - Range -20°C  to +60°C 10bit-measurement  and 0% to 100%

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-255.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature (linear)                              |value   |0.0-1023.0 ↔ -20.0-60.0 °C                                            |
|TTP     |Telegram Type                                     |enum    |0 - Heartbeat                                                         |
|        |                                                  |        |1 - Event triggered                                                   |



##### RORG 0xA5 - FUNC 0x06 - TYPE 0x01 - Range 300lx to 60.000lx

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage (linear)                           |value   |0.0-255.0 ↔ 0.0-5.1 V                                                 |
|ILL2    |Illumination 2 (linear)                           |value   |0.0-255.0 ↔ 300.0-30000.0 lx                                          |
|ILL1    |Illumination 1 (linear)                           |value   |0.0-255.0 ↔ 600.0-60000.0 lx                                          |
|RS      |Range select                                      |enum    |0 - Range acc. to DB_1 (ILL1)                                         |
|        |                                                  |        |1 - Range acc. to DB_2 (ILL2)                                         |



##### RORG 0xA5 - FUNC 0x08 - TYPE 0x01 - Range 0lx to 510lx, 0°C to +51°C and Occupancy Button

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage (linear)                           |value   |0.0-255.0 ↔ 0.0-5.1 V                                                 |
|ILL     |Illumination (linear)                             |value   |0.0-255.0 ↔ 0.0-510.0 lx                                              |
|TMP     |Temperature (linear)                              |value   |0.0-255.0 ↔ 0.0-51.0 °C                                               |
|PIRS    |PIR Status                                        |enum    |0 - PIR on                                                            |
|        |                                                  |        |1 - PIR off                                                           |
|OCC     |Occupancy Button                                  |enum    |0 - Button pressed                                                    |
|        |                                                  |        |1 - Button released                                                   |



##### RORG 0xA5 - FUNC 0x10 - TYPE 0x03 - Temperature Sensor and Set Point

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Set Point (linear)                                |value   |0.0-255.0 ↔ 0.0-255.0 %                                               |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 0.0-40.0 °C                                               |
|LRNB    |LRN Bit                                           |enum    |0 - Teach-in telegram                                                 |
|        |                                                  |        |1 - Data telegram                                                     |


##### RORG 0xA5 - FUNC 0x10 - TYPE 0x12 - Temperature and Humidity Sensor and Set Point

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Set Point (linear)                                |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-250.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature (linear)                              |value   |0.0-250.0 ↔ 0.0-40.0 °C                                               |
|LRNB    |LRN Bit                                           |enum    |0 - Teach-in telegram                                                 |
|        |                                                  |        |1 - Data telegram                                                     |



##### RORG 0xA5 - FUNC 0x11 - TYPE 0x02 - Temperature Controller Output

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CVAR    |Actual value of controller                        |value   |0.0-255.0 ↔ 0.0-100.0 %                                               |
|FAN     |Actual value of fan                               |enum    |0 - State 0 Manual                                                    |
|        |                                                  |        |1 - State 1 Manual                                                    |
|        |                                                  |        |2 - State 2 Manual                                                    |
|        |                                                  |        |3 - State 3 Manual                                                    |
|        |                                                  |        |16 - State 0 Automatic                                                |
|        |                                                  |        |17 - State 1 Automatic                                                |
|        |                                                  |        |18 - State 2 Automatic                                                |
|        |                                                  |        |19 - State 3 Automatic                                                |
|        |                                                  |        |255 - Not Available                                                   |
|ASP     |Actual Setpoint                                   |value   |0.0-255.0 ↔ 0.0-51.2 C                                                |
|ALR     |Alarm                                             |enum    |0 - No alarm                                                          |
|        |                                                  |        |1 - Alarm                                                             |
|CTM     |Controller mode                                   |enum    |1 - Heating                                                           |
|        |                                                  |        |2 - Cooling                                                           |
|        |                                                  |        |3 - Off                                                               |
|CTS     |Controller state                                  |enum    |0 - Automatic                                                         |
|        |                                                  |        |1 - Override                                                          |
|ERH     |Energy hold-off                                   |enum    |0 - Normal                                                            |
|        |                                                  |        |1 - Energy hold-off / Dew point                                       |
|RO      |Room occupancy                                    |enum    |0 - Occupied                                                          |
|        |                                                  |        |1 - Unoccupied                                                        |
|        |                                                  |        |2 - StandBy                                                           |
|        |                                                  |        |3 - Frost                                                             |


##### RORG 0xA5 - FUNC 0x11 - TYPE 0x03 - Blind Status

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|BSP     |Blind/shutter pos.                                |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|AS      |Angle sign                                        |enum    |0 - Positive sign                                                     |
|        |                                                  |        |1 - Negative sign                                                     |
|AN      |Angle                                             |value   |0.0-90.0 ↔ 0.0-180.0 °                                                |
|PVF     |Position value flag                               |enum    |0 - No position value available                                       |
|        |                                                  |        |1 - Position value available                                          |
|AVF     |Angle value flag                                  |enum    |0 - No Angle value available                                          |
|        |                                                  |        |1 - No Angle value available                                          |
|ES      |Error state                                       |enum    |0 - No error present                                                  |
|        |                                                  |        |1 - End-positions are not configured                                  |
|        |                                                  |        |2 - Internal failure                                                  |
|        |                                                  |        |3 - Not used                                                          |
|EP      |End-position                                      |enum    |0 - No End-position available                                         |
|        |                                                  |        |1 - No End-position reached                                           |
|        |                                                  |        |2 - Blind fully open                                                  |
|        |                                                  |        |3 - Blind fully closed                                                |
|ST      |Status                                            |enum    |0 - No Status available                                               |
|        |                                                  |        |1 - Blind is stopped                                                  |
|        |                                                  |        |2 - Blind opens                                                       |
|        |                                                  |        |3 - Blind closes                                                      |
|SM      |Service Mode                                      |enum    |0 - Normal mode                                                       |
|        |                                                  |        |1 - Service mode is activated                                         |
|MOTP    |Mode of the position                              |enum    |0 - Normal mode                                                       |
|        |                                                  |        |1 - Inverse mode                                                      |



##### RORG 0xA5 - FUNC 0x20 - TYPE 0x01 - Battery Powered Actuator (BI-DIR)

###### direction: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CV      |Current Value                                     |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|SO      |Service On                                        |enum    |0 - off                                                               |
|        |                                                  |        |1 - on                                                                |
|ENIE    |Energy input enabled                              |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|ES      |Energy storage sufficiently charged               |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|BCAP    |Battery capacity; change battery next days        |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|CCO     |Contact, cover open                               |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|FTS     |Failure Temperature sensor, out of range          |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|DWO     |Detection, window open                            |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|ACO     |Actuator obstructed                               |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|TMP     |Temperature (linear)                              |value   |0.0-255.0 ↔ 0.0-40.0 °C                                               |

###### direction: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Valve Position                                    |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature from RCU                              |value   |0.0-255.0 ↔ 0.0-40.0 °C                                               |
|RIN     |Run init sequence                                 |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|LFS     |Lift set                                          |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|VO      |Valve open / maintenance                          |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|VC      |Valve closed                                      |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|SB      |Summer bit, Reduction of energy consumption       |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|SPS     |Set point selection                               |enum    |0 - Valve position                                                    |
|        |                                                  |        |1 - Temperature set point                                             |
|SPN     |Set point inverse                                 |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|RCU     |Select function                                   |enum    |0 - RCU                                                               |
|        |                                                  |        |1 - service on                                                        |


##### RORG 0xA5 - FUNC 0x20 - TYPE 0x06 - Harvesting-powered actuator with local temperature offset control (BI-DIR)

###### direction: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CV      |Current Value                                     |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|LOM     |Local Offset Mode                                 |enum    |0 - LO is relative                                                    |
|        |                                                  |        |1 - LO is absolute                                                    |
|LO      |Local Offset                                      |value   |0.0-80.0 ↔ 0.0-40.0 °C                                                |
|TMP     |Temperature                                       |value   |0.0-80.0 ↔ 0.0-160.0 °C                                               |
|TSL     |Temperature Selection                             |enum    |0 - Ambient sensor temp                                               |
|        |                                                  |        |1 - Feed sensor temperature                                           |
|ENIE    |Energy input enabled                              |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|ES      |Energy storage sufficiently charged               |enum    |0 - Low, almost discharged                                            |
|        |                                                  |        |1 - Sufficiently charged                                              |
|DWO     |Window open detection                             |enum    |0 - No open window detected                                           |
|        |                                                  |        |1 - Open window detected                                              |
|RCE     |Radio Com Error                                   |enum    |0 - Radio communication is stable                                     |
|        |                                                  |        |1 - Six or more consecutive radio communication errors have occurred  |
|RSS     |Radio Signal Strength                             |enum    |0 - Radio signal is strong                                            |
|        |                                                  |        |1 - Radio signal is weak                                              |
|ACO     |Actuator obstructed                               |enum    |0 - Actuator working correctly                                        |
|        |                                                  |        |1 - Actuator is blocked                                               |

###### direction: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Valve Position                                    |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature from RCU                              |value   |0.0-160.0 ↔ 0.0-40.0 °C                                               |
|REF     |Execute reference-run                             |enum    |0 - Normal operation                                                  |
|        |                                                  |        |1 - Reference-run and Maintenance Interval                            |
|RFC     |RF Communication interval                         |enum    |0 - AUTO                                                              |
|        |                                                  |        |1 - 2 minutes                                                         |
|        |                                                  |        |2 - 5 minutes                                                         |
|        |                                                  |        |3 - 10 minutes                                                        |
|        |                                                  |        |4 - 20 minutes                                                        |
|        |                                                  |        |5 - 30 minutes                                                        |
|        |                                                  |        |6 - 60 minutes                                                        |
|        |                                                  |        |7 - 120 minutes                                                       |
|SB      |Summer bit, Reduction of energy consumption       |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|SPS     |Set point selection                               |enum    |0 - Valve position mode                                               |
|        |                                                  |        |1 - Temperature set point                                             |
|TSL     |Temperature requested from the actuator           |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|SBY     |Standby                                           |enum    |0 - Normal operation                                                  |
|        |                                                  |        |1 - Standby                                                           |



##### RORG 0xA5 - FUNC 0x12 - TYPE 0x01 - Electricity

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MR      |current value in W or cumulative value in kWh     |value   |0.0-16777215.0 ↔ 0.0-16777215.0                                       |
|TI      |Tariff info                                       |value   |0.0-15.0 ↔ 0.0-15.0                                                   |
|DT      |Current value or cumulative value                 |enum    |0 - kWh                                                               |
|        |                                                  |        |1 - W                                                                 |
|DIV     |Divisor for value                                 |enum    |0 - x/1                                                               |
|        |                                                  |        |1 - x/10                                                              |
|        |                                                  |        |2 - x/100                                                             |
|        |                                                  |        |3 - x/1000                                                            |



##### RORG 0xA5 - FUNC 3F - TYPE 0x7F - Universal

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MSGID   |Message ID                                        |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|RSSI    |Received Signal Strength Indicator                |value   |0.0-255.0 ↔ 0.0-255.0                                                 |



##### RORG 0xA5 - FUNC 0x30 - TYPE 0x03 - Digital Inputs, Wake and Temperature

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 0.0-40.0 °C                                               |
|WA0     |Value of wake signal                              |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |
|DI3     |Digital Input 3                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |
|DI2     |Digital Input 2                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |
|DI1     |Digital Input 1                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |
|DI0     |Digital Input 0                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |



##### RORG 0xA5 - FUNC 0x38 - TYPE 0x08 - Gateway

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command ID                                        |enum    |0-13 - Command ID {value}                                             |
|TIM     |Time                                              |value   |1.0-65535.0 ↔ 0.1-6553.5 s                                            |
|LRNB    |LRN Bit                                           |enum    |0 - Teach-in Telegram                                                 |
|        |                                                  |        |1 - Data Telegram                                                     |
|LCK     |LOCK/UNLOCK                                       |enum    |0 - Unlock                                                            |
|        |                                                  |        |1 - Lock                                                              |
|DEL     |Delay or Duration                                 |enum    |0 - Duration                                                          |
|        |                                                  |        |1 - Delay                                                             |
|SW      |Switching command                                 |enum    |0 - Off                                                               |
|        |                                                  |        |1 - On                                                                |

###### command: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command ID                                        |enum    |0-13 - Command ID {value}                                             |
|EDIM    |Dimming value                                     |value   |0.0-255.0 ↔ 0.0-255.0 %                                               |
|RMP     |Ramping time                                      |value   |0.0-255.0 ↔ 0.0-255.0 s                                               |
|LRNB    |LRN Bit                                           |enum    |0 - Teach-in Telegram                                                 |
|        |                                                  |        |1 - Data Telegram                                                     |
|EDIMR   |Dimming Range                                     |enum    |0 - Absolute value                                                    |
|        |                                                  |        |1 - Relative value                                                    |
|STR     |Store final value                                 |enum    |0 - No                                                                |
|        |                                                  |        |1 - Yes                                                               |
|SW      |Switching command                                 |enum    |0 - Off                                                               |
|        |                                                  |        |1 - On                                                                |



##### RORG 0xA5 - FUNC 0xFF - TYPE 0x00 - Eltako Blind Feedback

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MSB     |Shutter Run Time MSB                              |value   |0.0-255.0 ↔ 0.0-255.0 ms                                              |
|LSB     |Shutter Run Time LSB                              |value   |0.0-255.0 ↔ 0.0-255.0 ms                                              |
|BSP     |Blind/shutter pos.                                |enum    |2 - Closing                                                           |
|        |                                                  |        |1 - Opening                                                           |
|        |                                                  |        |2-255 - Unspecified                                                   |
|BBL     |Blind blocked status                              |enum    |0-9 - Unspecified                                                     |
|        |                                                  |        |10 - Not blocked                                                      |
|        |                                                  |        |11-13 - Unspecified                                                   |
|        |                                                  |        |14 - Blocked                                                          |
|        |                                                  |        |15-255 - Unspecified                                                  |


##### RORG 0xA5 - FUNC 0xFF - TYPE 0x01 - Thermokon SR65 3AI

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|DI3     |Data Input 3 linear                               |value   |0.0-255.0 ↔ 0.0-10.0 V                                                |
|DI2     |Data Input 2 linear                               |value   |0.0-255.0 ↔ 0.0-10.0 V                                                |
|DI1     |Data Input 1 linear                               |value   |0.0-255.0 ↔ 0.0-10.0 V                                                |



### VLD Telegram (0xD2)
##### RORG 0xD2 - FUNC 0x01 - TYPE 0x01 - Electronic switch with Local Control

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PF      |Power Failure                                     |enum    |0 - Power Failure Detection disabled/not supported                    |
|        |                                                  |        |1 - Power Failure Detection enabled                                   |
|PFD     |Power Failure Detection                           |enum    |0 - Power Failure Detection not detected/not supported/disabled       |
|        |                                                  |        |1 - Power Failure Detection Detected                                  |
|CMD     |Command indentifier                               |enum    |0-13 - Command ID {value}                                             |
|OC      |Over current switch off                           |enum    |0 - Over current switch off: ready / not supported                    |
|        |                                                  |        |1 - Over current switch off: executed                                 |
|EL      |Error level                                       |enum    |0 - Error level 0: hardware OK                                        |
|        |                                                  |        |1 - Error level 1: hardware warning                                   |
|        |                                                  |        |2 - Error level 2: hardware failure                                   |
|        |                                                  |        |3 - Error level not supported                                         |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|LC      |Local control                                     |enum    |0 - Local control disabled / not supported                            |
|        |                                                  |        |1 - Local control enabled                                             |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command indentifier                               |enum    |0-13 - Command ID {value}                                             |
|DV      |Dim value                                         |enum    |0 - Switch to new output value                                        |
|        |                                                  |        |1 - Dim to new output level - dim timer 1                             |
|        |                                                  |        |2 - Dim to new output level - dim timer 2                             |
|        |                                                  |        |3 - Dim to new output level - dim timer 3                             |
|        |                                                  |        |4 - Stop dimming                                                      |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |



### General Profile Telegram (0xB2)
##### RORG 0xB2 - FUNC 0x00 - TYPE 0x01 - Afriso Room Controller 2 Kanal

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|C1      |Channel 1 status                                  |enum    |0 - off                                                               |
|        |                                                  |        |1 - on                                                                |
|C2      |Channel 2 status                                  |enum    |0 - off                                                               |
|        |                                                  |        |1 - on                                                                |
|TY      |Type                                              |enum    |0 - receive                                                           |
|        |                                                  |        |1 - heartbeat                                                         |
|        |                                                  |        |2 - change                                                            |
|E1      |Channel 1 emergency status                        |enum    |0 - normal mode                                                       |
|        |                                                  |        |1 - emergency mode                                                    |
|E2      |Channel 2 emergency status                        |enum    |0 - normal mode                                                       |
|        |                                                  |        |1 - emergency mode                                                    |


##### RORG 0xB2 - FUNC 0x00 - TYPE 0x02 - Afriso Room Controller 6 Kanal

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|C1      |Channel 1 status                                  |enum    |0 - off                                                               |
|        |                                                  |        |1 - on                                                                |
|C2      |Channel 2 status                                  |enum    |0 - off                                                               |
|        |                                                  |        |1 - on                                                                |
|C3      |Channel 3 status                                  |enum    |0 - off                                                               |
|        |                                                  |        |1 - on                                                                |
|C4      |Channel 4 status                                  |enum    |0 - off                                                               |
|        |                                                  |        |1 - on                                                                |
|C5      |Channel 5 status                                  |enum    |0 - off                                                               |
|        |                                                  |        |1 - on                                                                |
|C6      |Channel 6 status                                  |enum    |0 - off                                                               |
|        |                                                  |        |1 - on                                                                |
|TY      |Type                                              |enum    |0 - receive                                                           |
|        |                                                  |        |1 - heartbeat                                                         |
|        |                                                  |        |2 - change                                                            |
|E1      |Channel 1 emergency status                        |enum    |0 - normal mode                                                       |
|        |                                                  |        |1 - emergency mode                                                    |
|E2      |Channel 2 emergency status                        |enum    |0 - normal mode                                                       |
|        |                                                  |        |1 - emergency mode                                                    |
|E3      |Channel 3 emergency status                        |enum    |0 - normal mode                                                       |
|        |                                                  |        |1 - emergency mode                                                    |
|E4      |Channel 4 emergency status                        |enum    |0 - normal mode                                                       |
|        |                                                  |        |1 - emergency mode                                                    |
|E5      |Channel 5 emergency status                        |enum    |0 - normal mode                                                       |
|        |                                                  |        |1 - emergency mode                                                    |
|E6      |Channel 6 emergency status                        |enum    |0 - normal mode                                                       |
|        |                                                  |        |1 - emergency mode                                                    |



