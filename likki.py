from spellchecker import SpellChecker

def correct_spelling(text):
    spell = SpellChecker()
    
    # Split the input text into words
    words = text.split()
    
    # Correct the spelling of each word
    corrected_words = [spell.candidates(word) for word in words]
    
    # Create a list of the best candidates for each word
    corrected_words = [spell.candidates(word)[0] if spell.candidates(word) else word for word in words]
    
    # Join the corrected words back into a single string
    corrected_text = ' '.join(corrected_words)
    return corrected_text

# Example usage
if __name__ == "__main__":
    input_text = "Ths is a smple txt with sme errrs."
    corrected_text = correct_spelling(input_text)
    print("Original Text: ", input_text)
    print("Corrected Text: ", corrected_text)
