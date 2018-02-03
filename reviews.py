from datetime import timedelta, date

a_year_ago = timedelta(days=-365)

class Reviews:
    def __init__(self, business_id: str, raw_json: dict):
        self._business_id = business_id
        self._review_text = self._generate_review_text(raw_json)
    
    def get_review_text(self) -> [str]:
        '''Gets the text of the reviews'''
        return self._review_text
    
    def get_business_id(self) -> str:
        '''Gets the ID of the business'''
        return self._business_id

    def _generate_review_text(self, raw_json: dict) -> [str]:
        '''Extracts the text of the reviews from the JSON data'''
        result = []
        json_reviews = raw_json["reviews"]
        print("---\n", raw_json["total"], "\n---\n")

        for i in range(len(json_reviews)):
            #time = json_reviews[i]["time_created"]
            #review_date = date(year=int(time[:4]), month=int(time[5:7]), day=int(time[8:10]))
            #how_long_ago = date.today() - review_date

            #if review_date < date.today() and how_long_ago.days < a_year_ago.days:
                result.append(json_reviews[i]["text"])
        
        return result
