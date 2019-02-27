"""
Once the necessary data is extracted from the corpus (cfr. Listing 5), it can directly
be analysed using specialised statistical libraries in Python. A version with detailed comments
can be found in the supplementary material.

https://ai.vub.ac.be/~yajadoul/jadoul_introducing-parselmouth_a-python-interface-to-praat.pdf
"""


# Maximum likelihood (ML/REML) estimation of mixed-effects linear model
import statsmodels.formula.api as smf


model = smf.mixedlm('interval ~ native', data, groups=data['speaker'])
results = model.fit()
print(results.summary())


# Bayesian estimation of mixed-effects linear model
import bambi


model = bambi.Model(data)
results = model.fit('interval ~ native', random=['1|speaker'])
print(results.summary())
