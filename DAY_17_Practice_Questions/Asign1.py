def mask_sensitive_info(info, info_type):
    if info_type == "email":
        at_index = info.find('@')
        if at_index == -1:
            raise ValueError("Invalid email address")
        
        local_part = info[:at_index]
        domain_part = info[at_index:]

        if len(local_part) > 2:
            masked_part = local_part[0] + "*" * (len(local_part) - 2) + local_part[-1]
        else:
            masked_part = local_part
        
        return masked_part + domain_part
    
    elif info_type == "creditcard":
        if len(info) != 19 or not info.replace(' ', '').isdigit():
            raise ValueError("Invalid credit card number")
        
        return "**** **** **** " + info[-4:]
    
    else:
        raise ValueError("Invalid info type")

email = "vaibhavw2001@gmail.com"
creditcard = "1234 1223 1234 1234"

masked_email = mask_sensitive_info(email, "email")
masked_creditcard = mask_sensitive_info(creditcard, "creditcard")

print(f"The masked email is: {masked_email}")     
print(f"The masked credit card is: {masked_creditcard}")
