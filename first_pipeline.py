def test_variable_numer(predictions, actual, categorical):
    '''
    INPUT: list predictions: list of a model's predictions
           pandas series actual: series of the actual values
           pandas series categorical: pandas series of to which category each
           row prediction/value pair belongs
    OUTPUT: dict {'False':float, 'False %IQR':float ,'True':float,
                  'True %IQR':float}
           Where True and False equate to the predictions and True %IQR and
           False %IQR are the raw differences for True and False divided by the
           IQR of the difference between the actual values and the predictions
    '''
    difference = pd.DataFrame(actual-predictions)
    diff_iqr = difference.quantile(.75) - difference.quantile(.25)

    # Calculating differences for 0:
    diff_0 = difference[categorical == 0].mean()

    # Calculating differences for 1:
    diff_1 = difference[categorical == 1].mean()

    return dict({'False': diff_0[0], 'False %IQR': diff_0[0]/diff_iqr,
                 'True': diff_1[0], 'True %IQR': diff_1[0]/diff_iqr})