import json
import Connectors
import Transformations
import AutoML
try:
    BostonHousing_DBFS = Connectors.DBFSConnector.fetch(
        [], {}, "5e982c8ba9264a2d660fdf51", spark, "{'url': '/Demo/BostonTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapib8073bbfa952efa9d363b234ce06e2c6', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    BostonHousing_AutoFE = Transformations.TransformationMain.run(["5e982c8ba9264a2d660fdf51"], {"5e982c8ba9264a2d660fdf51": BostonHousing_DBFS}, "5e982c8ba9264a2d660fdf52", spark, json.dumps({"FE": [{"transformationsData": {}, "feature": "CRIM", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "3.49", "stddev": "8.4", "min": "0.00632", "max": "88.9762", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "ZN", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "11.62", "stddev": "23.54", "min": "0.0", "max": "100.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "INDUS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "11.15", "stddev": "6.91", "min": "0.46", "max": "27.74", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "CHAS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "0.07", "stddev": "0.26", "min": "0.0", "max": "1.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "NOX", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "0.55", "stddev": "0.12", "min": "0.385", "max": "0.871", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "RM", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "6.29", "stddev": "0.71", "min": "3.561", "max": "8.78", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "AGE", "type": "real", "selected": "True", "replaceby": "mean", "stats": {
                                                                  "count": "450", "mean": "68.8", "stddev": "28.26", "min": "2.9", "max": "100.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "DIS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "3.83", "stddev": "2.13", "min": "1.1296", "max": "12.1265", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "RAD", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "9.43", "stddev": "8.61", "min": "1.0", "max": "24.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "TAX", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "407.42", "stddev": "166.95", "min": "187.0", "max": "711.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "PTRATIO", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "18.44", "stddev": "2.18", "min": "12.6", "max": "22.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "B", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "356.64", "stddev": "91.02", "min": "0.32", "max": "396.9", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "LSTAT", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "12.69", "stddev": "7.24", "min": "1.73", "max": "37.97", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "MEDV", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "450", "mean": "22.71", "stddev": "9.29", "min": "5.0", "max": "50.0", "missing": "0"}, "transformation": ""}]}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionRegression(BostonHousing_AutoFE, [
                              "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"], "MEDV")

except Exception as ex:
    print(ex)
