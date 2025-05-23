Currently, the generated models are fault tree models. The configurations are listed below. Although 14 options are available for customizing fault trees, the following three arguments are preferred to create fault trees in different formats:

- **The number of basic events**
- **Maximum probability for basic events**
- **Minimum probability for basic events**


### Configuration 1 `c1-P_0.01-0.05` Arguments and Values

| #  | Arguments                                          | Value                     |
|----|----------------------------------------------------|---------------------------|
| 1  | Fault tree name                                    | Autogenerated             |
| 2  | The root gate name                                 | root                      |
| 3  | The seed of the random number generator            | 123                       |
| 4  | **The number of basic events**                     | **100:50:5000**           |
| 5  | The number of house events                         | 0                         |
| 6  | The number of CCF groups                           | 0                         |
| 7  | The average number of gate arguments               | 3.0                       |
| 8  | The weights of gate types [AND, OR, K/N, NOT, XOR] | [1.0, 1.0, 1.0, 0.0, 0.0] |
| 9  | Percentage of common basic events per gate         | 0.3                       |
| 10 | Percentage of common gates per gate                | 0.1                       |
| 11 | The avg. number of parents for common basic events | 2                         |
| 12 | The avg. number of parents for common gates        | 2                         |
| 13 | **Maximum probability for basic events**           | **0.05**                  |
| 14 | **Minimum probability for basic events**           | **0.01**                  |


