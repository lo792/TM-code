from wordfreq import top_n_list


class Word:
    def __init__(self, text: str):
        self.text = text
    
class Word_Factory:
    def __init__(self):
        pass
    
    def get_words(self, num_words: int=25) -> list[Word]:
        """_summary_

        Args:
            num_words (int, optional): _description_. Defaults to 25.

        Returns:
            list[Word]: _description_
        """
        words: list[str] = top_n_list(num_words)
        results: list[Word] = []
        for w in words:
            results.append(Word(text=w))
        return results