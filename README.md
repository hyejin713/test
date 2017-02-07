# test

# matrix factorization

Usage:

python factorizer.py [path/to/triplets.feather] [maximum_iterations] [what_to_learn] [[regularization_parameter] [rank]]

For example, to learn 5 latent features:

python factorizer.py ~/Desktop/ratings_triplets.feather 100 features-only 10.0 5
