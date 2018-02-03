import yelp_api
import reviews

if __name__ == '__main__':
    review_data = yelp_api.get_all_reviews_json_data("wendys-irvine-4")

    wendys_reviews = reviews.Reviews("wendys-irvine-4", review_data)

    review_text = wendys_reviews.get_review_text()
    for i in range(len(review_text)):
        print(wendys_reviews.get_review_text()[i], "\n")
