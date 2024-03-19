"""
Copyright  (c)  2018-2024 Open Text  or  one  of its
affiliates.  Licensed  under  the   Apache  License,
Version 2.0 (the  "License"); You  may  not use this
file except in compliance with the License.

You may obtain a copy of the License at:
http://www.apache.org/licenses/LICENSE-2.0

Unless  required  by applicable  law or  agreed to in
writing, software  distributed  under the  License is
distributed on an  "AS IS" BASIS,  WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.
See the  License for the specific  language governing
permissions and limitations under the License.
"""
REL_TOLERANCE = 1e-6
ABS_TOLERANCE = 1e-12

rel_abs_tol_map = {
    "RandomForestRegressor": {
        "explained_variance": {"rel": 9e-02, "abs": ABS_TOLERANCE},
        "max_error": {"rel": 4e-01, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 6e-02, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": 2e-00, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "rmse": {"rel": 2e-02, "abs": ABS_TOLERANCE},
        **dict.fromkeys(["r2", "R-squared"], {"rel": 9e-02, "abs": ABS_TOLERANCE}),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": 9e-02, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 7e-02, "abs": ABS_TOLERANCE},
        "bic": {"rel": 5e-02, "abs": ABS_TOLERANCE},
        "F-statistic": {"rel": 2e-01, "abs": ABS_TOLERANCE},
        "Prob (F-statistic)": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Kurtosis": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "Skewness": {"rel": 3e-04, "abs": ABS_TOLERANCE},
        "Jarque-Bera (JB)": {"rel": 6e-03, "abs": ABS_TOLERANCE},
        "df": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ss": {"rel": 2e-01, "abs": ABS_TOLERANCE},
        "ms": {"rel": 2e-01, "abs": ABS_TOLERANCE},
        "f": {"rel": 2e-01, "abs": ABS_TOLERANCE},
        "p_value": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "coef_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "score": {"rel": 5e-02, "abs": ABS_TOLERANCE},
        "predict": {"rel": 7e-04, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": 8e-04, "abs": ABS_TOLERANCE},
    },
    "RandomForestClassifier": {
        "auc": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "prc_auc": {"rel": 4e-03, "abs": ABS_TOLERANCE},
        "accuracy": {"rel": 4e-02, "abs": ABS_TOLERANCE},
        "log_loss": {"rel": 9e10, "abs": ABS_TOLERANCE},
        "precision": {"rel": 4e-01, "abs": ABS_TOLERANCE},
        "recall": {"rel": 8e-01, "abs": ABS_TOLERANCE},
        "f1_score": {"rel": 6e-01, "abs": ABS_TOLERANCE},
        "mcc": {"rel": 4e-02, "abs": ABS_TOLERANCE},
        "markedness": {"rel": 4e-01, "abs": ABS_TOLERANCE},
        "csi": {"rel": 8e-01, "abs": ABS_TOLERANCE},
        "confusion_matrix": {"rel": 4e-01, "abs": ABS_TOLERANCE},
        "cutoff_curve": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "lift_chart": {"rel": 3e-01, "abs": ABS_TOLERANCE},
        "prc_curve": {"rel": 4e-03, "abs": ABS_TOLERANCE},
        "predict_proba": {"rel": 9e-01, "abs": ABS_TOLERANCE},
        "roc_curve": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "score": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "predict": {"rel": 7e-02, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": 1e-00, "abs": ABS_TOLERANCE},
    },
    "DecisionTreeRegressor": {
        "explained_variance": {"rel": 7e-01, "abs": ABS_TOLERANCE},
        "max_error": {"rel": 9e-02, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 9e-02, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": 2e-01, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": 2e-01, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": 2e-01, "abs": ABS_TOLERANCE},
        "rmse": {"rel": 2e-01, "abs": ABS_TOLERANCE},
        **dict.fromkeys(["r2", "R-squared"], {"rel": 7e-01, "abs": ABS_TOLERANCE}),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": 7e-01, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 3e-01, "abs": ABS_TOLERANCE},
        "bic": {"rel": 4e-01, "abs": ABS_TOLERANCE},
        "F-statistic": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "Prob (F-statistic)": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Kurtosis": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "Skewness": {"rel": 3e-04, "abs": ABS_TOLERANCE},
        "Jarque-Bera (JB)": {"rel": 6e-03, "abs": ABS_TOLERANCE},
        "df": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ss": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "ms": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "f": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "p_value": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "coef_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "score": {"rel": 4e-02, "abs": ABS_TOLERANCE},
        "predict": {"rel": 3e-16, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": 3e-16, "abs": ABS_TOLERANCE},
    },
    "DecisionTreeClassifier": {
        "auc": {"rel": 3e-01, "abs": ABS_TOLERANCE},
        "prc_auc": {"rel": 3e-01, "abs": ABS_TOLERANCE},
        "accuracy": {"rel": 2e-01, "abs": ABS_TOLERANCE},
        "log_loss": {"rel": 1e02, "abs": ABS_TOLERANCE},
        "precision": {"rel": 4e-01, "abs": ABS_TOLERANCE},
        "recall": {"rel": 7e-01, "abs": ABS_TOLERANCE},
        "f1_score": {"rel": 5e-01, "abs": ABS_TOLERANCE},
        "mcc": {"rel": 6e-01, "abs": ABS_TOLERANCE},
        "markedness": {"rel": 6e-01, "abs": ABS_TOLERANCE},
        "csi": {"rel": 9e-01, "abs": ABS_TOLERANCE},
        "confusion_matrix": {"rel": 4e-01, "abs": ABS_TOLERANCE},
        "cutoff_curve": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "lift_chart": {"rel": 5e-01, "abs": ABS_TOLERANCE},
        "prc_curve": {"rel": 4e-02, "abs": ABS_TOLERANCE},
        "predict_proba": {"rel": 1e-00, "abs": ABS_TOLERANCE},
        "roc_curve": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "score": {"rel": 4e-03, "abs": ABS_TOLERANCE},
        "predict": {"rel": 6e-02, "abs": ABS_TOLERANCE},
        "to_python": {"rel": 1e-00, "abs": ABS_TOLERANCE},
        "load_model": {"rel": 1e-00, "abs": ABS_TOLERANCE},
    },
    "DummyTreeRegressor": {
        "explained_variance": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "max_error": {"rel": 1e-03, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 1e-03, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": 1e-05, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": 1e-04, "abs": ABS_TOLERANCE},
        "rmse": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        **dict.fromkeys(
            ["r2", "R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 1e-05, "abs": ABS_TOLERANCE},
        "bic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "F-statistic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Prob (F-statistic)": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Kurtosis": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "Skewness": {"rel": 3e-04, "abs": ABS_TOLERANCE},
        "Jarque-Bera (JB)": {"rel": 6e-03, "abs": ABS_TOLERANCE},
        "df": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ss": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ms": {"rel": 1e-03, "abs": ABS_TOLERANCE},
        "f": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "p_value": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "coef_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "score": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "predict": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": 1e-01, "abs": ABS_TOLERANCE},
    },
    "DummyTreeClassifier": {
        "auc": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "prc_auc": {"rel": 1e-02, "abs": ABS_TOLERANCE},
        "accuracy": {"rel": 1e-02, "abs": ABS_TOLERANCE},
        "log_loss": {"rel": 1e-00, "abs": ABS_TOLERANCE},
        "precision": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "recall": {"rel": 1e-00, "abs": ABS_TOLERANCE},
        "f1_score": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "mcc": {"rel": 1e-02, "abs": ABS_TOLERANCE},
        "markedness": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "csi": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "confusion_matrix": {"rel": 4e-001, "abs": ABS_TOLERANCE},
        "cutoff_curve": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "lift_chart": {"rel": 1e-00, "abs": ABS_TOLERANCE},
        "prc_curve": {"rel": 1e-02, "abs": ABS_TOLERANCE},
        "predict_proba": {"rel": 1e-00, "abs": ABS_TOLERANCE},
        "roc_curve": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "score": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "predict": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": 1e-01, "abs": ABS_TOLERANCE},
    },
    "XGBRegressor": {
        "explained_variance": {"rel": 9e-01, "abs": ABS_TOLERANCE},
        "max_error": {"rel": 3e-01, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 7e-01, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": 4e-01, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": 9e-01, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": 2e-01, "abs": ABS_TOLERANCE},
        "rmse": {"rel": 7e-01, "abs": ABS_TOLERANCE},
        **dict.fromkeys(["r2", "R-squared"], {"rel": 4e-01, "abs": ABS_TOLERANCE}),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": 4e-01, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 9e-01, "abs": ABS_TOLERANCE},
        "bic": {"rel": 14e-01, "abs": ABS_TOLERANCE},
        "F-statistic": {"rel": 2e-00, "abs": ABS_TOLERANCE},
        "Prob (F-statistic)": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Kurtosis": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "Skewness": {"rel": 3e-04, "abs": ABS_TOLERANCE},
        "Jarque-Bera (JB)": {"rel": 6e-03, "abs": ABS_TOLERANCE},
        "df": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ss": {"rel": 1e-00, "abs": ABS_TOLERANCE},
        "ms": {"rel": 1e-00, "abs": ABS_TOLERANCE},
        "f": {"rel": 2e-00, "abs": ABS_TOLERANCE},
        "p_value": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "coef_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "score": {"rel": 6e-01, "abs": ABS_TOLERANCE},
        "to_json": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "predict": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": 3e-02, "abs": ABS_TOLERANCE},
    },
    "XGBClassifier": {
        "auc": {"rel": 5e-02, "abs": ABS_TOLERANCE},
        "prc_auc": {"rel": 8e-02, "abs": ABS_TOLERANCE},
        "accuracy": {"rel": 9e-02, "abs": ABS_TOLERANCE},
        "log_loss": {"rel": 8e01, "abs": ABS_TOLERANCE},
        "precision": {"rel": 5e-01, "abs": ABS_TOLERANCE},
        "recall": {"rel": 9e-01, "abs": ABS_TOLERANCE},
        "f1_score": {"rel": 7e-01, "abs": ABS_TOLERANCE},
        "mcc": {"rel": 6e-01, "abs": ABS_TOLERANCE},
        "markedness": {"rel": 8e-01, "abs": ABS_TOLERANCE},
        "csi": {"rel": 8e-01, "abs": ABS_TOLERANCE},
        "confusion_matrix": {"rel": 7e-01, "abs": ABS_TOLERANCE},
        "cutoff_curve": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "lift_chart": {"rel": 8e-01, "abs": ABS_TOLERANCE},
        "prc_curve": {"rel": 4e-02, "abs": ABS_TOLERANCE},
        "predict_proba": {"rel": 3e-00, "abs": ABS_TOLERANCE},
        "roc_curve": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "to_json": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "score": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "predict": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": 1e-00, "abs": ABS_TOLERANCE},
    },
    "Ridge": {
        "explained_variance": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "max_error": {"rel": 2e-04, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 8e-04, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": 7e-06, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": 5e-05, "abs": ABS_TOLERANCE},
        "rmse": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        **dict.fromkeys(
            ["r2", "R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 4e-06, "abs": ABS_TOLERANCE},
        "bic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "F-statistic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Prob (F-statistic)": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Kurtosis": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "Skewness": {"rel": 5e-04, "abs": ABS_TOLERANCE},
        "Jarque-Bera (JB)": {"rel": 8e-03, "abs": ABS_TOLERANCE},
        "df": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ss": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ms": {"rel": 7e-04, "abs": ABS_TOLERANCE},
        "f": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "p_value": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "coef_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "score": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "predict": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
    },
    "Lasso": {
        "explained_variance": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "max_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "rmse": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        **dict.fromkeys(
            ["r2", "R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 7e-06, "abs": ABS_TOLERANCE},
        "bic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "F-statistic": {"rel": REL_TOLERANCE, "abs": 1e-09},
        "Prob (F-statistic)": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Kurtosis": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "Skewness": {"rel": 5e-04, "abs": ABS_TOLERANCE},
        "Jarque-Bera (JB)": {"rel": 8e-03, "abs": ABS_TOLERANCE},
        "df": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ss": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ms": {"rel": 7e-04, "abs": ABS_TOLERANCE},
        "f": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "p_value": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "coef_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "score": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "predict": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
    },
    "ElasticNet": {
        "explained_variance": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "max_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "rmse": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        **dict.fromkeys(
            ["r2", "R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 7e-06, "abs": ABS_TOLERANCE},
        "bic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "F-statistic": {"rel": REL_TOLERANCE, "abs": 1e-09},
        "Prob (F-statistic)": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Kurtosis": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "Skewness": {"rel": 5e-04, "abs": ABS_TOLERANCE},
        "Jarque-Bera (JB)": {"rel": 8e-03, "abs": ABS_TOLERANCE},
        "df": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ss": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ms": {"rel": 7e-04, "abs": ABS_TOLERANCE},
        "f": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "p_value": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "coef_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "score": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "predict": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
    },
    "LinearRegression": {
        "explained_variance": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "max_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 2e-04, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "rmse": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        **dict.fromkeys(
            ["r2", "R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 4e-06, "abs": ABS_TOLERANCE},
        "bic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "F-statistic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Prob (F-statistic)": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Kurtosis": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "Skewness": {"rel": 5e-04, "abs": ABS_TOLERANCE},
        "Jarque-Bera (JB)": {"rel": 8e-03, "abs": ABS_TOLERANCE},
        "df": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ss": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ms": {"rel": 7e-04, "abs": ABS_TOLERANCE},
        "f": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "p_value": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "coef_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "score": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "predict": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
    },
    "LinearSVR": {
        "explained_variance": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "max_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "rmse": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        **dict.fromkeys(
            ["r2", "R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "bic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "F-statistic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Prob (F-statistic)": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Kurtosis": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "Skewness": {"rel": 2e-04, "abs": ABS_TOLERANCE},
        "Jarque-Bera (JB)": {"rel": 1e-02, "abs": ABS_TOLERANCE},
        "df": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ss": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ms": {"rel": 7e-04, "abs": ABS_TOLERANCE},
        "f": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "p_value": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "coef_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "score": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "predict": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": 1e-01, "abs": ABS_TOLERANCE},
    },
    "PoissonRegressor": {
        "explained_variance": {"rel": 2e-06, "abs": ABS_TOLERANCE},
        "max_error": {"rel": 2e-05, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 1e-03, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": 2e-06, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "rmse": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        **dict.fromkeys(["r2", "R-squared"], {"rel": 2e-06, "abs": ABS_TOLERANCE}),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": 2e-06, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 3e-06, "abs": ABS_TOLERANCE},
        "bic": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "F-statistic": {"rel": 7e-05, "abs": ABS_TOLERANCE},
        "Prob (F-statistic)": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "Kurtosis": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "Skewness": {"rel": 5e-04, "abs": ABS_TOLERANCE},
        "Jarque-Bera (JB)": {"rel": 8e-03, "abs": ABS_TOLERANCE},
        "df": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "ss": {"rel": 7e-05, "abs": ABS_TOLERANCE},
        "ms": {"rel": 7e-04, "abs": ABS_TOLERANCE},
        "f": {"rel": 7e-05, "abs": ABS_TOLERANCE},
        "p_value": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "coef_": {"rel": 9e-04, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": 3e-05, "abs": ABS_TOLERANCE},
        "score": {"rel": 2e-02, "abs": ABS_TOLERANCE},
        "predict": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "load_model": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
    },
    "AR": {
        "explained_variance": {"rel": 3e-05, "abs": ABS_TOLERANCE},
        "max_error": {"rel": 9e-03, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 8e-02, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": 8e-03, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": 2e-02, "abs": ABS_TOLERANCE},
        "rmse": {"rel": 3e-03, "abs": ABS_TOLERANCE},
        **dict.fromkeys(["r2", "R-squared"], {"rel": 4e-04, "abs": ABS_TOLERANCE}),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": 4e-04, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 7e-03, "abs": ABS_TOLERANCE},
        "bic": {"rel": 2e-02, "abs": ABS_TOLERANCE},
        "phi_": {"rel": 1e-01, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mse_": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "predict": {"rel": 2e-02, "abs": ABS_TOLERANCE},
    },
    "MA": {
        "explained_variance": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "max_error": {"rel": 3e-01, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 2e-02, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": 4e-02, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": 8e-02, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": 8e-02, "abs": ABS_TOLERANCE},
        "rmse": {"rel": 4e-02, "abs": ABS_TOLERANCE},
        **dict.fromkeys(["r2", "R-squared"], {"rel": 4e-02, "abs": ABS_TOLERANCE}),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": 4e-02, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 7e-03, "abs": ABS_TOLERANCE},
        "bic": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "phi_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mse_": {"rel": 8e-02, "abs": ABS_TOLERANCE},
        "predict": {"rel": 3e-03, "abs": ABS_TOLERANCE},
    },
    "ARMA": {
        "explained_variance": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "max_error": {"rel": 4e-06, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 1e-04, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": 1e-05, "abs": ABS_TOLERANCE},
        "rmse": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        **dict.fromkeys(
            ["r2", "R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 6e-03, "abs": ABS_TOLERANCE},
        "bic": {"rel": 2e-02, "abs": ABS_TOLERANCE},
        "phi_": {"rel": 5e-05, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mse_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "predict": {"rel": 9e-03, "abs": ABS_TOLERANCE},
    },
    "ARIMA": {
        "explained_variance": {"rel": 3e-03, "abs": ABS_TOLERANCE},
        "max_error": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "median_absolute_error": {"rel": 8e-02, "abs": ABS_TOLERANCE},
        "mean_absolute_error": {"rel": 2e-02, "abs": ABS_TOLERANCE},
        "mean_squared_error": {"rel": 3e-03, "abs": ABS_TOLERANCE},
        "mean_squared_log_error": {"rel": 3e-02, "abs": ABS_TOLERANCE},
        "rmse": {"rel": 2e-03, "abs": ABS_TOLERANCE},
        **dict.fromkeys(["r2", "R-squared"], {"rel": 2e-04, "abs": ABS_TOLERANCE}),
        **dict.fromkeys(
            ["r2_adj", "Adj. R-squared"], {"rel": 2e-04, "abs": ABS_TOLERANCE}
        ),
        "aic": {"rel": 5e-03, "abs": ABS_TOLERANCE},
        "bic": {"rel": 2e-02, "abs": ABS_TOLERANCE},
        "phi_": {"rel": 8e-01, "abs": ABS_TOLERANCE},
        "intercept_": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
        "mse_": {"rel": 3e-03, "abs": ABS_TOLERANCE},
        "predict": {"rel": 4e-02, "abs": ABS_TOLERANCE},
    },
    "KMeans": {
        "predict": {"rel": 6e-01, "abs": ABS_TOLERANCE},
        "to_python": {"rel": REL_TOLERANCE, "abs": ABS_TOLERANCE},
    },
    "TENSORFLOW": REL_TOLERANCE,
    "TFIDF": 1e-01,
}

REGRESSION_MODELS = [
    "RandomForestRegressor",
    "DecisionTreeRegressor",
    "DummyTreeRegressor",
    "XGBRegressor",
    "LinearRegression",
    "Ridge",
    "Lasso",
    "ElasticNet",
    "LinearSVR",
    "PoissonRegressor",
]
CLASSIFICATION_MODELS = [
    "RandomForestClassifier",
    "DecisionTreeClassifier",
    "DummyTreeClassifier",
    "XGBClassifier",
]
TIMESERIES_MODELS = ["AR", "MA", "ARMA", "ARIMA"]
CLUSTER_MODELS = ["KMeans"]
