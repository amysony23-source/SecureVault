from auth import register_user, login_user


register_user("amy", "securepassword123", "admin")


login_user("amy", "securepassword123")
