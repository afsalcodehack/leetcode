class Solution(object):
    def isValid(self, s):
        openP = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        st = []
        for i in s:
            if i in openP:
                st.append(i)
            else:
                if not st:
                    c = st.pop()
                    close = openP.get(c)
                    if i != close:
                        return False
        if len(st) != 0:
            return False
        return True


service = Solution()
print(service.isValid("(()){}"))
