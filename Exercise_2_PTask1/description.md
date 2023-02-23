# Signal reconstruction with PCA and ICA

Link to repo: https://github.com/tobiashillmer/MLinWeb

## Procedure

At first a time range is generated from 0 to 50 in steps of 0.001.
With this time range the three time series of the training data are generated. To each of the time series a small amount of noise is added.

In the next step the time series are multiplied with a random matrix and thus the three time series are mixed.

After that PCA and ICA are applied to reconstruct the three original time series.

## Results

First the results of the PCA and ICA were inspected visually.
After that both methods were evaluated quantitative.
Finally both methods were tested for a sensitivity to noise.

### Visual inspection

The PCA can reconstruct the f3 correctly but it mixes f1 and f2 into two components.
The ICA reconstructs the shapes of all three time series.

### Quantitative evaluation


### Sensitivity to noise

In the previous evaluations the noise was very small. Now we will increase the noise in steps.