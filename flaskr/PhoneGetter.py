import pandas as pd

class PhoneGetter:
    def extract_parent_contacts(file_path):
        # Read the Excel file
        try:
            data = pd.read_excel(file_path)
        except Exception as e:
            print(f"Error reading the file: {e}")
            return {}

        # Hash map to store parent names and their contact info
        parent_contacts = {}

        # Iterate through the rows of the data
        for index, row in data.iterrows():
            parent_name = row.get("Primary Contact Surname", None)
            parent_contact = row.get("Primary Contact Mobile", None)


            if pd.isna(parent_name):
                continue


            # Check if the contact is a phone number or an email
            if pd.notna(parent_contact):
                contact_info = int(parent_contact)  # Phone number
            else:
                contact_info = "No Number"  # Placeholder for non-numeric contacts


            # Add to hash map

        return parent_contacts

    if __name__ == "__main__":
        file_path = "filer/Fake_Student_Data_Updated.xlsx"
        contacts = extract_parent_contacts(file_path)

        # Print the extracted contacts
        for name, contact in contacts.items():
            print(f"{name}: {contact}")

PhoneGetter()