import nltk


G=nltk.CFG.fromstring(
        """
                     S -> "a" B | "b" A | "a" S | "b" A A | "a"
                     B -> "b" S | "a" B B | "b" 
                     A -> "a" 
        """
                     )


Parser=nltk.parse.RecursiveDescentParser(G)


char = ["a","a","b"]


for tree in Parser.parse(char):
    tree.draw()
