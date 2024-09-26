from database_generator import DatabaseGenerator


def mng_queries(db_name):
    db_conn = DatabaseGenerator(db_name, collection='recipe_collection')
    collection = db_conn.collection

    pipelines = {
        "average_ingredients": [
            {"$project": {"ingredients_count": {"$size": "$ingredients"}}},
            {"$group": {"_id": None, "average_ingredients": {
                "$avg": "$ingredients_count"}}}
        ],
        "average_steps": [
            {"$project": {"steps_count": {"$size": "$steps"}}},
            {"$group": {"_id": None, "average_steps": {"$avg": "$steps_count"}}}
        ],
        "most_portions": [
            {"$match": {"portions": {"$type": "array"}}},
            {"$project": {
                "recipe_name": 1,
                "portion_count": {"$toInt": {"$arrayElemAt": [{"$split": ["$portions", " "]}, 0]}}
            }},
            {"$sort": {"portion_count": -1}},
            {"$limit": 1}
        ],
        "auth_with_most_recipes": [
            {"$group": {"_id": "$author", "recipe_count": {"$sum": 1}}},
            {"$sort": {"recipe_count": -1}},
            {"$limit": 1}
        ]
    }

    results = {}
    for key, pipeline in pipelines.items():
        results[key] = list(collection.aggregate(pipeline))
        if results[key]:
            print_results(key, pipeline[key])


def print_results(key, result):
    if key == "average_ingredients":
        print(
            f"Average number of ingredients: {result[0]['average_ingredients']}")
    elif key == "average_steps":
        print(f"Average number of steps: {result[0]['average_steps']}")
    elif key == "most_portions":
        print(f"Most portions: {result[0]['recipe_name']}")
    elif key == "auth_with_most_recipes":
        print(
            f"The winner is: {result[0]['_id']} with {result[0]['recipe_count']} recipes")


if __name__ == '__main__':
    mng_queries(db_name="saladsdatabase")
