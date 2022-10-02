import marqo

mq = marqo.Client(url='http://localhost:9002')

mq.index("index").add_documents([
    {"Dessert": "Tiramisu",
        "Ingredients": "ladyfingers (savoiardi), egg yolks, sugar, coffee, mascarpone cheese, and cocoa powder"},
    {"Dessert": "Cookies",
        "Ingredients": "unsalted butter, granulated sugar, flour and a touch of vanilla",
        "_id": "article_500"}])

results = mq.index("index").search(
    q="what dessert better suits with milk")
