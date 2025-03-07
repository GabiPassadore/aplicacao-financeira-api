import phonenumbers

class PhoneHelpers:
    @staticmethod
    def format_phone_number(phone_number: str):
        try:    
            parsed_phone_number = phonenumbers.parse(phone_number, "BR")
            return phonenumbers.format_number(parsed_phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError('Invalid phone number')
        
    @staticmethod
    def validate_phone_number(phone_number: str):
        try:
            parsed_phone_number = phonenumbers.parse(phone_number, "BR")
            return phonenumbers.is_valid_number(parsed_phone_number)
        except phonenumbers.phonenumberutil.NumberParseException:
            return False