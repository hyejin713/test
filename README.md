# test

# matrix factorization
https://pub.beakernotebook.com/publications/56df05ac-4f52-46fe-a22d-4f604391a577
Usage:

python factorizer.py [path/to/triplets.feather] [maximum_iterations] [what_to_learn] [[regularization_parameter] [rank]]

For example, to learn 5 latent features:

python factorizer.py ~/Desktop/ratings_triplets.feather 100 features-only 10.0 5
