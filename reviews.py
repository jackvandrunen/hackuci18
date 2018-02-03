class Reviews:
    def __init__(self, business_id: str, decoded_json: dict):
        self._review_text = self._generate_review_text(decoded_json)
    
    def get_review_text(self) -> [str]:
        '''Gets the text of the reviews'''
        return self._review_text

    def _generate_review_text(self, decoded_json: dict) -> [str]:
        '''Extracts the text of the reviews from the JSON data'''
        result = []
    
        for i in range(len(decoded_json["review"])):
            result.append(decoded_json["review"][i]["description"])

        return result