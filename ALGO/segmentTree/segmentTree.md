https://www.hackerrank.com/contests/hack-the-interview-ii-global/challenges/maximal-char-requests

In this challenge, a string and a list of intervals are given. The string consists of English letters only and it can contain both lowercase and uppercase letters.

For two different letters, we say that the first letter is greater than the second letter when the first letter comes later in the alphabet than the second letter ignoring the case of the letters. For example, the letter 'Z' and 't' are greater than the letters 'b' and 'G', while the letters 'B' andd 'b' are equal as case is not considered.

The task is the following. For each given interval, you need to find the count of the greatest letter occurring in the string in that interval, ignoring the case of the letters, so occurrences of, for example,  and  are occurrences of the same letter.

Consider, for example, for the string "AbaBacD". In the interval, [0, 4], the greatest letter is 'b' with count 2.
