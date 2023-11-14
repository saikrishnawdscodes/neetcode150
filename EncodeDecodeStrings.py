# Approach - just implement a simple encode and decode pattern
# encode - simple addition of a chracter sequence like ":;" after each list entity. encode creates one encoded string based on the list of strings
# decode should simialrly get back the original output.

class Codec:
    
    def encode(self, strs):
        return ":;".join(strs)
    
    def decode(self, encoded_str):
        if not encoded_str or encoded_str == ":;":
            return []
        else:
            return encoded_str.split(":;")

# strs = ["lint","code","love","you"]
# strs = ["we", "say", ":", "yes"]
strs = []
codec = Codec()
encoded_output = codec.encode(strs)

print(encoded_output)

decoded_output = codec.decode(encoded_output)

print(decoded_output)

# TC - O(n) - traversing through the list
# SC: O(n) - we are using the .join() method - this join method 

# Here, ':;'.join(strs) creates a new string by concatenating all the strings in the list strs using the ':;' delimiter. The space required for this new string is proportional to the total length of all strings in strs plus the length of the delimiter.
# Therefore, the space complexity of the encode function is O(n), where n is the total length of the input strings.
# The decode function, on the other hand, has a space complexity of O(1) because it uses the split method to create a list of strings, and the space required for this list is not proportional to the length of the input strings.
