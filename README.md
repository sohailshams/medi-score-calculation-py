# Medi Score Calculation

- [Github Repo](https://github.com/sohailshams/medi-score-calculation-py)

## Description

The Medi Score Calculation is a simple function to calculate score of a patient based on patient's physiological measurements. These measurements are taken against following observations;

1. Air / Oxygen saturation
1. Alert / level of consciousness or
1. Respiration rate
1. SpO2 (%)
1. Temperature

### Bonus

1. Raising a flag if score raised by 2 in 24 hours

## Developemt Process

I developed this function in python and also setup python [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html) for testing purpose to make this function robust. My approach was to create a function that take observations as dictionary and then calculate the score of each individual observation object property. So I developed following functions in connection to the main **medi_score_calculation** function;

1. get_air_or_oxygen_score
1. get_consciousness_score
1. get_respiration_range_score
1. get_spo2_score
1. get_temperature_score

Finally I added the scores to get the total of all and returned an error message if any of the above functions returned None.

## Testing

I followed test driven development approach and wrote comprehensive test scenarios for all functions. For testing **_get_air_or_oxygen_score_**, **_get_consciousness_score_**, **_get_respiration_range_score_**, **_get_spo2_score_** and **_get_temperature_score_** I wrote tests for the individual function and also tested the main **medi_score_calculation**. This function takes **_observation_dict_** dictionary as a parameter with different values and correct value is vaified as per following table. Please note ranges are inclusive.

|           Property            | Score 3 | Score 2 |  Score 1  |        Score 0        |     Score 1     |     Score 2     |    Score 3    |
| :---------------------------: | :-----: | :-----: | :-------: | :-------------------: | :-------------: | :-------------: | :-----------: |
|        Air or oxygen?         |         | Oxygen  |           |          Air          |                 |                 |               |
|         Consciousness         |         |         |           |         Alert         |                 |                 |     CVPU      |
| Respiration rate (per minute) |   ≤8    |         |   9–11    |         12–20         |                 |      21–24      |               |
|           SpO2 (%)            |   ≤83   |  84–85  |   86–87   | 88–92 (or ≥93 on air) | 93–94 on oxygen | 95–96 on oxygen | ≥97 on oxygen |
|       Temperature (°C)        |  ≤35.0  |         | 35.1–36.0 |       36.1–38.0       |    38.1–39.0    |      ≥39.1      |               |

**medi_score_calculation** function is tested with following input observations;

#### Patient 1 - No alert

```
{
    "air_or_oxygen": AirOrOxygen.AIR.value,
    "consciousness": Consciousness.ALERT.value,
    "respiration": 15,
    "spo2": 95,
    "temperature": 37.1
};
```

**Total Medi Score = 0**

#### Patient 2 - Flag an alert

```
{
    "air_or_oxygen": AirOrOxygen.OXYGEN.value,
    "consciousness": Consciousness.ALERT.value,
    "respiration": 17,
    "spo2": 95,
    "temperature": 37.1
};
```

**Total Medi Score = 4**

#### Patient 3 - Flag an alert

```
{
    "air_or_oxygen": AirOrOxygen.OXYGEN.value,
    "consciousness": Consciousness.CVPU.value,
    "respiration": 23,
    "spo2": 88,
    "temperature": 38.5
};
```

**_Please note there is a typo in patient 3 observations in the project README as CVPU score is 3 not 1._**
**Total Medi Score = 8**

#### Patient 4 - Flag an alert

```
{
    "air_or_oxygen": AirOrOxygen.OXYGEN.value,
    "consciousness": Consciousness.CVPU.value,
    "respiration": 25,
    "spo2": 97,
    "temperature": 35
};
```

**Total Medi Score = 14**

## Bonus Flagging an Alert

To develop this function I created mock data which is an array and contains dictionaries of medi score with time and id. I also assumed that this mock data is associdated to the current patient and this array contains data for only last 24 hours. This function is taking medi score and the test data list as parameters and compare the total medi score against the previous readings taken within 24 hours and if the score is raised by more than 2 in the current reading, the function will return true and a message will be rendered.

## Bonus CBG

Since I have completed this task in JavaScript and did not had enough time so I left it. But I will follow the same approach, by have a is_fasting a bolean in observation dictionaly as being False by default and use the the corresponding CBG ranges. But if patient is fasting then I will use the fasting CBG ranges. To accomplish this I will have a check box to get user input and will change is_fasting value to True if user tich the check box.

#### If/Elif/Else Statement- Match case

I mainly used if/elif/else statement but also use match and case statement.

## Technologies Used

- [Python](https://www.python.org/)
  [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)

## Local Deployment

Please follow these steps to run this project locally on your machine;

1. Go to [GitHub repository](https://github.com/sohailshams/medi-score-calculation-py), first fork it and clone to your local machine.
1. Remember to install **python version 3.10**

### Running Tests

1. Open the project in code editor of your choice
1. Go to the project directory and run **python -m unittest tests.medi_score_tests** command
1. Please note if running on macos or ubuntu use followng command **python3 -m unittest tests.medi_score_tests**
1. For running a single test suite please follow this command **python3 -m unittest tests.medi_score_tests<class of each test suite>**
