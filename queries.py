from query_strings import Queries


def mng_queries(collection):

    result_avg = list(collection.aggregate(Queries.pipeline_avg()))
    result_avg_steps = list(collection.aggregate(Queries.avg_steps()))
    result_most_servings = list(collection.aggregate(Queries.most_servings()))
    result_auth_with_most_recipes = list(
        collection.aggregate(
            Queries.author_with_most_recipes()
        )
    )
    
    return {
        'avg_num_ingredients': result_avg[0]['average_ingredients'],
        'avg_num_stages': result_avg_steps[0]['average_stages'],
        'most_servings': {
            'title':result_most_servings[0]['title'],
            'url': result_most_servings[0]['url']
        },
        'auth_with_most_recipes': {
            'id': result_auth_with_most_recipes[0]['_id'],
            'recipes': result_auth_with_most_recipes[0]['recipe_count']
        }
    }