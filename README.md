# Aggregation Energy Model 

Aggregation Energy Model for  Non-Ligated and Ligated Single Atom Alloys (SAAs)

Incorporates Bare and Two Different Adsorbates (R-NH and R-S)

## Predicts Eagg in the Absence and Presence of an Adsorbate

```python
from eagg_model import regressor
predicted_eagg = regressor.predict(X)
```

## Features

Eagg Model utilizes 4 features, 3 of which are tabulated:

### ΔBE / CN<sub>adsorbate</sub>
- ΔBE = BE<sub>host</sub> - BE<sub>dopant</sub>
- Binding energy of an adsorbate on a single atom (5 to 7 atom system) (eV)
- CN<sub>ads</sub> is the coorindation number of the adsorbate on the metal surface.
- 
### ΔnCE<sub>bulk</sub> / CN
- ΔCE<sub>bulk</sub> = CE<sub>bulk</sub><sub>host</sub> - CE<sub>bulk</sub><sub>dopant</sub>
- CE<sub>bulk</sub><sub>i</sub> = bulk cohesive energy of monometallic material (eV)
- Δn = n<sub>cluster</sub> - n<sub>SAA</sub>
- n = number of dopants on the surface
- CN = coordination number of the slab (number of neighboring atoms)

### ΔEA
- ΔEA = EA<sub>host</sub> - EA<sub>dopant</sub>
- EA = electron affinity (eV)
  
### Δr
- Δr = r<sub>host</sub> - r<sub>dopant</sub>
- r= radius (au)



