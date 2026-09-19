def clean_text(text:str)->str:
    text=text.strip()
    lines=text.splitlines()
    cleaned_lines=[
            line.strip()
            for line in lines
            if line.strip()
            ]
    return "\n".join(cleaned_lines)
