class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            elif char == "[":
                count_stack.append(current_num)
                string_stack.append(current_str)

                current_num = 0
                current_str = ""

            elif char == "]":
                repeat_count = count_stack.pop()
                prev_str = string_stack.pop()

                current_str = prev_str + repeat_count * current_str

            else:
                current_str += char

        return current_str
