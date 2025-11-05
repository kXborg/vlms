```markdown
# IEC 61439: Alternate Design Verification Methods

**N. S. Vijayanarayanan**, Kushal Parwal and Ravindra Kadam  
Larsen & Toubro Ltd.

---

## Abstract

Design verification for low-voltage power switchgear and control gear assemblies is intended to verify compliance of the design of an assembly or assembly system with the requirements of IEC61439 series of standards. There are 3 methods of verification. 1. Verification testing 2. Verification comparison with a tested reference design 3. Verification assessment by calculations and design rules including use of appropriate safety margins. The normally preferred verification method is verification by testing. However, verification by assessment and verification by comparison are also alternate verification methods provided by IEC 61439, which are still unexplored. This is in spite of the fact that IEC 61439 states: “**all the permitted means of design verification which includes comparison and assessment are equivalent in terms of performance achieved.**” Here, we shall elaborate on the verification assessment and verification comparison methods for Low voltage switchgear and control gear assemblies.

**Keywords:** Assessment, Assembly, Comparison, Low Voltage Switchgear, Testing, Verification

---

## 1. Verification Assessment

Design verification by strict design rules or calculations applied to a sample of an assembly or to parts of assemblies to show that the design meets the requirements of the relevant assembly standard.

When there is more than one method for the same verification, they are considered equivalent and the selection of the appropriate method is the responsibility of the original manufacturer.

However, all the tests are not possible with assessment. Annex D of IEC 61439-1 mentions the verification options available and applicable against each tests.

Let’s discuss about the tests which are possible by assessment.

### 1.1 Glow Wire Test

Verification of resistance of insulating materials to abnormal heat and fire due to internal electric effects:

- 960 °C for parts necessary to retain current-carrying parts in position.
- 850 °C for enclosures intended for mounting in hollow walls.

---

## 2. Verification Comparison

### 2.1 Temperature Rise

Standard defines how the rated currents of variants can be verified by derivation from similar arrangements verified by test.

1) Temperature-rise tests on the circuit(s) carried out at 50 Hz are applicable to 60 Hz for rated currents up to and including 800A. In the absence of tests at 60 Hz for currents above 800A, the rated current at 60 Hz shall be reduced to 95% of that at 50Hz. alternatively, where the maximum temperature rise at 50 Hz does not exceed 90% of the permissible value, then derating for 60 Hz is not required. Tests carried out at a particular frequency are applicable at the same current rating to lower frequencies including d.c.

2) Assemblies verified by derivation from a similar tested arrangement shall comply with the following:

a) The functional units shall belong to the same group as the functional unit selected for test

b) The same type of construction as used for the test

c) The same or increased overall dimensions as used for the test

d) The same or increased cooling conditions as used for the test (forced or natural convection, same or larger ventilation openings)

e) The same or reduced internal separations as used for the test (if any)

f) The same or reduced power losses in the same section as used for the test

3) Thermal tests performed on 3-phase, 3-wire assemblies are considered as representing 3-phase, 4-wire and single-phase, 2-wire or 3-wire assemblies, provided that the neutral conductor is sized equal to or greater than the phase conductors arranged in the same manner.

4) Busbars: Ratings established for aluminum busbars are valid for copper Busbars with the same cross sectional dimensions and configuration. However, ratings established for copper busbars shall not be used to establish ratings of aluminum busbars.

5) If additionally, a similar cross-section than the one to be derived has been tested, which also fulfils the conditions, then the rating of the intermediate variants may be established by interpolation.

6) The standard allows, in clearly defined circumstances, for the derivation of rating of a double lamination busbar has been established by test, it is acceptable to assign a rating equal to 50% of the tested arrangement to a busbar comprising a single lamination with the same width and thickness as the tested laminations, when all other considerations are the same.

**Functional units - Device substitution**

A device may be substituted with a similar device from another series to that used in the original verification, provided that the power loss and terminal temperature rise of the device, t=when tested in accordance with its product standard, is the same or lower. In addition, the physical arrangement within the functional unit and the rating of the functional unit shall be maintained.

### 2.2 Short Circuit

Short circuit verification by comparison can be done in two ways

a) Using a check list:

| Item No. | Requirements to be considered |
|----------|-------------------------------|
| 1        | Is the short-circuit withstand rating of each circuit of the assembly to be assessed, less than or equal to, that of the reference design? |
| 2        | Is the cross-sectional dimensions of the busbars and connections of each circuit of the assembly to be assessed, greater than or equal to, those of the reference design? |
| 3        | Is the center line spacing of the busbars and connections of each circuit of the assembly to be assessed, greater than or equal to, those of the reference design? |
| 4        | Are the busbar supports of each circuit of the assembly to be assessed of the same type, shape and material and have, the same or smaller center line spacing, along the length of the busbar as the reference design? And is the mounting structure for the busbar supports of the same design and mechanical strength? |

---

## 1.2 Resistance to Ultra-violet (UV) Radiation

This test applies only to enclosures, external parts of assemblies intended to be installed outdoors, and which are constructed of insulating materials or metals that are entirely coated by synthetic material. Representative samples of such parts shall be subjected to the following test:

**Assessment:** This test need not be carried out if the original manufacturer can provide data from the material supplier to demonstrate that material of the same type and thickness or thinner complies with this requirement.

---

## 1.3 Degree of Protection

**Testing:** The degree of protection shall be verified in accordance with IEC 60529; the test may be carried out on one representative equipped assembly in a condition stated by the original manufacturer.

**Assessment:** Where an empty enclosure in accordance with IEC 62208 is used, a verification assessment shall be performed to ensure that any external modification that has been carried out does not result in a deterioration of the degree of protection; In this case, no further testing is required.

---

## 1.4 Impulse withstand Voltage

**Testing:** The 1, 2/50 µs impulse voltage shall be applied to the assembly five times for each polarity at intervals of 1s minimum.

---

## 1.5 Temperature Rise

**Assessment:** Two calculation methods are provided by standard for specific ratings. Both determine the approximate air temperature rise inside the enclosure, which is caused by the power losses of all circuits, and compare this temperature with the limits for the installed equipment.

### Method 1) Single compartment assembly with rated current not exceeding 630 A

Verification of the temperature rise of a single compartment ASSEMBLY with the total supply current not exceeding 630 A and for rated frequencies up to and including 60 Hz may be made by calculation if all the following conditions are fulfilled:

- The power loss data for all built-in components is available from the component manufacturer;
- There is an approximately even distribution of power losses inside the enclosure;
- The rated current of the circuits of the ASSEMBLY to be verified shall not exceed 80% of the rated convectional free air thermal current (Ith) If any, or the rated current (In) of the switching devices and electrical components included in the circuit. Circuit protection devices shall be selected to ensure adequate protection to outgoing circuits, e.g. thermal motor protection devices at the calculated temperature in the ASSEMBLY;
- a) The mechanical parts and the installed equipment are so arranged that air circulation is not significantly impeded.
- b) Conductors carrying currents in excess of 200A, and the adjacent structural parts are so arranged that eddy-current and hysteresis losses are minimized.
- c) All conductors shall have a minimum cross-sectional area based on 125% of the permitted current rating of the associated circuit.
- d) The temperature rise depending on the power loss installed in the enclosure for the different installation methods.

The effective power losses of all circuits including interconnecting conductors shall be calculated based on

---

## 1.6 EMC

**Assessment:** No EMC immunity or emission tests are required on final ASSEMBLIES if the following conditions are fulfilled:

a) The incorporated devices and components are in compliance with the requirements for EMC for the stated environment (see J.9.4.1) as required by the relevant product or generic EMC standard.

b) The internal installation and wiring is carried out in accordance with the devices and components manufacturer’s instructions (arrangement with

---

## Table 1 – Minimum clearances in air *(8.3.2)*

| Rated Impulse withstand voltage U_imp kV | Minimum clearance mm |
|------------------------------------------|----------------------|
| ≤ 2,5                                    | 1,5                  |
| 4,0                                      | 3,0                  |
| 6,0                                      | 5,5                  |
| 8,0                                      | 8,0                  |
| 12,0                                     | 14,0                 |

*Based on inhomogeneous field conditions and pollution degree 3.*

---

## 1.1 Glow Wire Test (continued)

Verification of resistance of insulating materials to abnormal heat and fire due to internal electric effects:

- 960 °C for parts necessary to retain current-carrying parts in position.
- 850 °C for enclosures intended for mounting in hollow walls.

---

## 1.2 Resistance to Ultra-violet (UV) Radiation (continued)

This test applies only to enclosures, external parts of assemblies intended to be installed outdoors, and which are constructed of insulating materials or metals that are entirely coated by synthetic material. Representative samples of such parts shall be subjected to the following test:

**Assessment:** This test need not be carried out if the original manufacturer can provide data from the material supplier to demonstrate that material of the same type and thickness or thinner complies with this requirement.

---

## 1.3 Degree of Protection (continued)

**Testing:** The degree of protection shall be verified in accordance with IEC 60529; the test may be carried out on one representative equipped assembly in a condition stated by the original manufacturer.

**Assessment:** Where an empty enclosure in accordance with IEC 62208 is used, a verification assessment shall be performed to ensure that any external modification that has been carried out does not result in a deterioration of the degree of protection; In this case, no further testing is required.

---

## 1.4 Impulse withstand Voltage (continued)

**Testing:** The 1, 2/50 µs impulse voltage shall be applied to the assembly five times for each polarity at intervals of 1s minimum.

---

## 1.5 Temperature Rise (continued)

**Assessment:** Two calculation methods are provided by standard for specific ratings. Both determine the approximate air temperature rise inside the enclosure, which is caused by the power losses of all circuits, and compare this temperature with the limits for the installed equipment.

### Method 1) Single compartment assembly with rated current not exceeding 630 A

Verification of the temperature rise of a single compartment ASSEMBLY with the total supply current not exceeding 630 A and for rated frequencies up to and including 60 Hz may be made by calculation if all the following conditions are fulfilled:

- The power loss data for all built-in components is available from the component manufacturer;
- There is an approximately even distribution of power losses inside the enclosure;
- The rated current of the circuits of the ASSEMBLY to be verified shall not exceed 80% of the rated convectional free air thermal current (Ith) If any, or the rated current (In) of the switching devices and electrical components included in the circuit. Circuit protection devices shall be selected to ensure adequate protection to outgoing circuits, e.g. thermal motor protection devices at the calculated temperature in the ASSEMBLY;
- a) The mechanical parts and the installed equipment are so arranged that air circulation is not significantly impeded.
- b) Conductors carrying currents in excess of 200A, and the adjacent structural parts are so arranged that eddy-current and hysteresis losses are minimized.
- c) All conductors shall have a minimum cross-sectional area based on 125% of the permitted current rating of the associated circuit.
- d) The temperature rise depending on the power loss installed in the enclosure for the different installation methods.

The effective power losses of all circuits including interconnecting conductors shall be calculated based on

---

## 1.6 EMC (continued)

**Assessment:** No EMC immunity or emission tests are required on final ASSEMBLIES if the following conditions are fulfilled:

a) The incorporated devices and components are in compliance with the requirements for EMC for the stated environment (see J.9.4.1) as required by the relevant product or generic EMC standard.

b) The internal installation and wiring is carried out in accordance with the devices and components manufacturer’s instructions (arrangement with

---

## Table 1 – Minimum clearances in air *(8.3.2)* (continued)

| Rated Impulse withstand voltage U_imp kV | Minimum clearance mm |
|------------------------------------------|----------------------|
| ≤ 2,5                                    | 1,5                  |
| 4,0                                      | 3,0                  |
| 6,0                                      | 5,5                  |
| 8,0                                      | 8,0                  |
| 12,0                                     | 14,0                 |

*Based on inhomogeneous field conditions and pollution degree 3.*

---

## 1.1 Glow Wire Test (continued)

Verification of resistance of insulating materials to abnormal heat and fire due to internal electric effects:

- 960 °C for parts necessary to retain current-carrying parts in position.
- 850 °C for enclosures intended for mounting in hollow walls.

---

## 1.2 Resistance to Ultra-violet (UV) Radiation (continued)

This test applies only to enclosures, external parts of assemblies intended to be installed outdoors, and which are constructed of insulating materials or metals that are entirely coated by synthetic material. Representative samples of such parts shall be subjected to the following test:

**Assessment:** This test need not be carried out if the original manufacturer can provide data from the material supplier to demonstrate that material of the same type and thickness or thinner complies with this requirement.

---

## 1.3 Degree of Protection (continued)

**Testing:** The degree of protection shall be verified in accordance with IEC 60529; the test may be carried out on one representative equipped assembly in a condition stated by the original manufacturer.

**Assessment:** Where an empty enclosure in accordance with IEC 62208 is used, a verification assessment shall be performed to ensure that any external modification that has been carried out does not result in a deterioration of the degree of protection; In this case, no further testing is required.

---

## 1.4 Impulse withstand Voltage (continued)

**Testing:** The 1, 2/50 µs impulse voltage shall be applied to the assembly five times for each polarity at intervals of 1s minimum.

---

## 1.5 Temperature Rise (continued)

**Assessment:** Two calculation methods are provided by standard for specific ratings. Both determine the approximate air temperature rise inside the enclosure, which is caused by the power losses of all circuits, and compare this temperature with the limits for the installed equipment.

### Method 1) Single compartment assembly with rated current not exceeding 630 A

Verification of the temperature rise of a single compartment ASSEMBLY with the total supply current not exceeding 630 A and for rated frequencies up to and including 60 Hz may be made by calculation if all the following conditions are fulfilled:

- The power loss data for all built-in components is available from the component manufacturer;
- There is an approximately even distribution of power losses inside the enclosure;
- The rated current of the circuits of the ASSEMBLY to be verified shall not exceed 80% of the rated convectional free air thermal current (Ith) If any, or the rated current (In) of the switching devices and electrical components included in the circuit. Circuit protection devices shall be selected to ensure adequate protection to outgoing circuits, e.g. thermal motor protection devices at the calculated temperature in the ASSEMBLY;
- a) The mechanical parts and the installed equipment are so arranged that air circulation is not significantly impeded.
- b) Conductors carrying currents in excess of 200A, and the adjacent structural parts are so arranged that eddy-current and hysteresis losses are minimized.
- c) All conductors shall have a minimum cross-sectional area based on 125% of the permitted current rating of the associated circuit.
- d) The temperature rise depending on the power loss installed in the enclosure for the different installation methods.

The effective power losses of all circuits including interconnecting conductors shall be calculated based on

---

## 1.6 EMC (continued)

**Assessment:** No EMC immunity or emission tests are required on final ASSEMBLIES if the following conditions are fulfilled:

a) The incorporated devices and components are in compliance with the requirements for EMC for the stated environment (see J.9.4.1) as required by the relevant product or generic EMC standard.

b) The internal installation and wiring is carried out in accordance with the devices and components manufacturer’s instructions (arrangement with

---

## Table 1 – Minimum clearances in air *(8.3.2)* (continued)

| Rated Impulse withstand voltage U_imp kV | Minimum clearance mm |
|------------------------------------------|----------------------|
| ≤ 2,5                                    | 1,5                  |
| 4,0                                      | 3,0                  |
| 6,0                                      | 5,5                  |
| 8,0                                      | 8,0                  |
| 12,0                                     | 14,0                 |

*Based on inhomogeneous field conditions and pollution degree 3.*

---

## 1.1 Glow Wire Test (continued)

Verification of resistance of insulating materials to abnormal heat and fire due to internal electric effects:

- 960 °C for parts necessary to retain current-carrying parts in position.
- 850 °C for enclosures intended for mounting in hollow walls.

---

## 1.2 Resistance to Ultra-violet (UV) Radiation (continued)

This test applies only to enclosures, external parts of assemblies intended to be installed outdoors, and which are constructed of insulating materials or metals that are entirely coated by synthetic material. Representative samples of such parts shall be subjected to the following test:

**Assessment:** This test need not be carried out if the original manufacturer can provide data from the material supplier to demonstrate that material of the same type and thickness or thinner complies with this requirement.

---

## 1.3 Degree of Protection (continued)

**Testing:** The degree of protection shall be verified in accordance with IEC 60529; the test may be carried out on one representative equipped assembly in a condition stated by the original manufacturer.

**Assessment:** Where an empty enclosure in accordance with IEC 62208 is used, a verification assessment shall be performed to ensure that any external modification that has been carried out does not result in a deterioration of the degree of protection; In this case, no further testing is required.

---

## 1.4 Impulse withstand Voltage (continued)

**Testing:** The 1, 2/50 µs impulse voltage shall be applied to the assembly five times for each polarity at intervals of 1s minimum.

---

## 1.5 Temperature Rise (continued)

**Assessment:** Two calculation methods are provided by standard for specific ratings. Both determine the approximate air temperature rise inside the enclosure, which is caused by the power losses of all circuits, and compare this temperature with the limits for the installed equipment.

### Method 1) Single compartment assembly with rated current not exceeding 630 A

Verification of the temperature rise of a single compartment ASSEMBLY with the total supply current not exceeding 630 A and for rated frequencies up to and including 60 Hz may be made by calculation if all the following conditions are fulfilled:

- The power loss data for all built-in components is available from the component manufacturer;
- There is an approximately even distribution of power losses inside the enclosure;
- The rated current of the circuits of the ASSEMBLY to be verified shall not exceed 80% of the rated convectional free air thermal current (Ith) If any, or the rated current (In) of the switching devices and electrical components included in the circuit. Circuit protection devices shall be selected to ensure adequate protection to outgoing circuits, e.g. thermal motor protection devices at the calculated temperature in the ASSEMBLY;
- a) The mechanical parts and the installed equipment are so arranged that air circulation is not significantly impeded.
- b) Conductors carrying currents in excess of 200A, and the adjacent structural parts are so arranged that eddy-current and hysteresis losses are minimized.
- c) All conductors shall have a minimum cross-sectional area based on 125% of the permitted current rating of the associated circuit.
- d) The temperature rise depending on the power loss installed in the enclosure for the different installation methods.

The effective power losses of all circuits including interconnecting conductors shall be calculated based on

---

## 1.6 EMC (continued)

**Assessment:** No EMC immunity or emission tests are required on final ASSEMBLIES if the following conditions are fulfilled:

a) The incorporated devices and components are in compliance with the requirements for EMC for the stated environment (see J.9.4.1) as required by the relevant product or generic EMC standard.

b) The internal installation and wiring is carried out in accordance with the devices and components manufacturer’s instructions (arrangement with

---

## Table 1 – Minimum clearances in air *(8.3.2)* (continued)

| Rated Impulse withstand voltage U_imp kV | Minimum clearance mm |
|------------------------------------------|----------------------|
| ≤ 2,5                                    | 1,5                  |
| 4,0                                      | 3,0                  |
| 6,0                                      | 5,5                  |
| 8,0                                      | 8,0                  |
| 12,0                                     | 14,0                 |

*Based on inhomogeneous field conditions and pollution degree 3.*

---

## 1.1 Glow Wire Test (continued)

Verification of resistance of insulating materials to abnormal heat and fire due to internal electric effects:

- 960 °C for parts necessary to retain current-carrying parts in position.
- 850 °C for enclosures intended for mounting in hollow walls.

---

## 1.2 Resistance to Ultra-violet (UV