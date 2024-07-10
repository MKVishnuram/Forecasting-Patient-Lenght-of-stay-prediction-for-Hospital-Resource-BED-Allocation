

#  Hospital Insights DB TO  Extracting Relevant Feature for Prediction
#
# def create_trigger_admission():
#     try:
#         # Connect to MySQL server
#         mysql_conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="0512",
#             database="hospital_insights_db"
#         )
#
#         mysql_cursor = mysql_conn.cursor()
#
#         # Create trigger for admission table
#         create_trigger_query = """
#         CREATE TRIGGER sync_to_admission AFTER INSERT ON admission
#         FOR EACH ROW
#         BEGIN
#             -- Insert into print_log table
#             INSERT INTO print_log (table_name, action, data)
#             VALUES ('admission', 'INSERT', JSON_OBJECT('Patient_id', NEW.Patient_id, 'Age_Group', NEW.Age_Group, 'Gender', NEW.Gender, 'Type_of_Admission', NEW.Type_of_Admission, 'Admission_date', NEW.Admission_date));
#         END;
#         """
#
#         mysql_cursor.execute(create_trigger_query)
#
#         # Commit the changes
#         mysql_conn.commit()
#
#         print("Trigger for admission table created successfully!")
#
#     except mysql.connector.Error as err:
#         print("Error:", err)
#
#     finally:
#         if 'mysql_conn' in locals() and mysql_conn.is_connected():
#             mysql_cursor.close()
#             mysql_conn.close()


#  Hospital Insights DB TO  Extracting Relevant Feature for Prediction
#
# def create_trigger_medical_encounters():
#     try:
#         # Connect to MySQL server
#         mysql_conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="0512",
#             database="hospital_insights_db"
#         )
#
#         mysql_cursor = mysql_conn.cursor()
#
#         # Create trigger for medical_encounters table
#         create_trigger_query = """
#         CREATE TRIGGER sync_to_medical_encounters AFTER INSERT ON medical_encounters
#         FOR EACH ROW
#         BEGIN
#             -- Insert into print_log table with specific fields
#             INSERT INTO print_log (table_name, action, data)
#             VALUES ('medical_encounters', 'INSERT', JSON_OBJECT('Patient_id', NEW.Patient_id,'CCS_Diagnosis_Code',NEW.CCS_Diagnosis_Code,'CCS_Procedure_Code',NEW.CCS_Procedure_Code,'APR_DRG_Code',NEW.APR_DRG_Code,'APR_MDC_Code',NEW.APR_MDC_Code,'APR_Severity_of_Illness_Code',NEW.APR_Severity_of_Illness_Code,'APR_Risk_of_Mortality',NEW.APR_Risk_of_Mortality,'APR_Medical_Surgical_Description',NEW.APR_Medical_Surgical_Description));
#         END;
#         """
#         mysql_cursor.execute(create_trigger_query)
#
#         # Commit the changes
#         mysql_conn.commit()
#
#         print("Trigger for medical_encounters table created successfully!")
#
#     except mysql.connector.Error as err:
#         print("Error:", err)
#
#     finally:
#         if 'mysql_conn' in locals() and mysql_conn.is_connected():
#             mysql_cursor.close()
#             mysql_conn.close()