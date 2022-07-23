import string


def contains_punc(str):

    return any( 
        char in string.punctuation
        for char in str
    )

print(contains_punc("SUPER"))
print(contains_punc("sup'*ers's"))

