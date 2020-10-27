# The validate_dict function that receives as a parameter a set of tuples that represent validation rules for a dictionary with string keys and values of the string type and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.


# def