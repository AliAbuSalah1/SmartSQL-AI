def generate_local_sql(question):

    question = question.lower()


    if "all products" in question or "show me all products" in question:
        return "SELECT * FROM products;"


    if "all customers" in question or "show me all customers" in question:
        return "SELECT * FROM customers;"


    if "all orders" in question or "show me all orders" in question:
        return "SELECT * FROM orders;"


    if "expensive products" in question:
        return "SELECT * FROM products WHERE price > 500;"


    return None