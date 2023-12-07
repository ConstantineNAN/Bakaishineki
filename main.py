import sys
import dependencies as deps
from utilities import LunarDateConverter, TrigramCalculator, TrigramLoader, get_trigram_name_from_binary

def main(input_date):
    try:
        dt = deps.datetime.strptime(input_date, '%Y%m%d%H%M')
        lunar_date = LunarDateConverter.convert_to_lunar(dt)

        # Load trigrams using the utility function
        trigrams = TrigramLoader.load_trigrams('trigrams_8.txt')
        
        calculator = TrigramCalculator(lunar_date)
        result1 = calculator.calculate_and_lookup(trigrams)  # Unpack the tuple
        result2, total = calculator.calculate_and_lookup_extended(trigrams)  # Unpack the tuple

        # Calculate main trigram
        main_binary = result1.strip() + result2.strip()  # Apply strip to string parts
        main_trigram = calculator.binary_to_symbol(main_binary)
        main_name = get_trigram_name_from_binary(main_binary)

        # Calculate reciprocal trigram
        reciprocal_binary = calculator.process_and_print_tokens(main_binary)
        reciprocal_trigram = calculator.binary_to_symbol(reciprocal_binary)
        reciprocal_name = get_trigram_name_from_binary(reciprocal_binary)

        # Calculate variant trigram
        variant_binary = calculator.variant_binary_sequence(main_binary, total)
        variant_trigram = calculator.binary_to_symbol(variant_binary)
        variant_name = get_trigram_name_from_binary(variant_binary)

        return main_trigram, main_name, reciprocal_trigram, reciprocal_name, variant_trigram, variant_name
    except ValueError as e:
        return f"Error: {e}"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <YYYYMMDDHHMM>")
        sys.exit(1)

    input_date = sys.argv[1]
    main_trigram, main_name, reciprocal_trigram, reciprocal_name, variant_trigram, variant_name = main(input_date)  # Adjusted to unpack three values

    if isinstance(main_trigram, str) and main_trigram.startswith("Error"):
        print(main_trigram)  # Error message
    else:
        print(f"The main trigrams:\n\n{main_name}\n{main_trigram}")
        print(f"The main trigrams:\n\n{reciprocal_name}\n{reciprocal_trigram}")
        print(f"The main trigrams:\n\n{variant_name}\n{variant_trigram}")