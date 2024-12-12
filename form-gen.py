def generate_form(template, case_data):
    for field, value in case_data.items():
        template = template.replace(f"{{{{ {field} }}}}", value)
    return template
