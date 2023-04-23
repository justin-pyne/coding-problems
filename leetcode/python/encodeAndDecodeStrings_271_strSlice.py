class Codec:
    from typing import List
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        #var
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        #vars
        decoded = []
        i = 0

        #search for delimiter, find length, extract substring
        while i < len(s):
            delim = s.find("#", i) # start from i to avoid repeat words
            length = int(s[i:delim])
            i = delim+1
            decoded.append(s[i:i+length])
            i += length
        
        return decoded
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))