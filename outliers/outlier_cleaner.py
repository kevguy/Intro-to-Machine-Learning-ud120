#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for i in range(0, len(predictions)):
        cleaned_data.append( (ages[i], net_worths[i], (predictions[i] - net_worths[i])**2) )
    
    '''
    for i in range(0, len(cleaned_data)):
        print cleaned_data[i]
    '''

    ### sorted by error, i.e. the second element in the tuple
    cleaned_data = sorted(cleaned_data, key=lambda tup: tup[2])

    '''
    for i in range(0, len(cleaned_data)):
        print cleaned_data[i]
    '''

    cleaned_data = cleaned_data[0:int(len(cleaned_data)*0.9)]
    print 'Number of elements left is ', len(cleaned_data)
    
    return cleaned_data

