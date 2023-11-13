import pandas as pd
from flask import send_file
from app.controllers.read import fetch_session_participants

def generate_participants_excel(session_uuid):
    # create participants dictionary
    all_participants = fetch_session_participants(session_uuid)
    sheet_index = 0
    participants = {
        'First Name': {},
        'Last Name': {},
        'Email Address': {},
        'Department': {},
        'Registration Timestamp': {}
    }
    for participant in all_participants:
        participants['First Name'][sheet_index] = participant['first_name']
        participants['Last Name'][sheet_index] = participant['last_name']
        participants['Email Address'][sheet_index] = participant['email_address']
        participants['Department'][sheet_index] = participant['department']
        participants['Registration Timestamp'][sheet_index] = participant['created_at'].strftime("%d/%m/%Y %H:%M:%S")
        sheet_index = sheet_index + 1
    
    # forming dataframe
    data = pd.DataFrame(participants)
    # storing into the excel file
    data.to_excel("app/static/Participants_Sheets/cifor_icraf_events_participants_sheet_"+session_uuid+".xlsx", index=False)
    
    return send_file("static/Participants_Sheets/cifor_icraf_events_participants_sheet_"+session_uuid+".xlsx", as_attachment=True)