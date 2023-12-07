import dependencies as deps

def get_trigram_name_from_binary(binary_string, trigram_file='trigrams_64.txt'):
    trigram_name = 'Unknown'
    with open(trigram_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3 and parts[2].strip() == binary_string:
                trigram_name = parts[1].strip()
                break
    return trigram_name

class LunarDateConverter:
    @staticmethod
    def convert_to_lunar(dt):
        # Your existing conversion logic here
        lunar_date = deps.Converter.Solar2Lunar(deps.Solar(dt.year, dt.month, dt.day))
        modified_year = (lunar_date.year - 3) % 12
        formatted_lunar_date = f'{modified_year:02d}{lunar_date.month:02d}{lunar_date.day:02d}'
        time_period = (dt.hour + 1) // 2 % 12 + 1
        return f'{formatted_lunar_date}{time_period}'.strip()

class TrigramLoader:
    @staticmethod
    def load_trigrams(filename):
        trigrams = {}
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:  
                    trigrams[parts[0]] = parts[2].strip()  
        return trigrams


class TrigramCalculator:
    def __init__(self, lunar_date):
        self.lunar_date = lunar_date

    def calculate_and_lookup(self, trigrams):
        year, month, day_time = int(self.lunar_date[:2]), int(self.lunar_date[2:4]), int(self.lunar_date[4:])
        total = year + month + day_time
        remainder = str(total % 8)
        if remainder == '0':
            remainder = '8'
        trigram_result = trigrams.get(remainder, 'Unknown')
        return trigram_result

    def calculate_and_lookup_extended(self, trigrams):
        numbers = [int(self.lunar_date[i:i+2]) for i in range(0, len(self.lunar_date), 2)]
        total = sum(numbers)
        remainder = str(total % 8)
        if remainder == '0':
            remainder = '8'
        return trigrams.get(remainder, 'Unknown'), total
    
    def variant_binary_sequence(self, binary_string, total):
        # Step 1: Reverse the sequence
        reversed_binary = binary_string[::-1]

        # Step 2: Calculate the index i
        i = total % 6
        i = 6 if i == 0 else i
        i = min(i, total)  # Ensure i is not larger than total

        # Step 3: Change the i-th number in the new sequence
        char_list = list(reversed_binary)
        char_list[i - 1] = '0' if char_list[i - 1] == '1' else '1'
        modified_binary = ''.join(char_list)

        # Step 4: Reverse the sequence again
        original_order_binary = modified_binary[::-1]

        return original_order_binary

    def binary_to_symbol(self, binary_string):
        symbol_representation = ''
        token_count = 0 

        for char in binary_string:
            if char == '1':
                symbol_representation += '---\n'
            elif char == '0':
                symbol_representation += '- -\n'
            token_count += 1

            if token_count % 6 == 0 and token_count < len(binary_string):
                symbol_representation += '\n'

        return symbol_representation

    def process_and_print_tokens(self, binary_string):
        trimmed_binary = binary_string[1:-1]
        first_part = trimmed_binary[:3]
        second_part = trimmed_binary[-3:]
        reciprocal_binary = first_part + second_part

        return reciprocal_binary