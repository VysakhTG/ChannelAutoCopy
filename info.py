from os import environ


#bot information
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

#channel
FROM = int(os.environ.get("FROM", ""))
TO = int(os.environ.get("TO", ""))

#server
PORT = environ.get("PORT", "8080")
