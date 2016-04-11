import pandas as pd

data = {'age': [38, 49, 27, 19, 54, 29, 19, 42, 34, 64,
                19, 62, 27, 77, 55, 41, 56, 32, 59, 35],
        'distance': [6169.98, 7598.87, 3276.07, 1570.43, 951.76,
                     139.97, 4476.89, 8958.77, 1336.44, 6138.85,
                     2298.68, 1167.92, 676.30, 736.85, 1326.52,
                     712.13, 3083.07, 1382.64, 2267.55, 2844.18],
        'attended': [False, False, False, True, True, True, False,
                     True, True, True, False, True, True, True,
                     False, True, True, True, True, False]}

df = pd.DataFrame(data)