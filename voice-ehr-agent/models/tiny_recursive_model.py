class TinyRecursiveModel:
    """
    Local step-by-step clinical reasoning model.
    """

    def reason(self, text: str) -> dict:
        t = text.lower()

        if "shortness of breath" in t:
            diagnosis = "Possible acute heart failure exacerbation"
        elif "chest pain" in t:
            diagnosis = "Rule out acute coronary syndrome"
        else:
            diagnosis = "Undifferentiated complaint"

        return {
            "diagnosis": diagnosis,
            "confidence": 0.8
        }
