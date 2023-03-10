from .validate import is_valid
from models.db_connection import fetch_one


class UserModule:
    def login(params):
        if not is_valid(params):
            return {"errno": 403}
        required = [
            'UserName', 'PassWord'
        ]
        for i in required:
            if i not in params:
                return {"errno": 403}
        query = f"""
            select * from patient_auth
            where (
                patient_id = '{params['UserName']}'
                or patient_mail = '{params['UserName']}'
                or phone_no = '{params['UserName']}'
            )
            and password = '{params['PassWord']}'
        """
        data = fetch_one(query)
        patient_id = data['patient_id']
        field_maps = {
            "Patient Id": "patient_id",
            "First Name": "patient_first_name",
            "Middle Name": "patient_middle_name",
            "Last Name": "patient_last_name",
            "Date Of Birth": "patient_dob",
            "Gender": "patient_gender",
            "Blood Group": "patient_blood_group",
            "Aadhaar Number": "patient_aadhar",
            "Pan Card Number": "patient_pan_number",
            "Voter Card Number": "patient_voter_id",
            "Occupation": "patient_occupation",
            "Primary Address": "patient_primary_address",
            "Primary Email": "patient_primary_email",
            "Bank Name": "bank_name",
            "Branch Name": "branch_name",
            "IFSC Code": "ifsc_code",
            "Bank Account Number": "bank_account_number",
            "Phone Number": "patient_phone_number",
            "Alternative Phone Number": "patient_phone_number",
            "Nominee Name": "nominee_name",
            "Nominee Phone Number": "nominee_phone_number",
            "Nominee Relation": "nominee_relation",
            "Nominee Email": "nominee_mail",
            "Nominee Address": "nominee_address"
        }
        query = f"""
            select * from patient_master
            where patient_id = {patient_id}
        """
        rdata = fetch_one(query)
        rdata['patient_dob'] = str(rdata['patient_dob'])
        data = {k: rdata[v] for k, v in field_maps.items()}
        print(data)
        return data
