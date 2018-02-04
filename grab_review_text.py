import yelp_api
import reviews

#NOW BROKEN DON'T USE!!

"""
if __name__ == '__main__':
    restaurant_list = ["le-diplomate-cafe-irvine",
        "in-n-out-burger-irvine",
        "blaze-fast-fired-pizza-irvine-3",
        "peets-coffee-irvine-2",
        "wendys-irvine-4"]

    review_text_file = open("reviews.txt", "w+")

    for i in restaurant_list:
        review_text_file.write("====================\n" + i + "\n====================\n")

        review_text_json = reviews.generate_review_text_json(yelp_api.get_all_reviews_json_data(i))

        review_text_file.write("--------------------\n")
        for j in review_text_json:
            review_text_file.write(j + "\n--------------------\n")
    
    review_text_file.close()
"""