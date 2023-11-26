from src.model import (generate_predictions_model_mlflow,
                       load_model_from_mlflow,
                       load_preprocessing_step_from_mlflow)


def test_load_model_from_mlflow(mocker):
    expected_model = "mocked model"
    mock_mlflow = mocker.patch("src.model.mlflow")
    mock_mlflow.pyfunc.load_model = mocker.Mock(return_value=expected_model)

    run_id = "dummy_run_id"
    model_name = "dummy_model"
    model = load_model_from_mlflow(run_id, model_name)

    mock_mlflow.pyfunc.load_model.assert_called_once_with(
        f"runs:/{run_id}/{model_name}"
    )

    assert model == expected_model


def test_load_preprocessing_step_from_mlflow(mocker):
    expected_model = "mocked model"
    mock_mlflow = mocker.patch("src.model.mlflow")
    mock_mlflow.sklearn.load_model = mocker.Mock(return_value=expected_model)

    run_id = "dummy_run_id"
    preprocessing_name = "dummy_model"
    model = load_preprocessing_step_from_mlflow(run_id, preprocessing_name)

    mock_mlflow.sklearn.load_model.assert_called_once_with(
        f"runs:/{run_id}/{preprocessing_name}"
    )

    assert model == expected_model


def test_generate_predictions_model_mlflow(mocker):
    expected_results = [1, 2, 3]
    mock_model = mocker.Mock()
    mock_model.predict = mocker.Mock(return_value=expected_results)
    mock_data = mocker.Mock()

    results = generate_predictions_model_mlflow(mock_model, mock_data)

    mock_model.predict.assert_called_once_with(mock_data)

    assert results == expected_results
