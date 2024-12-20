def validate_email(email):
    """Validate email format."""
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_score(score):
    """Validate score is between 0 and 100."""
    try:
        score = float(score)
        return 0 <= score <= 100
    except ValueError:
        return False
