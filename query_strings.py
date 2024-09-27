class Queries:
    @staticmethod
    def pipeline_avg():
        return [
            {
                "$match": {
                    "ingredients": {"$type": "array"}

                }
            },
            {
                "$project": {
                    "ingredients_count": {"$size": "$ingredients"}
                }
            },
            {
                "$group": {
                    "_id": None,
                    "average_ingredients": {"$avg": "$ingredients_count"},
                }
            }
        ]

    @staticmethod
    def avg_steps():
        return [
            {
                "$match": {
                    "ingredients": {"$type": "array"}

                }
            },
            {
                "$project": {
                    "stages_count": {"$size": "$stages"}
                }
            },
            {
                "$group": {
                    "_id": None,
                    "average_stages": {"$avg": "$stages_count"},
                }
            }
        ]

    @staticmethod
    def most_servings():
        return [
            {
                "$sort": {
                    "servings": -1
                }
            },
            {
                "$limit": 1
            },
            {
                "$project": {
                    "_id": 0,
                    "title": 1,
                    "url": 1
                }
            }
        ]

    @staticmethod
    def author_with_most_recipes():
        return [
            {
                "$group": {
                    "_id": "$author",
                    "recipe_count": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "recipe_count": -1
                }
            },
            {
                "$limit": 1
            }
        ]
