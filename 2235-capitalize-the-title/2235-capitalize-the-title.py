class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title_list = title.split()
        new_title = ''
        for st in title_list:
            if len(st) <= 2:
                new_title += st.lower() + ' '
            else:
                new_title += st.lower().capitalize() + ' '

        return new_title.strip()