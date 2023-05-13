import re


class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Validator:
    # Validate email address
    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValidationError("Invalid email address")
        return email

    # Validate password strength
    def validate_password(self, password):
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")

        # Validate password strength
        # https://stackoverflow.com/questions/1960516/python-password-strength-checker
        # https://stackoverflow.com/questions/1960516/python-password-strength-checker/50786363#50786363

        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must have at least one numeral")

        if not any(char.isupper() for char in password):
            raise ValidationError("Password must have at least one uppercase letter")

        if not any(char.islower() for char in password):
            raise ValidationError("Password must have at least one lowercase letter")

        if not any(
            char
            in [
                "!",
                "@",
                "#",
                "$",
                "%",
                "^",
                "&",
                "*",
                "(",
                ")",
                "-",
                "_",
                "+",
                "=",
                "[",
                "]",
                "{",
                "}",
                "|",
                ";",
                ":",
                '"',
                "'",
                "<",
                ">",
                ",",
                ".",
                "?",
                "/",
            ]
            for char in password
        ):
            raise ValidationError("Password must have at least one special character")

        return password


# Validate password strength
def validate_password(password):
    if len(password) < 8:
        return False

    # Validate password strength
    # https://stackoverflow.com/questions/1960516/python-password-strength-checker
    # https://stackoverflow.com/questions/1960516/python-password-strength-checker/50786363#50786363

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(
        char
        in [
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "(",
            ")",
            "-",
            "_",
            "+",
            "=",
            "[",
            "]",
            "{",
            "}",
            "|",
            ";",
            ":",
            '"',
            "'",
            "<",
            ">",
            ",",
            ".",
            "?",
            "/",
        ]
        for char in password
    ):
        return False

    return True
