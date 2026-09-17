# Data dictionary

| Column | Definition | Unit |
|---|---|---|
| `Pyro_T` | Pyrolysis temperature | °C |
| `Pyro_time` | Pyrolysis duration | h |
| `SSA` | Specific surface area | m²/g |
| `PV` | Pore volume | cm³/g |
| `pore_size` | Pore size | nm |
| `C_pct` | Carbon content | % |
| `H_pct` | Hydrogen content | % |
| `O_pct` | Oxygen content | % |
| `N_pct` | Nitrogen content | % |
| `HC` | Mass-based H/C ratio calculated from elemental mass percentages | dimensionless |
| `OC` | Mass-based O/C ratio calculated from elemental mass percentages | dimensionless |
| `ONC` | Mass-based (O+N)/C ratio calculated from elemental mass percentages | dimensionless |
| `pHpzc` | Point of zero charge | pH unit |
| `Ads_temp` | Adsorption temperature | °C |
| `rotation` | Mixing speed | rpm |
| `contact_time` | Contact time | h |
| `pH` | Solution pH | pH unit |
| `C0` | Initial tetracycline concentration | mg/L |
| `dosage` | Biochar dosage | g/L |
| `TC_removal_efficiency_pct` | Tetracycline removal efficiency | % |

The released modeling matrix contains no missing values. As described in Supplementary Information Text S1, selected elemental-composition fields were completed during database preparation and the mass-based elemental ratios were then recalculated. The median imputer retained in the training pipeline is a defensive preprocessing step; it does not alter the released complete modeling matrix under the fixed train–test split (`random_state = 92`).
