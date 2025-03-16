import torch


def split_data(X, y, train_ratio=0.8):
    """Splits X and y into training and testing sets with a given train ratio."""
    indices = torch.randperm(len(X))
    train_size = int(train_ratio * len(X))
    train_indices, test_indices = indices[:train_size], indices[train_size:]

    X_train = X[train_indices].view(-1, 1)
    X_test = X[test_indices].view(-1, 1)
    y_train = y[train_indices].view(-1, 1)
    y_test = y[test_indices].view(-1, 1)

    return X_train, y_train, X_test, y_test
