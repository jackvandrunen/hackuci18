import json

class Reviews:
    def __init__(self, decoded_json: dict):
        self._review_text_json = self._generate_review_text_json(decoded_json)
    
    def get_review_text_json(self) -> [str]:
        '''Gets the text of the reviews'''
        return self._review_text_json

    def _generate_review_text_json(self, decoded_json: dict):
        '''Extracts the text of the reviews from the JSON data'''
        result = {"reviews": []}
    
        for i in range(len(decoded_json["review"])):
            result["reviews"].append(decoded_json["review"][i]["description"])

        return json.dump(result, "reviews.json")