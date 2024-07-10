from datetime import datetime
import time

import mysql.connector
def Bed_count_reducer(predicted_discharge_date):
    mysql_conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "0512",
        database = "hospital_insights_db"
    )
    mysql_cursor = mysql_conn.cursor()


    # Continuously check all data IF Predicted Discharge Date Meets Current Date  Reucing the Bed Count in the resources table
    while True:
        # Fetch all data from the resources table
        select_query = "SELECT * FROM resources order by  patient_id desc limit 5"
        mysql_cursor.execute(select_query)
        resources_data = mysql_cursor.fetchall()

        # Loop through each row in the fetched data
        for row in resources_data:
            # Extract relevant information from the row
            patient_id = row[0]
            admission_date = row[2]

            current_date = datetime.now().date()
            if current_date >= predicted_discharge_date.date():
                print("PD date is", predicted_discharge_date)
                print("current date is", current_date)

                BC_query = f"UPDATE resources SET bed_count = bed_count - 1 WHERE patient_id = {patient_id}"

                try:
                    mysql_cursor.execute(BC_query)
                    mysql_conn.commit()  # Commit the transaction
                    print(f"Bed counts reduced for patient ID {patient_id}.")
                except Exception as e:
                    print("Error:", e)
                print(f"Bed counts reduced for patient ID {patient_id}.")


            # Wait for some time before checking again
        time.sleep(5)  # Sleep for 1 hour (adjust as needed)
