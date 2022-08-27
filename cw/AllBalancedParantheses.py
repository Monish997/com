# Write a function which makes a list of strings representing all of the ways you can
# balance n pairs of parentheses

# Examples
# balanced_parens(0) => [""]
# balanced_parens(1) => ["()"]
# balanced_parens(2) => ["()()","(())"]
# balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]


def balanced_parens(n):
    stack = [("", n, 0)]
    result = []

    while stack:
        current, left, right = stack.pop()

        if left == 0 and right == 0:
            result.append(current)

        if left > 0:
            stack.append((current + "(", left - 1, right + 1)) # type: ignore

        if right > 0:
            stack.append((current + ")", left, right - 1)) # type: ignore

    return result
