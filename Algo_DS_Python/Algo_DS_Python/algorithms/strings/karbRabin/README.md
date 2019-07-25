# karpRabin: - O(n+m) n being the length of substring and m being the length of the larger substring
> This algorithim finds if a string is contanied in a larger string and returns how much times those matches occur.
## This algorithm finds matches by applying a rolling hash to all values of substrings  in larger string and comparing it to the hash value of string s. If the two hashes match at any point then the algorithm checks if the strings match. This avoids having to do comparisons on every character in every possible substring and instead does on compare of the hash values saving memory and making the algorithm faster.

