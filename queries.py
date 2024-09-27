from database_generator import DatabaseGenerator
from query_strings import Queries


def mng_queries(db_name):
    db_conn = DatabaseGenerator(database=db_name)
    collection = db_conn.collection

    result_avg = list(collection.aggregate(Queries.pipeline_avg()))
    if result_avg:
        print(
            f"Average number of ingredients: {
                result_avg[0]['average_ingredients']}")

    result_avg_steps = list(collection.aggregate(Queries.avg_steps()))
    if result_avg_steps:
        print(
            f"Average number of stages: {
                result_avg_steps[0]['average_stages']}")

    result_most_servings = list(collection.aggregate(Queries.most_servings()))
    if result_most_servings:
        print(
            f"Most servings: {
                result_most_servings[0]['title']}. რეცეპტის ნახვა შეგიძლიათ ლინკზე: {
                result_most_servings[0]['url']}")

    result_auth_with_most_recipes = list(
        collection.aggregate(
            Queries.author_with_most_recipes()))
    if result_auth_with_most_recipes:
        print(
            f"The winner is: {
                result_auth_with_most_recipes[0]['_id']} {
                result_auth_with_most_recipes[0]['recipe_count']} რეცეპტით")

    return result_avg, result_avg_steps, result_avg_steps, result_most_servings, result_auth_with_most_recipes

