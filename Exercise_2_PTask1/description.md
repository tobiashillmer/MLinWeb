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
The ICA reconstructs f1 and reconstructs a shape similar to f2. However f2 is converted from a almost constant to a rising or falling function with a little sinus part.

### Quantitative evaluation

For Quantitative evaluation the coranking library was used.
There the metrics trustworthiness continuity and local continuity meta criteria were evaluated.
For data with no or very little noise the PCA worked better than ICA.

### Sensitivity to noise

In the previous evaluations the noise was very small. Now we will increase the noise in steps.

A small amount of noise (standard normal noise multiplied with 0.1) does not change the evaluation results.

A higher amount of noise (with factor 1) changes the results in the way that the ICA now works better.
