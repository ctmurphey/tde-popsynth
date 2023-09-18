# tde-popsynth
Modeling LSST visibility of TDEs using stellar and SMBH IMFs

The goal of this project is to provide a realistic estimate of the visibility of Tidal Disruption Events (TDEs) as viewed from the Large Synoptic Survey Telescope (LSST) at the Vera C. Rubin observatory. Populations of both stars and the supermassive black holes (SMBHs) will be generated from IMFs (source both here). The light curves of the events will be generated and run through the LSST simulation pipeline to determine their visibility.

## `IMFs.py`
An auxilliary library that contains all of the IMFs and population synthyesis functions necessary for generating the stars and SMBHs. If run on it's own, it plots all IMFs and a random sample of each to verify their accuracy.

The population synthesis functions: `F_inv` and `generate_ys`, are designed to take any arbirtary pdf and create *n* random samples of the function. `F_inv` takes $X\sim Unif(0,1)$ and maps it to a given pdf. `generate_ys` just randomly samples the *n* points and calls `F_inv`.

## `lightcurves.py`
Generates set of mock light curves using `mosfit` in order to run through the LSST pipeline. Light curves are generated according to the random population synthesis functions found in `IMFs.py`