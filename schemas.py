recipe_schema = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['title', 'url', 'category', 'subcategory', 'image', 'author', 'servings', 'ingredients', 'stages'],
        'properties': {
            'title': {
                'bsonType': 'string',
                'description': 'recipe title is required and it must be string.'
            },
            'url': {
                'bsonType': 'string',
                'description': 'recipe url is required and it must be string.'
            },
            'category': {
                'bsonType': 'object',
                'required': ['title', 'url'],
                'properties': {
                    'title': {
                        'bsonType': 'string',
                        'description': 'category title must be a string and is required.'
                    },
                    'url': {
                        'bsonType': 'string',
                        'description': 'category url must be a string and is required.'
                    }
                },
                'description': 'category must be an object with title and url fields.'
            },
            'subcategory': {
                'bsonType': 'object',
                'required': ['title', 'url'],
                'properties': {
                    'title': {
                        'bsonType': 'string',
                        'description': 'subcategory title must be a string and is required.'
                    },
                    'url': {
                        'bsonType': 'string',
                        'description': 'subcategory url must be a string and is required.'
                    }
                },
                'description': 'subcategory must be an object with title and url fields.'
            },
            'image': {
                'bsonType': 'string',
                'description': 'recipe image is required and it must be string.'
            },
            'author': {
                'bsonType': 'string',
                'description': 'recipe author is required and it must be string.'
            },
            'servings': {
                'bsonType': 'string',
                'description': 'recipe servings is required and it must be string.'
            },
            'ingredients': {
                'bsonType': 'array',
                'items': {
                    'bsonType': 'string',
                    'description': 'ingredients must be a string.'
                },
                'description': 'ingredients must be an array of strings and is required.'
            },
            'stages': {
                'bsonType': 'array',
                'items': {
                    'bsonType': 'object',
                    'required': ['step', 'description'],
                    'properties': {
                        'step': {
                            'bsonType': 'string',
                            'description': 'step must be a string and is required.'
                        },
                        'description': {
                            'bsonType': 'string',
                            'description': 'stage description must be a string and is required.'
                        }
                    }
                },
                'description': 'stages must be an array of objects with step and description fields.'
            }
        }
    }
}
