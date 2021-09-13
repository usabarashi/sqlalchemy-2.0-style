from sqlalchemy import column, table

user = table("user", column("id"), column("name"), column("email_address"))
