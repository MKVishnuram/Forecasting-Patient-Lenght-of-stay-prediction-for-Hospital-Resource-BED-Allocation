
import mysql.connector
import time
import math
import droptrigger
import json
import Prediction
import BedCount_Checker

import mysql.connector
def create_trigger_admission():
    try:
        # Connect to MySQL server
        mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0512",
            database="hospital_insights_db"
            )

        mysql_cursor = mysql_conn.cursor()

        # Check if the trigger exists
        check_trigger_query = """
        SELECT TRIGGER_NAME
        FROM information_schema.TRIGGERS
        WHERE TRIGGER_SCHEMA = 'hospital_insights_db' AND TRIGGER_NAME = 'sync_to_admission';
        """

        mysql_cursor.execute(check_trigger_query)
        trigger_exists = mysql_cursor.fetchone() is not None

        # If trigger exists, drop it
        if trigger_exists:
            drop_trigger_query = "DROP TRIGGER IF EXISTS sync_to_admission;"
            mysql_cursor.execute(drop_trigger_query)
            print("Existing trigger dropped successfully.")

        # Create (or recreate) the trigger
        create_trigger_query = """
        CREATE TRIGGER sync_to_admission AFTER INSERT ON admission
        FOR EACH ROW
        BEGIN
            -- Insert into print_log table
            INSERT INTO print_log (table_name, action, data)
            VALUES ('admission', 'INSERT', JSON_OBJECT('Patient_id', NEW.Patient_id, 'Age_Group', NEW.Age_Group, 'Gender', NEW.Gender, 'Type_of_Admission', NEW.Type_of_Admission, 'Admission_date', NEW.Admission_date));
        END;
        """

        mysql_cursor.execute(create_trigger_query)
        mysql_conn.commit()
        print("Trigger for admission table created successfully!")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if 'mysql_conn' in locals() and mysql_conn.is_connected():
            mysql_cursor.close()
            mysql_conn.close()


import mysql.connector


def create_trigger_medical_encounters():
    try:
        # Connect to MySQL server
        mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0512",
            database="hospital_insights_db"
        )

        mysql_cursor = mysql_conn.cursor()

        # Check if the trigger exists
        check_trigger_query = """
        SELECT TRIGGER_NAME
        FROM information_schema.TRIGGERS
        WHERE TRIGGER_SCHEMA = 'hospital_insights_db' AND TRIGGER_NAME = 'sync_to_medical_encounters';
        """

        mysql_cursor.execute(check_trigger_query)
        trigger_exists = mysql_cursor.fetchone() is not None

        # If trigger exists, drop it
        if trigger_exists:
            drop_trigger_query = "DROP TRIGGER IF EXISTS sync_to_medical_encounters;"
            mysql_cursor.execute(drop_trigger_query)
            print("Existing trigger dropped successfully.")

        # Create (or recreate) the trigger
        create_trigger_query = """
        CREATE TRIGGER sync_to_medical_encounters AFTER INSERT ON medical_encounters
        FOR EACH ROW
        BEGIN
            -- Insert into print_log table with specific fields
            INSERT INTO print_log (table_name, action, data)
            VALUES ('medical_encounters', 'INSERT', JSON_OBJECT('Patient_id', NEW.Patient_id, 'CCS_Diagnosis_Code', NEW.CCS_Diagnosis_Code, 'CCS_Procedure_Code', NEW.CCS_Procedure_Code, 'APR_DRG_Code', NEW.APR_DRG_Code, 'APR_MDC_Code', NEW.APR_MDC_Code, 'APR_Severity_of_Illness_Code', NEW.APR_Severity_of_Illness_Code, 'APR_Risk_of_Mortality', NEW.APR_Risk_of_Mortality, 'APR_Medical_Surgical_Description', NEW.APR_Medical_Surgical_Description));
        END;
        """

        mysql_cursor.execute(create_trigger_query)
        mysql_conn.commit()
        print("Trigger for medical_encounters table created successfully!")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if 'mysql_conn' in locals() and mysql_conn.is_connected():
            mysql_cursor.close()
            mysql_conn.close()



import Preprocessing

# Function to process input data and make predictions
def process_input_data(data):
    processed_data = []
    for row in data:
        json_obj1 = json.loads(row[3])
        json_obj2 = json.loads(row[8])

        age = Preprocessing.convert_to_numeric(str(json_obj1['Age_Group']))  # Convert age group to numeric

        gender = Preprocessing.map_gender(str(json_obj1['Gender']))  # Map gender to numeric

        admission_type = Preprocessing.map_admission_type(str(json_obj1['Type_of_Admission']))  # Map admission type to numeric

        ccs_diagnosis_code = int(json_obj2['CCS_Diagnosis_Code'])  # Keep ccs_diagnosis_code as is

        ccs_procedure_code = int(json_obj2['CCS_Procedure_Code'])  # Keep ccs_procedure_code as is

        apr_drg_code = int(json_obj2['APR_DRG_Code'])  # Keep apr_drg_code as is

        apr_mdc_code = int(json_obj2['APR_MDC_Code']) # Keep apr_mdc_code as is

        apr_severity_of_illness_code = int(json_obj2['APR_Severity_of_Illness_Code'])  # Keep apr_severity_of_illness_code as is

        apr_medical_surgical_description = Preprocessing.map_apr_medical_surgical_description(str(json_obj2['APR_Medical_Surgical_Description']))  # Map apr medical surgical description to numeric

        apr_risk_of_mortality = Preprocessing.map_apr_risk_of_mortality(str(json_obj2['APR_Risk_of_Mortality']))  # Map apr risk of mortality to numeric

        if all(v is not None for v in [age, gender, admission_type]):
            processed_data.append([age, gender, admission_type, ccs_diagnosis_code, ccs_procedure_code, apr_drg_code, apr_mdc_code,
                                   apr_severity_of_illness_code, apr_medical_surgical_description, apr_risk_of_mortality])
        print("Age, Gender, admission_type, Diagnosis_code, Procedure_code, Drg_Code, MDC_Code, Severityof_illness_code, Medical_surgical_Description,  Risk_of_Mortality ")
        print("Processed data is",processed_data)
    return processed_data



def fetch_new_data_and_predict():
    print("Calling")
    try:
        # Connect to MySQL server
        mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0512",
            database="hospital_insights_db"
        )

        mysql_cursor = mysql_conn.cursor()

        # Query print_log table for new entries from the admission table
        mysql_cursor.execute("""
            SELECT * FROM print_log
            WHERE table_name = 'admission'
            AND created_at > NOW() - INTERVAL 5 SECOND
        """)
        admission_logs = mysql_cursor.fetchall()

        # Query print_log table for new entries from the medical_encounters table
        mysql_cursor.execute("""
            SELECT * FROM print_log
            WHERE table_name = 'medical_encounters'
            AND created_at > NOW() - INTERVAL 5 SECOND
        """)
        medical_encounters_logs = mysql_cursor.fetchall()

        if len(admission_logs) == 0:
            return

        logs = [admission_logs[0] + medical_encounters_logs[0]]
        print(logs)


        # Process the new data and make predictions if logs is not empty
        if logs:
            input_data = process_input_data(logs)
            # Pass Processed data to Prediction model
            predictions = Prediction.predict_with_xgb_model(input_data)
            print("Length Of Stay Predictions Result is :", predictions)

            json_obj3 = json.loads(logs[0][3])
            patient_id = int(json_obj3['Patient_id'])
            admission_date = json_obj3['Admission_date']

            # Processing Predicted Discharge Date
            from datetime import timedelta,datetime

            # Convert admission_date string to a datetime object
            admission_date_datetime = datetime.strptime(admission_date, '%Y-%m-%d')  # Adjust the date format as needed

            # Calculate predicted_discharge_date (predicted_los + admission_date)
            predicted_discharge_date = admission_date_datetime + timedelta(days=predictions[0])  # Assuming predicted_los is in days
            #predicted_discharge_date = datetime.now()


            insert_query = """
                           INSERT INTO resources (patient_id, admission_date, predicted_los, Predicted_Discharge_Date)
                           VALUES (%s, %s, %s, %s)
                           ON DUPLICATE KEY UPDATE admission_date = VALUES(admission_date), predicted_los = VALUES(predicted_los),
                            Predicted_Discharge_Date = VALUES(predicted_discharge_date)
                           """

            # Keeping BEDCOUNT in Previous BedCount
            update_query = """
               UPDATE resources AS r
               JOIN ( SELECT bed_count FROM
               (
                SELECT bed_count FROM resources ORDER BY patient_id LIMIT 1 offset 1 ) AS prev ) AS prev_record
                SET r.bed_count = prev_record.bed_count + 1
                WHERE r.patient_id = (
                SELECT patient_id FROM ( SELECT MAX(patient_id) AS patient_id FROM resources ) AS max_patient );
            """


            # Execute the SQL query with patient_id, predicted_los, admission_date, and predicted_discharge_date
            data = (patient_id, admission_date, predictions[0], predicted_discharge_date)
            mysql_cursor.execute(insert_query, data)
            mysql_cursor.execute(update_query)
            mysql_conn.commit()

            print("Prediction result updated in resources table successfully!")


            # CAlling Bedcount Reducer Function
            BedCount_Checker.Bed_count_reducer(predicted_discharge_date)







    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if 'mysql_conn' in locals() and mysql_conn.is_connected():
            mysql_cursor.close()
            mysql_conn.close()

if __name__ == "__main__":
    #droptrigger.drop_trigger()
    create_trigger_admission()
    create_trigger_medical_encounters()

    # Fetch new data and make predictions continuously
    while True:
        fetch_new_data_and_predict()
        time.sleep(1)



