class Utils:
    def generate_rating_bar(self, rating: float):
        if rating >= 0 and rating < 0.5:
            return """
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
            """
        elif rating >= 0.5 and rating < 1:
            return """
                <span class="fa fa-star-half-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
            """
        elif rating >= 1 and rating < 1.5:
            return """
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
            """
        elif rating >= 1.5 and rating < 2:
            return """
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star-half-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
            """
        elif rating >= 2 and rating < 2.5:
            return """
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
            """
        elif rating >= 2.5 and rating < 3:
            return """
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star-half-o checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
            """
        elif rating >= 3 and rating < 3.5:
            return """
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star-o checked"></span>
                <span class="fa fa-star-o checked"></span>
            """
        elif rating >= 3.5 and rating < 4:
            return """
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star-half-o checked"></span>
                <span class="fa fa-star-o checked"></span>
            """
        elif rating >= 4 and rating < 4.5:
            return """
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star-o checked"></span>
            """
        elif rating >= 4.5 and rating < 5:
            return """
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star-half-o checked"></span>
            """
        elif rating == 5:
            return """
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
                <span class="fa fa-star checked"></span>
            """
