from rj.settings import DEFAULT_SETTINGS_DICT as settings
try:
    import bcrypt

except ModuleNotFoundError:
    print("bcrypt is not installed. Please install.")

class Secrets:
    @staticmethod
    def hash_password(string):
        password_bytes = string.encode("utf-8")
        salt = bcrypt.gensalt(12)
        hashed_password = bcrypt.hashpw(password_bytes,salt)
        return hashed_password.decode("utf-8")

    @staticmethod
    def check_password(string1, string2):
        return bcrypt.checkpw(
            string1.encode("utf-8"),
            string2.encode("utf-8")
        )
         
class API:
    @staticmethod
    def generate_api_key():

        import secrets
        from rj.settings import API_SIGNATURE as api_signature
        token =secrets.token_urlsafe(64)
        start = api_signature["start"]
        end = api_signature["end"]
        api_key = f"{start} {token} {end}"
        return api_key
   