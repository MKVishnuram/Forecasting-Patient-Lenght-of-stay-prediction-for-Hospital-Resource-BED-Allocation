
import math
def convert_to_numeric(age_str):
    if isinstance(age_str, float) and math.isnan(age_str):
        return None
    age_str = str(age_str)
    if 'to' in age_str:
        lower, upper = map(int, age_str.split('to'))
        return int(math.ceil((lower + upper) / 2))
    elif 'or Older' in age_str:
        return int(age_str.split()[0])
    else:
        try:
            return int(age_str)
        except ValueError:
            return None


# Function to map gender to numeric
def map_gender(gender):
    if gender == 'F':
        return 0
    elif gender == 'M':
        return 1
    else:
        return None


def map_admission_type(admission_type):
    if admission_type == 'Elective':
        return 0
    elif admission_type == 'Emergency':
        return 1
    elif admission_type == 'Newborn':
        return 2
    elif admission_type == 'Trauma':
        return 3
    elif admission_type == 'Urgent':
        return 4
    else:
        return None


# Function to map apr_risk_of_mortality to numeric
def map_apr_risk_of_mortality(risk):
    if risk == 'Minor':
        return 2
    elif risk == 'Major':
        return 1
    elif risk == 'Moderate':
        return 3
    elif risk == 'Extreme':
        return 0
    else:
        return None


# Function to map apr_medical_surgical_description to numeric
def map_apr_medical_surgical_description(description):
    if description == 'Medical':
        return 0
    elif description == 'Surgical':
        return 1
    else:
        return None


