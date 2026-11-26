class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0

            # Pack as many words as possible
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            line_words = words[i:j]
            gaps = j - i - 1

            # Last line or single word: left justify
            if j == n or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))

            else:
                total_spaces = maxWidth - line_length
                space_each = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (space_each + (1 if k < extra_spaces else 0))

                line += line_words[-1]

            result.append(line)
            i = j

        return result