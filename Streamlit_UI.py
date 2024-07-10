import streamlit as st
import mysql.connector

# Connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="0512",
        database="hospital_db"
    )

# Function to insert patient data into MySQL database
def insert_patient_data(patient_id, age_group,gender,type_of_admission,admission_date):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        query = "INSERT INTO admission (Patient_ID, Age_Group,Gender,Type_of_Admission, Admission_Date) VALUES (%s, %s, %s, %s, %s)"
        data = (patient_id, age_group,gender,type_of_admission, admission_date)

        cursor.execute(query, data)
        conn.commit()
        st.success("Patient data inserted successfully!")
    except Exception as e:
        st.error(f"Error inserting patient data: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Function to insert medical encounters data into MySQL database
def insert_medical_data(patient_id, ccs_diagnosis_code, ccs_diagnosis_description, ccs_procedure_code, ccs_procedure_description, apr_drg_code, apr_drg_description, apr_mdc_code, apr_mdc_description, apr_severity_of_illness_code, apr_severity_of_illness_description, apr_risk_of_mortality, apr_medical_surgical_description):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        query = "INSERT INTO medical_encounters (Patient_ID, CCS_Diagnosis_Code, CCS_Diagnosis_Description, CCS_Procedure_Code, CCS_Procedure_Description, APR_DRG_Code, APR_DRG_Description, APR_MDC_Code, APR_MDC_Description, APR_Severity_of_Illness_Code, APR_Severity_of_Illness_Description, APR_Risk_of_Mortality, APR_Medical_Surgical_Description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (patient_id, ccs_diagnosis_code, ccs_diagnosis_description, ccs_procedure_code, ccs_procedure_description, apr_drg_code, apr_drg_description, apr_mdc_code, apr_mdc_description, apr_severity_of_illness_code, apr_severity_of_illness_description, apr_risk_of_mortality, apr_medical_surgical_description)
        cursor.execute(query, data)
        conn.commit()
        st.success("Medical encounters data inserted successfully!")
    except Exception as e:
        st.error(f"Error inserting medical encounters data: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def patient_data_page(data):
    st.title("Patient Data Information")
    data['patient_id'] = st.number_input("Patient ID", value=0, step=1)
    data['age_group'] = st.selectbox("Age Group", ['30 to 49', '70 or Older', '0 to 17', '18 to 29', '50 to 69'])
    #data['zip_code'] = st.number_input("Zip Code", value=0, step=1)
    data['gender'] = st.radio("Gender", ['M', 'F'])
    #data['race'] = st.text_input("Race")
   # data['race'] = st.text_input("Race", placeholder="(e.g., Black/African American, White, Others)")
    #data['ethnicity'] = st.text_input("Ethnicity",placeholder="e.g., Not Span/Hispanic', 'Spanish/Hispanic")
    data['type_of_admission'] = st.selectbox("Type of Admission", ['Elective', 'Urgent', 'Emergency', 'Trauma'])
    data['admission_date'] = st.date_input("Admission Date")
    return data


def medical_data_page(data):
    st.title("Medical Encounters Information")

    # Diagnosis COde
    DIG_codes = [122, 197, 142, 154, 125, 127, 126, 159, 231, 145, 238, 146, 244,
                                 153, 128, 155, 55, 58, 118, 50, 233, 95, 157, 80, 99, 133,
                                 236, 657, 152, 8, 171, 170, 189, 26, 2, 175, 131, 144, 130,
                                 660, 129, 230, 101, 187, 195, 149, 48, 237, 218, 102, 51, 108,
                                 47, 169, 172, 103, 15, 226, 59, 242, 109, 192, 181, 185, 135,
                                 100, 163, 207, 106, 193, 186, 190, 251, 222, 211, 5, 224, 46,
                                 184, 83, 148, 156, 24, 183, 140, 245, 7, 160, 191, 96, 42,
                                 250, 241, 14, 97, 205, 105, 182, 234, 253, 229, 143, 93, 49,
                                 196, 60, 239, 112, 661, 246, 17, 653, 168, 27, 115, 257, 259,
                                 90, 85, 138, 164, 136, 141, 92, 63, 663, 35, 43, 19, 38,
                                 167, 199, 173, 33, 161, 117, 147, 120, 121, 188, 203, 151, 248,
                                 139, 114, 62, 61, 18, 32, 13, 240, 659, 116, 110, 6, 3,
                                 252, 39, 12, 98, 162, 25, 137, 204, 202, 123, 201, 77, 54,
                                 670, 158, 107, 29, 654, 165, 235, 124, 4, 194, 198, 44, 180,
                                 113, 254, 214, 57, 213, 104, 84, 81, 76, 651, 655, 36, 243,
                                 21, 53, 232, 217, 212, 91, 219, 225, 177, 11, 52, 64, 662,
                                 200, 82, 656, 650, 652, 255, 166, 111, 16, 94, 79, 134, 178,
                                 210, 209, 34, 132, 41, 228, 78, 56, 40, 258, 23, 1, 89,
                                 206, 227, 37, 658, 247, 87, 216, 179, 119, 9, 10, 221, 45,
                                 223, 215, 220, 256, 176, 28, 208, 20, 249, 22, 31, 30, 174,
                                 86, 88]

    data['ccs_diagnosis_code'] = st.selectbox("Select Diagnosis Code", DIG_codes)


    # Procedure Code

    PROC_codes = [0, 202, 124, 134, 216, 119, 222,  39,  84, 147,  54, 137,  70,
       115,  76,  96, 153, 127, 228, 140, 141, 146, 169, 231, 174, 168,
         4, 163, 171,  80, 135, 121, 102,  87, 128, 136, 160, 111,  75,
        89,  99, 227, 175, 221, 214,  98,  71,  86,  78, 157,  85, 125,
        90, 132, 109, 101, 117,  97,  77,  88,  94, 225,   5, 155, 193,
       107,  65,  95,  35, 116, 129, 152, 133,  63,  60,  37,  48,  36,
        55,  66,  93,  58,  67,  61, 110, 211, 100, 120,  40,  51, 164,
        72, 167,  42, 113,  27,  91, 165,  69,  81, 103, 190, 219,  83,
       148, 229,  52,  17, 217,  33, 154, 145, 184,   8, 187, 197,  10,
       142, 123, 162, 223, 199, 220, 201,  82, 122, 159, 112,  49, 139,
        12,  29, 172, 213,   3,  62,  41, 130,  19,  21, 218, 156, 205,
       210, 177, 179, 180, 108, 185, 104,  47, 161, 192, 178, 198, 114,
       208,  38,  26, 207, 118, 106,  34,  32, 131, 224, 151, 209, 173,
        74,  56, 215, 191, 170,  28,  73,  44,  45, 158,  57,  43, 189,
         1,  59,  11,   7, 188,   9,   2, 212, 226,  20, 181, 126,   6,
        92, 203, 150, 144,  50, 204,  18,  31, 196, 149,  24, 166,  30,
       138,  23, 176, 195, 105,  13, 182,  14, 143,  64, 194,  15,  16,
       206,  79,  53,  22, 183, 200,  25, 186,  68, 230]

    data['ccs_procedure_code'] = st.selectbox("Select PROCEDURE Code", PROC_codes)


# Diagnosis Related Group COde
    DRG_codes = [139, 383, 254, 249, 138, 140, 113, 463, 144, 247, 721, 244, 115,
       135, 253, 141, 425, 421, 422, 815, 197, 351, 468,  55, 861, 460,
        43, 199, 142, 384, 753, 282, 346, 513, 540, 720, 133, 245, 143,
       775, 263, 137, 342, 198, 560, 284, 424, 466, 640, 203, 194, 532,
       134,  48, 221, 301, 660, 812,  45, 952, 248, 190, 343, 201, 566,
       308, 251, 663, 252, 341, 892, 519, 626, 773, 130,  53, 770, 462,
       634, 382, 241, 204, 225, 723, 541, 465, 518, 951, 517, 200,  41,
       347,  26, 240, 207, 710, 420, 229, 542, 581, 811, 242, 639, 751,
       111, 850, 380, 340, 314, 711, 228, 564,  47, 224, 816, 722, 281,
       544, 757, 563, 317,  44, 791, 446, 530,  82,  52, 243, 930, 501,
       776, 344, 114, 220, 136, 206, 633, 385, 280, 694, 309, 680, 950,
       461, 423, 264, 223, 262, 226, 754,  58, 313, 813,  42, 302, 279,
       173, 305, 246, 121, 650, 171, 681, 661, 227, 662, 381, 844, 283,
       750,  24, 691,  50, 724, 512, 362, 120, 349, 482,  57,  46, 363,
       636, 625, 614, 196, 500, 169,   4, 760, 546,  97, 447, 514, 315,
       170, 545, 404, 531, 511, 860, 364,   5, 759,  54,  51, 756, 561,
        80, 589, 222, 180, 613, 443, 894, 361, 955, 131, 320, 316, 580,
       193, 110, 890,  23, 445, 405,  40, 772, 758, 755, 161, 441, 310,
       911, 480, 191, 442, 483, 175, 192, 484, 205, 176, 690,  49, 912,
       621, 774, 260, 623,  56, 165, 444, 174, 740, 162, 163, 304, 177,
       321,  21,  22, 651, 166, 401, 910, 167, 403, 303,  98, 261, 312,
       893, 481, 862, 752,  89,  20,  92,  93, 591, 588, 593, 611, 622,
       693, 602, 607, 132, 631, 612, 609, 603,  70, 608,  95, 565,   1,
        90, 843,  73, 510, 583,  91, 440,   6, 842, 160, 841, 863, 692,
         3, 956,   2, 630]
    data['apr_drg_code'] = st.selectbox("Select Diagnosis Related Group Code", DRG_codes)



   # Major Diagnosis Related Code
    MDC_codes = [4, 9, 6, 3, 11, 18, 10, 21, 5, 8, 1, 23, 19, 7, 13, 14, 20,
                 15, 16, 24, 2, 25, 12, 17, 22, 0]
    data['apr_mdc_code'] = st.selectbox("Select Major Diagnosis related Code", MDC_codes)


    # Severity of Illness code

    SIC_codes = [1,2,3,4,5]
    data['apr_severity_of_illness_code'] = st.selectbox("Select Severity of Illness Code", SIC_codes)



    data['apr_risk_of_mortality'] = st.selectbox("APR Risk of Mortality", ['Minor', 'Major', 'Moderate', 'Extreme'])

    data['apr_medical_surgical_description'] = st.selectbox("APR Medical Surgical Description", ['Medical','Surgical'])

    return data




# Function to insert patient data into MySQL database
def insert_patient_and_medical_data(data):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        patient_query = "INSERT INTO admission (Patient_ID, Age_Group,Gender,Type_of_Admission, Admission_Date) VALUES (%s, %s, %s, %s, %s)"
        patient_data = (data['patient_id'], data['age_group'],data['gender'],data['type_of_admission'], data['admission_date'])
        cursor.execute(patient_query, patient_data)

        medical_query = "INSERT INTO medical_encounters (Patient_ID, CCS_Diagnosis_Code,CCS_Procedure_Code,APR_DRG_Code,APR_MDC_Code,APR_Severity_of_Illness_Code,APR_Risk_of_Mortality, APR_Medical_Surgical_Description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        medical_data = (
        data['patient_id'], data['ccs_diagnosis_code'],data['ccs_procedure_code'],
        data['apr_drg_code'],data['apr_mdc_code'],
        data['apr_severity_of_illness_code'],
        data['apr_risk_of_mortality'], data['apr_medical_surgical_description'])
        cursor.execute(medical_query, medical_data)

        # Commit the transaction
        conn.commit()
        st.success("Patient and medical data inserted successfully!")
    except Exception as e:
        st.error(f"Error inserting data: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


import pandas as pd
def connect_to_database1():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="0512",
        database="hospital_insights_db"
    )

# Function to fetch data from Resources table
def fetch_resources_data():
    try:

        conn = connect_to_database1()
        cursor = conn.cursor()

        # Query to fetch all data from Resources table
        # query = "SELECT patient_id,admission_date,predicted_los,Predicted_Discharge_Date FROM Resources order by patient_id desc limit 10"
        query = "SELECT * FROM Resources order by patient_id desc limit 10"
        cursor.execute(query)
        # Fetch all rows
        rows = cursor.fetchall()
        # Create a DataFrame from the fetched data
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(rows, columns=columns)
        return df

    except Exception as e:
        st.error(f"Error fetching data: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()




# Streamlit UI for displaying resources data
def resources_data_page():
    st.title("Resources Data")

    # Fetch data from Resources table
    resources_df = fetch_resources_data()

    if resources_df is not None:
        # Display data using Streamlit's DataFrame component
        st.dataframe(resources_df)


# Main function to run Streamlit app
def main():
    st.set_page_config(page_title="Hospital Data Collection", page_icon="🏥", layout="wide")
    st.sidebar.title("Length of Stay Prediction ")
    pages = {
        "Admission Information": patient_data_page,
        "Medical Encounters Information ": medical_data_page
    }
    data = {}
    for page_title, page_func in pages.items():
        st.sidebar.markdown(f"## {page_title}")
        data = page_func(data)
        st.sidebar.markdown("---")
    if st.sidebar.button("Submit"):
        insert_patient_and_medical_data(data)
    connect_to_database()
    st.sidebar.title("Predicted Result Table")
    page = st.sidebar.radio("",["Resources Data"])

    if page == "Resources Data":
        resources_data_page()

if __name__ == "__main__":
    main()