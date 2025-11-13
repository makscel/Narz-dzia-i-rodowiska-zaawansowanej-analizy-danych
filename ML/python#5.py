import numpy as np

class DecisionStumpClassifier:
    def __init__(self):
        self.feature_index = None
        self.threshold = None
        self.polarity = 1
        self.alpha = None

    def fit(self, X, y):
        m, n = X.shape
        self.alpha = 1
        min_error = float('inf')

        for feature_index in range(n):
            feature_values = np.expand_dims(X[:, feature_index], axis=1)
            unique_values = np.unique(feature_values)

            for threshold in unique_values:
                p = 1
                predictions = np.ones(m)
                predictions[X[:, feature_index] < threshold] = -1

                error = sum(y != predictions)

                if error > 0.5 * m:
                    error = m - error
                    p = -1

                if error < min_error:
                    self.polarity = p
                    self.threshold = threshold
                    self.feature_index = feature_index
                    min_error = error

    def predict(self, X):
        n_samples = X.shape[0]
        X_column = X[:, self.feature_index]
        predictions = np.ones(n_samples)
        if self.polarity == 1:
            predictions[X_column < self.threshold] = -1
        else:
            predictions[X_column >= self.threshold] = -1
        return predictions

# Example usage
X = np.array([[2, 3], [1, 1], [2, 1], [1, 2]])
y = np.array([1, -1, 1, -1])
stump = DecisionStumpClassifier()
stump.fit(X, y)
predictions = stump.predict(X)
print(predictions)