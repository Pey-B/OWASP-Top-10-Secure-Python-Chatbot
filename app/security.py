BLOCKED_TERMS = [
    "diagnose",
    "prescribe",
    "medical record",
    "test result",
    "ignore previous instructions"
]

def enforce_security(user_input: str) -> bool:
    return not any(term in user_input.lower() for term in BLOCKED_TERMS)
