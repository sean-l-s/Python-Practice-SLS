def vowel_freq_count(string):
    vowels = "aeiou"
    v_count = 0
    for i in string.lower():
        if i in vowels:
            v_count += 1
    return v_count

if __name__ == "__main__":
    print(f"Number of vowels: {vowel_freq_count("Learning Python is fun!")}")