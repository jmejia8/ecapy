# Evolutionary Centers Algorithm

ECA is a physics-inspired algorithm based on the center of mass concept on 
a D-dimensional space for real-parameter single-objective optimization. The 
general idea is to promote the creation of an irregular body using K mass points
in the current population, then the center of mass is calculated to get a new direction 
for the next population... [read more.](https://www.dropbox.com/s/kqc22ki2edjtt0y/ECA-optimization.pdf)

## Parameters
- Parameters (suggested):
    - Objective function: `fobj`
    - Dimension: `D`
    - K-value:
           `K = 7`
    - Population size:
           `N = K*D`
    - stepsize:
           `eta_max = 2.0`
    - binomial probability:
           `P_bin = 0.03`
    - Exploit parameter:
           `P_exploit = 0.95`
     - Max. number of evaluations:
           `max_evals = 10000*D`

- Bounds:
     - Lower: `low_bound`
     - Upper: `up_bound`

- Search Type:
    - Maximize:
        - `minimize = True`
    - minimize:
        - `minimize = False`


## Example

You can write Python code to use ECA in your project:

```python
from ecapy import eca

# D-dimensional sphere function
def sphere(x):
    s = 0.0
    for xi in x:
        s += xi**2
    return s

x, fx = eca(sphere, D = 10, minimize=True)

```