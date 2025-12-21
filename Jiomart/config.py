class Config:
    SECRET_KEY = "pooja_secret_key"

    
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Pooja%4014@localhost/Sample"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class JWTConfig:
    JWT_SECRET_KEY = "pooja_jwt_secret"

# class Config:
#     SECRET_KEY = "pooja_secret_key"

#     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Pooja@14@localhost/Sample"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

#     # ✅ JWT must be here
#     JWT_SECRET_KEY = "pooja_jwt_secret"
