import pandas as pd
import numpy as np
from typing import Tuple


def exp_ordinal_encoder_categoricas(
    X_train: pd.DataFrame, X_test: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    from sklearn.preprocessing import OrdinalEncoder
    from sklearn.compose import make_column_transformer

    X_train, X_test = X_train.copy(), X_test.copy()
    encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=np.nan)
    train_idx, test_index = X_train.index, X_test.index
    columns = X_train.columns.tolist()

    category_columns = X_train.select_dtypes(include='category').columns.tolist()
    transformer = make_column_transformer((encoder, category_columns), remainder='passthrough')
    X_train = transformer.fit_transform(X_train)
    X_test = transformer.transform(X_test)

    return (
        pd.DataFrame(X_train, columns=columns, index=train_idx),
        pd.DataFrame(X_test, columns=columns, index=test_index)
    )


def exp_onehotencoder_categoricas(
    X_train: pd.DataFrame, X_test: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import make_column_transformer
    from sklearn.pipeline import make_pipeline

    X_train, X_test = X_train.copy(), X_test.copy()
    encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    train_idx, test_index = X_train.index, X_test.index

    category_columns = X_train.select_dtypes(include='category').columns.tolist()
    transformer = make_column_transformer((encoder, category_columns), remainder='passthrough')
    pipeline = make_pipeline(transformer)

    X_train = pipeline.fit_transform(X_train)
    X_test = pipeline.transform(X_test)

    return (
        pd.DataFrame(X_train, columns=pipeline.get_feature_names_out(), index=train_idx),
        pd.DataFrame(X_test, columns=pipeline.get_feature_names_out(), index=test_index)
    )


def exp_countencoder_categoricas(
    X_train: pd.DataFrame, X_test: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    from category_encoders import CountEncoder

    X_train, X_test = X_train.copy(), X_test.copy()
    category_columns = X_train.select_dtypes(include='category').columns.tolist()
    encoder = CountEncoder(cols=category_columns, drop_invariant=True, return_df=True,
                           handle_missing='return_nan', handle_unknown='return_nan',
                           min_group_size=0.1, min_group_name='otros')

    X_train = encoder.fit_transform(X_train)
    X_test = encoder.transform(X_test)

    return X_train, X_test


def exp_targetencoder_categoricas(
    X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.Series
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    from category_encoders import TargetEncoder

    X_train, X_test, y_train = X_train.copy(), X_test.copy(), y_train.copy()
    category_columns = X_train.select_dtypes(include='category').columns.tolist()
    encoder = TargetEncoder(cols=category_columns, drop_invariant=True, return_df=True,
                            handle_missing='return_nan', handle_unknown='return_nan')

    X_train = encoder.fit_transform(X_train, y_train)
    X_test = encoder.transform(X_test)

    return X_train, X_test


def exp_ordinalencoder_rmv_high_corr(
    X_train: pd.DataFrame, X_test: pd.DataFrame, corr_threshold: float = 0.8
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    from category_encoders import OrdinalEncoder

    X_train, X_test = X_train.copy(), X_test.copy()
    category_columns = X_train.select_dtypes(include='category').columns.tolist()

    # Correlation
    corr_matrix = X_train.select_dtypes('number').corr().abs()
    upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool_))
    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > corr_threshold)]
    X_train.drop(to_drop, axis=1, inplace=True)
    X_test.drop(to_drop, axis=1, inplace=True)

    # Encode
    encoder = OrdinalEncoder(cols=category_columns, drop_invariant=True, return_df=True,
                             handle_missing='return_nan', handle_unknown='return_nan')

    X_train = encoder.fit_transform(X_train)
    X_test = encoder.transform(X_test)

    return X_train, X_test


def exp_ordinalencoder_knn_imputer(
    X_train: pd.DataFrame, X_test: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    from category_encoders import OrdinalEncoder
    # from sklearn.feature_selection import f_regression, SelectKBest
    from sklearn.impute import KNNImputer

    X_train, X_test = X_train.copy(), X_test.copy()
    category_columns = X_train.select_dtypes(include='category').columns.tolist()

    # Encode
    encoder = OrdinalEncoder(cols=category_columns, drop_invariant=True, return_df=True,
                             handle_missing='return_nan', handle_unknown='return_nan')

    X_train = encoder.fit_transform(X_train)
    X_test = encoder.transform(X_test)

    # Missin values
    imputer = KNNImputer(n_neighbors=5)
    X_train = pd.DataFrame(imputer.fit_transform(X_train), columns=X_train.columns,
                           index=X_train.index)
    X_test = pd.DataFrame(imputer.transform(X_test), columns=X_test.columns,
                          index=X_test.index)

    # Feature selection
    # selector = SelectKBest(f_regression, k=k)
    # selector.fit(X_train, y_train)

    # return X_train[selector.get_support()], X_test[selector.get_support()]
    return X_train, X_test