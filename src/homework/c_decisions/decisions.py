#
def get_options_ratio(option, total):
    """
    Calculate the ratio of options divided by total.

    Parameters:
    option (int or float): The number of options.
    total (int or float): The total number.

    Returns:
    float: The ratio of options to total.
    """
    if total == 0:
        raise ValueError("Total cannot be zero.")
    return option / total

def get_faculty_rating(ratio):
    """
    Get the faculty rating based on the ratio.

    Parameters:
    ratio (float): The ratio of options to total.

    Returns:
    str: The faculty rating based on the ratio.
    """
    if 0.9 <= ratio < 1:
        return "Excellent"
    elif ratio > 0.8:
        return "Very Good"
    elif ratio > 0.7:
        return "Good"
    elif ratio > 0.6:
        return "Needs Improvement"
    elif 0 <= ratio <= 0.59:
        return "Unacceptable"
    else:
        raise ValueError("Invalid ratio value.")
