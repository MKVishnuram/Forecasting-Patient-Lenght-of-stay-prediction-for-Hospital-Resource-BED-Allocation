
##Admission_Trigger

import droptrigger
import mysql.connector
#droptrigger.admdrop_trigger();
try:
    # Connect to hospital_db
    hospital_db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0512",
        database="hospital_db"
    )

    hospital_db_cursor = hospital_db_conn.cursor()

    # Create a trigger to sync data to hospital_insights_db
    trigger_query = """
    CREATE TRIGGER sync_to_admission AFTER INSERT ON hospital_db.admission
    FOR EACH ROW
    BEGIN
        INSERT INTO hospital_insights_db.admission (Patient_id, Age_Group, Gender, Type_of_Admission, Admission_date)
        VALUES (NEW.Patient_id, NEW.Age_Group, NEW.Gender, NEW.Type_of_Admission, NEW.Admission_date);
    END
    """


    hospital_db_cursor.execute(trigger_query)

    # Commit the changes
    hospital_db_conn.commit()

    print(" Admission table Trigger created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if 'hospital_db_conn' in locals() and hospital_db_conn.is_connected():
        hospital_db_cursor.close()
        hospital_db_conn.close()





# # Medical_Encounters Trigger
#
#
# import mysql.connector
#
# import droptrigger
#
# droptrigger.admdroptrigger();
#
# try:
#     # Connect to hospital_db
#     hospital_db_conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="0512",
#         database="hospital_db"
#     )
#
#     hospital_db_cursor = hospital_db_conn.cursor()
#
#     # Create a trigger to sync data to hospital_insights_db
#     trigger_query = """
#     CREATE TRIGGER sync_to_insights AFTER INSERT ON hospital_db.medical_encounters
#     FOR EACH ROW
#     BEGIN
#         INSERT INTO hospital_insights_db.medical_encounters (
#             Patient_id,
#             CCS_Diagnosis_Code,
#             CCS_Diagnosis_Description,
#             CCS_Procedure_Code,
#             CCS_Procedure_Description,
#             APR_DRG_Code,
#             APR_DRG_Description,
#             APR_MDC_Code,
#             APR_MDC_Description,
#             APR_Severity_of_Illness_Code,
#             APR_Severity_of_Illness_Description,
#             APR_Risk_of_Mortality,
#             APR_Medical_Surgical_Description
#         )
#         VALUES (
#             NEW.Patient_id,
#             NEW.CCS_Diagnosis_Code,
#             NEW.CCS_Diagnosis_Description,
#             NEW.CCS_Procedure_Code,
#             NEW.CCS_Procedure_Description,
#             NEW.APR_DRG_Code,
#             NEW.APR_DRG_Description,
#             NEW.APR_MDC_Code,
#             NEW.APR_MDC_Description,
#             NEW.APR_Severity_of_Illness_Code,
#             NEW.APR_Severity_of_Illness_Description,
#             NEW.APR_Risk_of_Mortality,
#             NEW.APR_Medical_Surgical_Description
#         );
#     END
#     """
#
#     hospital_db_cursor.execute(trigger_query)
#
#     # Commit the changes
#     hospital_db_conn.commit()
#
#     print("Medical_Encounters_Table Trigger created successfully!")
#
# except mysql.connector.Error as err:
#     print("Error:", err)
#
# finally:
#     if 'hospital_db_conn' in locals() and hospital_db_conn.is_connected():
#         hospital_db_cursor.close()
#         hospital_db_conn.close()
#
#
# ## PAtient_INFO Trigger
#
# import mysql.connector
# droptrigger.admdroptrigger()
# try:
#     # Connect to hospital_db
#     hospital_db_conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="0512",
#         database="hospital_db"
#     )
#
#     hospital_db_cursor = hospital_db_conn.cursor()
#
#     # Drop the trigger for patients_info if it exists
#     hospital_db_cursor.execute("DROP TRIGGER IF EXISTS sync_to_insights_patients_info")
#
#     # Create a trigger to sync data to hospital_insights_db for patients_info
#     trigger_query = """
#     CREATE TRIGGER sync_to_insights_patients_info AFTER INSERT ON hospital_db.patients_info
#     FOR EACH ROW
#     BEGIN
#         INSERT INTO hospital_insights_db.patients_info (Patient_id, Age_Group, Gender, Length_of_Stay)
#         VALUES (NEW.Patient_id, NEW.Age_Group, NEW.Gender, NEW.Length_of_Stay);
#     END
#     """
#
#     hospital_db_cursor.execute(trigger_query)
#     print("Patiets_Info table Trigger created successfully!")
#
# except mysql.connector.Error as err:
#     print("Error:", err)
#
# finally:
#     if 'hospital_db_conn' in locals() and hospital_db_conn.is_connected():
#         hospital_db_cursor.close()
#         hospital_db_conn.close()
