# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23681812")

API_HASH = os.environ.get("API_HASH", "3152d0cda0a21787db0c924f522374b7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6858377496:AAEHVaWfhp-2LC11YEm4oSGes5Fw7iiNJJI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Dramafilez") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "cluster0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://bhankharvansh:8xS4igRIb41EiJnz@cluster0.ctbwmpb.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6710996831').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
