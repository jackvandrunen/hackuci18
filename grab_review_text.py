import yelp_api
import reviews

if __name__ == '__main__':
    restaurant_list = ["le-diplomate-cafe-irvine",
        "in-n-out-burger-irvine",
        "blaze-fast-fired-pizza-irvine-3",
        "peets-coffee-irvine-2",
        "wendys-irvine-4"]

    review_text_file = open("reviews.txt", "w+")

    for i in restaurant_list:
        review_text_file.write("====================\n" + i + "\n====================\n")

        review_text = reviews.Reviews(yelp_api.get_all_reviews_json_data(i)).get_review_text()

        review_text_file.write("--------------------\n")
        for i in review_text:
            review_text_file.write(i + "\n--------------------\n")
    
    review_text_file.close()