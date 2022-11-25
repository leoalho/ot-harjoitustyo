def time_to_string(time):
    remaining = time
    result = ""
    if remaining>3600:
        hours = remaining//3600
        remaining -= hours*3600
        result += f"{hours} h "
    if remaining>60:
        minutes = remaining//60
        remaining -= minutes*60
        result += f"{minutes} m "
    result += f"{remaining} s"
    return result