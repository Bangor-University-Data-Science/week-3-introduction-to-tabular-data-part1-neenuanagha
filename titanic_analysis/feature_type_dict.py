def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],  # Fill with continuous numerical features
            'discrete': []  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Fill with nominal categorical features
            'ordinal': []  # Fill with ordinal categorical features
        }
    }
    
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numerical_columns:
        if df[col].dtype == 'int64':  # Integer columns are often discrete
            feature_types['numerical']['discrete'].append(col)
        else:  # Float columns are typically continuous
            feature_types['numerical']['continuous'].append(col)
    
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    for col in categorical_columns:
        if col in ['Pclass']:  # Add rules for ordinal features based on known columns
            feature_types['categorical']['ordinal'].append(col)
        else:
            feature_types['categorical']['nominal'].append(col)
    
    return feature_types
